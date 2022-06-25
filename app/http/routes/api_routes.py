from flask import Blueprint
from app.http.controllers import api_controller

api = Blueprint("api", __name__, url_prefix="/api")


@api.route("/", methods=["GET"])
def index():
    return api_controller.index()


def init_app(app):
    app.register_blueprint(api)
