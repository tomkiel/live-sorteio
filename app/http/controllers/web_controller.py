from flask import render_template
from dynaconf import settings
from app.database.repositories import people_repository
import json


def index():
    api_url = settings.get("APP_URL") + "/api/people/send-name"
    return render_template("index.html", api_url=api_url)

def login():
    return render_template("admin/login.html")


def list_people():
    people = people_repository.get_all() or []
    return render_template("admin/people.html", people=people)


def random():
    people = people_repository.get_all() or []
    return render_template("admin/random.html", people=json.dumps(people, indent=4))
