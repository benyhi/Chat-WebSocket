from flask_socketio import Namespace, emit, join_room, leave_room, disconnect
from flask import request, jsonify
from flask_jwt_extended import decode_token
from flask_jwt_extended.exceptions import NoAuthorizationError, FreshTokenRequired, RevokedTokenError, InvalidHeaderError

class ChatNamespace(Namespace):
    def __init__(self, namespace=None):
        super().__init__(namespace)
        self.connected_users = {}

    def on_connect(self, token):
        token = request.args.get('token')

        if not token:
            print("No se recibio token, desconectando....")
            disconnect()
            return
        
        try:
            decoded_token = decode_token(token)
            username = decoded_token['sub']     # ""Convencion"" , 'sub' almacena el identificador del usuario
            self.connected_users[request.sid] = username
            print(f"{username} conectado con el SID {request.sid}")

        #Manejo de errores de Tokens
        except (NoAuthorizationError, InvalidHeaderError) as e:
            # Si no se proporciona un token o el encabezado es inválido
            return jsonify({"error": "No se proporcionó un token de acceso o el encabezado es inválido."}), 401
        except FreshTokenRequired as e:
            # Si el token ha expirado
            return jsonify({"error": "El token ha expirado."}), 401
        except RevokedTokenError as e:
            # Si el token ha sido revocado
            return jsonify({"error": "El token ha sido revocado."}), 401
        except Exception as e:
            # Para otros errores inesperados
            return jsonify({"error": "Error desconocido.", "details": str(e)}), 500


    def on_disconnect(self):
        username = self.connected_users.pop(request.sid, None)
        emit('message', {'text': f'{username} se ha desconectado', 'sender': 'Servidor'})

    def on_join(self, data):
        room = data.get('room')
        join_room(room)
        self.emit('message', {'text': 'Bienvenido a la sala de chat 1', 'sender':'Servidor'})

    def on_leave(self, data):
        room = data.get('room')
        leave_room(room)
        print('Desconectado de la sala de chat 1.')

    def on_message(self, data):
        print(f'Mensaje recibido {data}')
        message = data.get('text')
        username = self.connected_users.get(request.sid)
        print(username)
        self.emit('message', {'text': message, 'sender':username})