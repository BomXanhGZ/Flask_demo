from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services import user_service

user_bp = Blueprint('user', __name__)


@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = user_service.get_profile(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user), 200


@user_bp.route('/register', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = user_service.create_user(data)
    return jsonify(new_user), 201


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result, status = user_service.authenticate_user(
        data['username'], data['password'])
    return jsonify(result), status
