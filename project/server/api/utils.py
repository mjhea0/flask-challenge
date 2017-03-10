# project/server/api/utils.py


import base64
import json
import uuid
from functools import wraps

import pandas as pd
from flask import abort, request, jsonify, make_response

from project.server import app
from .schema import schema, validate


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        if not request.json:
            abort(400)
        return f(*args, **kw)
    return wrapper


def validate_schema(f):
    @wraps(f)
    def wrapper(*args, **kw):
        if not validate(request.json):
            return make_response(jsonify(
                {'status': '400', 'error': 'Invalid payload'}), 400)
        return f(*args, **kw)
    return wrapper


def write_data(data):
    with open(app.config['DATA_FILE']) as f:
        current = json.load(f)
    current.append(data)
    with open(app.config['DATA_FILE'], mode='w') as f:
        f.write(json.dumps(current, indent=2))


def update_stats():
    with open(app.config['DATA_FILE']) as f:
        container = []
        for row in json.load(f):
            for key, value in row.items():
                if key == 'events':
                    for obj in value:
                        container.append(obj)
        df = pd.DataFrame(container)
        uuid = create_uuid()
        data = {
            'uuid': uuid,
            'name': 'event_duration',
            'stats': df['event_duration'].describe().to_dict()
        }
    with open(app.config['STATS_FILE']) as f:
        current = json.load(f)
    current.append(data)
    with open(app.config['STATS_FILE'], mode='w') as f:
        f.write(json.dumps(current, indent=2))
    return uuid
    

def get_stats(uuid):
    with open(app.config['STATS_FILE']) as f:
        if not uuid:
            return json.load(f)
        else:
            for stat in json.load(f):
                if stat['uuid'] == uuid:
                    return stat


def create_uuid():
    string = (base64.urlsafe_b64encode(uuid.uuid4().bytes)).decode('utf-8')
    return string.replace('=', '')
