class ChatClient{
    constructor(namespace){
        this.namespace = namespace
        this.socket = io(namespace)

        // DOM
        this.messageInput = document.getElementById('chat-input')
        this.messageSend = document.getElementById('chat-send')
        this.messageDiv = document.getElementById('chat-message')

        this.socketEvents();
        this.domEvents();
    }

    // Inicializa los eventos del socket (conectarse, desconectarse, respuesta del servidor)
    socketEvents(){
        this.socket.on('connect', ()=>{
            console.log(`Conectado al chat ${this.namespace}`)
            alert(`Conectado a ${this.namespace}`)
        })

        this.socket.on('disconnect', ()=>{
            console.log(`Desconectado de ${this.namespace}`)
            alert(`Desconectado de ${this.namespace}`)
        })

        this.socket.on('response', (data)=>{
            console.log(`Mensaje del servidor: ${data}`)
        })
    }

    // Inicializa los eventos del DOM (boton enviar mensaje)
    domEvents(){
        this.messageSend.addEventListener('click',()=> this.sendMessage());
    }

    // Añadir mensaje al div en el front
    addMessage(text){
        const newMessage = document.createElement('p');
        newMessage.textContent = text
        this.messageDiv.appendChild(newMessage);
    }

    // Enviar mensajes al servidor
    sendMessage(){
        const message = this.messageInput.value.trim();
        if (message){
            this.socket.emit('message', message);
            this.addMessage(`Tu: ${message}`);
            this.messageInput.value = '';
        }
    }
}

document.addEventListener('DOMContentLoaded', ()=>{
    const Chat = new ChatClient('/chat');
})