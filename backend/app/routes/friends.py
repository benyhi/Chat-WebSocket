from flask import Blueprint, request
from flask_jwt_extended import jwt_required

friends_bp = Blueprint('friends', __name__)


@friends_bp.route('/add-friend')
@jwt_required
def add_friend():
    data = request.get_json()
    


    pass

