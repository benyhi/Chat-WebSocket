from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    create_access_token,
    jwt_required,
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app import db
from ..models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=username,)

        return jsonify({'Token': access_token, 'Username': username})

    return jsonify({'Mensaje':'El usuario o contraseña no coinciden.'})

@auth_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    email = data['email']
    username = data['username']
    password = data['password']

    if email and username and password:
        try:
            new_user= User(
                email = email,
                username = username,
                password_hash = generate_password_hash(password)
            )
            db.session.add(new_user)
            db.session.commit()

            return jsonify({'Mensaje':'Usuario creado exitosamente'}), 200

        except Exception as e:
            return jsonify({'Mensaje':'El usuario ya existe', 'Error': str(e)})  
    
    else: 
        return jsonify({'Mensaje':'Se deben completar todos los campos requeridos'})
        
@auth_bp.route('/user/<int:id>', methods=['GET','PUT'])
@jwt_required()
def edit_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    
    if request.method == 'GET':
        if user:
            return jsonify({ 'username': user.username, 'email': user.email })
    
    if request.method == 'PUT':
        if not data or 'username' not in data or 'password' not in data or 'new_password' not in data or 'email' not in data:
            return jsonify({'Mensaje': 'Faltan datos necesarios'}), 400
            
        try:
            if data['username'] != user.username:
                user.username = data['username']

            if data['email'] != user.email:
                user.email = data['email']
                
            if check_password_hash(user.password_hash, data['password']):

                if data['new_password'] != data['password']:
                    user.password_hash = generate_password_hash(data['new_password'])

                else:
                    return jsonify({'Mensaje':'La contraseña ingresada no coincide con tu contraseña actual'}), 400
                
            else:
                return jsonify({'Mensaje':'No puedes crear una nueva contraseña identica a la actual'}), 400
        
            db.session.commit()
            return jsonify({'Mensaje':'Usuario actualizado con exito'}), 200
        
        except Exception as e:
            return jsonify({'Error': str(e)})
        
