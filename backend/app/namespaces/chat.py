from flask_socketio import Namespace, emit, join_room, leave_room
from flask import request

class ChatNamespace(Namespace):
    def __init__(self, namespace=None):
        super().__init__(namespace)
        self.users = {}

    def on_connect(self):
        if request.sid in self.users:
            print(self.users)
            user = self.users.get(request.sid)
            emit('message', {'text': f'{user} se ha conectado', 'sender': 'Servidor'}, broadcast=True, include_self=False)
            emit('message', {'text':'Bienvenido al chat!', 'sender':'Servidor'})

    def on_disconnect(self):
        user = self.users.get(request.sid)
        emit('message', {'text': f'{user} se ha desconectado', 'sender': 'Servidor'})
        self.users.pop(request.sid)

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
        sender = self.users.get(request.sid)
        self.emit('message', {'text': message, 'sender':sender})

    def on_set_username(self, username):
        if username:    
            self.users[request.sid] = username
            print(f"Usuarios {username} conectado con el SID {request.sid}")