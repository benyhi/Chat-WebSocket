from flask import Flask
from flask_socketio import SocketIO


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key?'
    
    socketio = SocketIO(app, cors_allowed_origins="*")   
    
    # Registarar blueprints
    from .routes import register_blueprints
    register_blueprints(app)

    # Registrar namespaces
    from .namespaces import namespaces
    for namespace in namespaces:
        socketio.on_namespace(namespace)

    return app
