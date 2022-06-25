from app.database.models.people_model import People, PeopleSchema
from app.core.database import db
from sqlalchemy import exc
from app.utils.helpers import http_error


def get_all():
  people = People.query.all()
  return PeopleSchema(many=True).dump(people) or None

def get_person_by_name(name):
  person = People.query.filter(People.name == name).first() or http_error(404, "Not Found")
  return PeopleSchema(many=False).dump(person) or None

def create_person(name):
  try:
    person = People(name=name)
    db.session.add(person)
    db.session.commit()
    return PeopleSchema(many=False).dump(person) or None
  except exc.SQLAlchemyError as e:
    return http_error(500, "Ocorreu um erro!" + str(e))
