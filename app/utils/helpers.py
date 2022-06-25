from werkzeug.security import generate_password_hash, check_password_hash
from flask import abort, make_response, jsonify
import json


def hash_create(string):
    return generate_password_hash(string)


def hash_verify(encrypt, string):
    return check_password_hash(encrypt, string)


def time_serial(datetime):
    print(datetime)
    return json.dumps(datetime)


def http_error(error=404, message='Not found!'):
    return abort(make_response(jsonify({'status': 'error', 'message': message}), error))
