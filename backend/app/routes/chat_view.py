from flask import Blueprint

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat/1')
def chat_1():
    pass