from flask import Flask
from flask_cors import CORS
from dynaconf import settings
from app.core import configuration

static_dir = settings.get("APP_DIR") + settings.get("STATIC_DIR")
views_dir = settings.get("APP_DIR") + settings.get("VIEWS_DIR")

def construct(**config):
    app = Flask(__name__, static_folder=static_dir, template_folder=views_dir)
    configuration.init_app(app, **config)
    CORS(app)
    return app


def create_app(**config):
    app = construct(**config)
    configuration.load_extensions(app)
    return app

"""
Create a new app instance.
"""
app = create_app()