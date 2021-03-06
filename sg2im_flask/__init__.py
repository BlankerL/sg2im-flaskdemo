from flask import Flask
from .extensions import cors


def create_app():
    app = Flask(__name__)
    cors.init_app(app)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
