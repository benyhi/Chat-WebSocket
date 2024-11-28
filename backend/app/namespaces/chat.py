from flask_socketio import Namespace, emit, join_room, leave_room
from flask import request

class ChatNamespace(Namespace):
    def on_connect(self):
        cliente = request.sid
        emit('message', {'text': f'{cliente} se ha conectado', 'sender': 'Servidor'}, broadcast=True, include_self=False)
        emit('message', {'text':'Bienvenido al chat!', 'sender':'Servidor'})

    def on_disconnect(self):
        return("desconectado")

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
        sender = data.get('sender')
        self.emit('message', {'text': message, 'sender':sender})