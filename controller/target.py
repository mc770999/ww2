from dataclasses import asdict

from flask import Blueprint, jsonify, request
from returns.maybe import Nothing
from toolz import pipe
from toolz.curried import reduce


from repository.target_repository import *
from models import Target

# from repository.target_repository import get_all_answers
# from repository.season_repository import get_all_questions, create_question
# from service.player_service import create_full_question_on_db

targets_blueprint = Blueprint("targets",__name__)

@targets_blueprint.route("/<int:target_id>", methods=['GET'])
def get_one(target_id : int):
    a = (find_target_by_id(target_id).unwrap().to_dict()
         if find_target_by_id(target_id) is not Nothing
         else {"error" : "cent get"})
    return jsonify(a), 200

@targets_blueprint.route("/all", methods=['GET'])
def get_all():
    targets = [t.to_dict() for t in list(get_all_target().unwrap() if get_all_target() is not Nothing else [])]
    return jsonify(targets), 200


@targets_blueprint.route("/", methods=['POST'])
def create():
    try:
        all_data = request.json
        new_target = Target(target_priority=all_data["target_priority"],target_type_id=all_data["target_type_id"],city_id=all_data["city_id"],target_industry=all_data["target_industry"])
        create_target(new_target)
        return jsonify(new_target.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}),400



@targets_blueprint.route("/<int:target_id>", methods=['PUT'])
def put(target_id : int):
    try:
        all_data = request.json
        # Create the question using the data from the request
        new_target = Target(target_priority=all_data["target_priority"],target_type_id=all_data["target_type_id"],city_id=all_data["city_id"],target_industry=all_data["target_industry"])
        target = find_target_by_id(target_id).unwrap() if find_target_by_id(target_id) is not Nothing else False
        if target:
            update_target(target_id,new_target)
            return jsonify(new_target.to_dict()), 201
        raise Exception("cent update")
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@targets_blueprint.route("/<int:target_id>", methods=['DELETE'])
def delete(target_id : int):
    try:
        return jsonify(f"{delete_target(target_id)}"), 201
    except Exception as e:
        return jsonify({"error": str(e)}),400
