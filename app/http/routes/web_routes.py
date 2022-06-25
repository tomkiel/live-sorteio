from flask import Blueprint
from app.http.controllers import web_controller

web = Blueprint("web", __name__)


@web.route("/", methods=["GET"])
def index():
    return web_controller.index()


@web.route("/login", methods=["GET"])
def login():
    return web_controller.login()


@web.route("/pessoas-cadastradas", methods=["GET"])
def list_people():
    return web_controller.list_people()


@web.route("/sorteio", methods=["GET"])
def random():
    return web_controller.random()


def init_app(app):
    app.register_blueprint(web)
