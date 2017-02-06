# seed.py


import os
import base64
import json
import uuid

import pandas as pd


basedir = os.path.abspath(os.path.dirname(__file__))
IN_FILE = os.path.join(basedir, 'challenge', 'data', 'sample.json')
DATA_FILE_DEV = os.path.join(basedir, 'project', 'server', 'data_dev.json')
STATS_FILE_DEV = os.path.join(basedir, 'project', 'server', 'stats_dev.json')
DATA_FILE_TEST = os.path.join(basedir, 'project', 'server', 'data_test.json')
STATS_FILE_TEST = os.path.join(basedir, 'project', 'server', 'stats_test.json')


SCHEMA = [
    'session_start_epoch',
    'layer',
    'session_duration',
    'uuid',
    'session_steps',
    'events',
    'session_attributes',
    'filter_results',
    'visitor_key',
    'session_start_datetime',
    'path_results'
]


def get_data():
    data = []
    with open(IN_FILE) as f:
        for line in f:
            data.append(json.loads(line))
    return data

def validate_data(json_data):
    keys = []
    for key, value in json_data.items():
        keys.append(key)
    return set(keys) == set(SCHEMA)

def write_data(data, file_name):
    with open(file_name, mode='w') as f:
        f.write(json.dumps(data, indent=2))

def create_data_frame(data):
    container = []
    for row in data:
        for key, value in row.items():
            if key == 'events':
                for obj in value:
                    container.append(obj)
    df = pd.DataFrame(container)
    return [{
        'uuid': create_uuid(),
        'name': 'event_duration',
        'stats': df['event_duration'].describe().to_dict()
    }]

def create_uuid():
    string = (base64.urlsafe_b64encode(uuid.uuid4().bytes)).decode('utf-8')
    return string.replace('=', '')


if __name__ == '__main__':
    current = []
    all_data = get_data()
    for row in all_data:
        if validate_data(row):
            current.append(row)
    stats = create_data_frame(current)
    write_data(stats, STATS_FILE_DEV)
    write_data(current, DATA_FILE_DEV)
    write_data([], STATS_FILE_TEST)
    write_data([], DATA_FILE_TEST)
    print('done!')
