from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..services import user_service


# Create user route group
user_bp = Blueprint('user', __name__)


# Register user (local)
@user_bp.route('/register', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = user_service.create_user(data)
    return jsonify(new_user), 201


# Login user (local)
@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result, status = user_service.login_user(
        data['username'], data['password'])
    return jsonify(result), status


# Get profile
@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = user_service.get_profile(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify(user), 200


# Authenticate user (google) controller
@user_bp.route('/auth/google-callback', methods=['GET'])
def authGoogleCallback():
    code = request.args.get('code')
    if not code:
        return {"error": "Missing authorization code"}, 400
    # --- rederect to FE ---
    result = user_service.GoogleCallback(code)
    return result
