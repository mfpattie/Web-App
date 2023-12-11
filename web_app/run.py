from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevelopmentConfig, TestingConfig, ProductionConfig
from flask_login import LoginManager
from app.models.user_model import User
from app.main import main as main_blueprint
from app.auth import auth as auth_blueprint

db = SQLAlchemy()  # Instantiate SQLAlchemy with no arguments here.

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app(config_name):
    app = Flask(__name__)

    # Configure the app using the provided config name
    if config_name == 'development':
        app.config.from_object(DevelopmentConfig)
    elif config_name == 'testing':
        app.config.from_object(TestingConfig)
    elif config_name == 'production':
        app.config.from_object(ProductionConfig)
    else:
        # If an unrecognized config_name is provided, use development settings
        app.config.from_object(DevelopmentConfig)

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    app.config.from_pyfile('config.py')

    db.init_app(app)

    # Place any blueprint registration or other app setup here.
    # For example, to register routes from a 'routes.py' you would import and register blueprints.

    return app


if __name__ == '__main__':
    # Here, you should call create_app with the desired profile to run it with that config.
    # Replace with 'testing' or 'production' as needed.
    flask_app = create_app('development')
    # Running with debug=True is not recommended in a production environment.
    flask_app.run(debug=True)
