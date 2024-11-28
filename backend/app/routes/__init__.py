from .main_view import main_bp
from .chat_view import chat_bp
from .auth_view import auth_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(auth_bp)