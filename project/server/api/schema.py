# project/server/api/schema.py

schema = [
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

def validate(data):
    keys = []
    for key, value in data.items():
        keys.append(key)
    return set(keys) == set(schema)
