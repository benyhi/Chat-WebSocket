from flask_socketio import Namespace, emit
from flask import request

class ChatNamespace(Namespace):
    def on_connect(self):
        cliente = request.sid
        print(cliente)
        emit('message', {'text':'Bienvenido al chat!', 'sender':'Servidor'})

    def on_disconnect(self):
        return("desconectado")

    def on_join(self):
        emit('message', {'msg': 'Bienvenido a la sala de chat 1'})

    def on_leave(self):
        emit('message', {'msg': 'Saliste de la sala'})

    def on_message(self, data):
        print(f'Mensaje recibido {data}')
        emit('message', data)