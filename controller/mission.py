from flask import Blueprint, jsonify
from returns.result import Success, Failure

from repository.mission_repository import get_all_missions, get_mission_by_id

mission_blueprint = Blueprint('mission', __name__)



@mission_blueprint.route('/', methods=['GET'])
def get_all_missions_c():
    missions_result = get_all_missions()

    if isinstance(missions_result, Success):
        missions = missions_result.unwrap()
        return jsonify(missions[:500]), 200
    elif isinstance(missions_result, Failure):
        error_message = missions_result.failure()
        return jsonify({'error': error_message}), 500



@mission_blueprint.route('/<int:mission_id>', methods=['GET'])
def get_mission(mission_id: int):

    result = get_mission_by_id(mission_id)

    if isinstance(result, Success):
        return jsonify(result.unwrap()), 200
    else:
        return jsonify({"error": result.failure()}), 404