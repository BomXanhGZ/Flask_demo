from flask import Flask
from .extensions import db, ma, cors, jwt
from . import settings
from .controller.user_controller import user_bp
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    # Load configuration from settings module
    app.config.from_object(settings)

    # Initialize extensions
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)

    # Initialize Flask-Migrate
    migrate = Migrate(app, db)

    # Register blueprints (controllers)
    app.register_blueprint(user_bp, url_prefix=settings.API_PREFIX)

    return app
