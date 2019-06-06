import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import app_config

# instantiate the db
db = SQLAlchemy()

def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)

    # set config
    env_config = os.getenv('ENV_CONFIG')
    app.config.from_object(app_config[env_config])

    # set up extensions
    db.init_app(app)

    # register blueprints
    from .key_metrics import keymetrics_blueprint

    app.register_blueprint(keymetrics_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
