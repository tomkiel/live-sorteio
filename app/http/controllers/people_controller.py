from flask import jsonify
from flask import request
from app.database.repositories import people_repository
from app.utils.helpers import http_error
import json


def get_all():
    people = people_repository.get_all()
    return jsonify({"people": people})


def send_name():
    name = request.json.get("name") or http_error(400, "Invalid name")
    person = people_repository.create_person(name)
    return jsonify(
        {
            "person": person,
            "message": "Pessoa salvo com sucesso!"
        }
    ), 200