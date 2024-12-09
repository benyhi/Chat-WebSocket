from flask import Blueprint
from flask_jwt_extended import jwt_required

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat')
@jwt_required
def chat_1():
    pass