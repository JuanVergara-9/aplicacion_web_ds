from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config, TestingConfig
from app.views import main_bp  # Importa el Blueprint principal

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_name='default'):
    # Crea la aplicación Flask, especificando carpetas personalizadas para plantillas y estáticos
    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')


    # Configura la aplicación según el entorno especificado
    if config_name == 'testing':
        app.config.from_object(TestingConfig)
    else:
        app.config.from_object(Config)

    # Inicializa las extensiones con la instancia de la aplicación
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Configura la vista de login predeterminada para Flask-Login
    login_manager.login_view = 'main_bp.login'

    # Registra el Blueprint principal
    app.register_blueprint(main_bp)

    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    return app
