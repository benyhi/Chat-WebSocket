from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from datetime import timedelta

socketio = SocketIO(cors_allowed_origins="*")   
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret_key?'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base_datos.db'
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

    # Inicializacion de objetos
    db.init_app(app)
    CORS(app, resources={r"/*": {"origins": "http://localhost:*"}})
    socketio.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Registarar blueprints
    from .routes import register_blueprints
    register_blueprints(app)

    # Registrar namespaces
    from .namespaces import namespaces
    for namespace in namespaces:
        socketio.on_namespace(namespace)

    return app
