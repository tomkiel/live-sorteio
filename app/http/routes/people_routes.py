from app.http.controllers import people_controller
from flask import Blueprint

people = Blueprint("people", __name__, url_prefix="/api/people")


@people.route("/", methods=["GET"])
def index():
    return people_controller.get_all()


@people.route("/send-name", methods=["POST"])
def send_name():
    return people_controller.send_name()


def init_app(app):
    app.register_blueprint(people)
