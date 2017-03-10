# project/server/api/routes.py


from flask import Blueprint, request, jsonify, abort

from .utils import validate_json, validate_schema, \
    write_data, get_stats, update_stats


api_blueprint = Blueprint('api', __name__,)


# sanity check
@api_blueprint.route('/api/v1/ping', methods=['GET'])
def ping():
    return jsonify(
        {'status': '200', 'data': 'pong!'})


@api_blueprint.route('/api/v1/stats', methods=['GET'])
def get_all_stats():
    try:
        stats = get_stats(None)
    except:
        abort(500)
    return jsonify({'status': '200', 'data': stats})


@api_blueprint.route('/api/v1/stats/<uuid>', methods=['GET'])
def get_single_stat(uuid):
    try:
        stats = get_stats(uuid)
    except:
        abort(500)
    return jsonify({'status': '200', 'data': stats})


@api_blueprint.route('/api/v1/stats', methods=['POST'])
@validate_json
@validate_schema
def add_data():
    try:
        write_data(request.json)
        uuid = update_stats()
    except:
        abort(500)
    return jsonify(
        {'status': '200', 'data': {'status': 'success', 'uuid': uuid}})
