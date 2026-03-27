from flask_jwt_extended import create_access_token
from ..models.user import User
from ..schemas.user_schema import user_schema, users_schema
from ..extensions import db


# Find user by ID
def get_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return None
    return user_schema.dump(user)


# Save new user to DB
def create_user(data):
    # Check if user already exists
    if User.query.filter_by(username=data['username']).first():
        return {'message': 'User already exists'}, 400
    if User.query.filter_by(email=data['email']).first():
        return {'message': 'Email already exists'}, 400

    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])

    # Add user to database
    db.session.add(new_user)
    db.session.commit()
    return user_schema.dump(new_user)


# Verify user and generate JWT token
def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=str(user.id))
        return {'access_token': access_token, 'user': user_schema.dump(user)}, 200
    return {'message': 'Invalid username or password'}, 401
