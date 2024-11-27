from .main_view import main_bp
from .chat_view import chat_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(chat_bp)