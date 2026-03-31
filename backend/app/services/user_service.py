from flask_jwt_extended import create_access_token
from flask import redirect
import json
import time
import requests as py_requests
from datetime import datetime
from google.auth.transport import requests as gg_requests
from google.oauth2 import id_token as gg_id_token
from urllib.parse import quote
from ..models.user import User
from ..schemas.user_schema import user_schema
from ..extensions import db
from ..settings import JWT_ACCESS_TOKEN_EXPIRES, GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, \
    GOOGLE_REDIRECT_URI, GOOGLE_TOKEN_URL


# Create new user (local)
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


# Get user profile
def get_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return None
    return user_schema.dump(user)


# Authenticate user (local)
def login_user(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return {'message': 'Invalid username or password'}, 401
    access_token = create_access_token(
        identity=str(user.id),
        expires_delta=JWT_ACCESS_TOKEN_EXPIRES
    )
    user.last_login_at = datetime.utcnow()
    db.session.commit()
    return {'access_token': access_token, 'user': user_schema.dump(user)}, 200


# Authenticate user (google)
def GoogleCallback(code):
    # get token from code
    rq_body = {
        "code": code,
        "client_id": GOOGLE_CLIENT_ID,
        "client_secret": GOOGLE_CLIENT_SECRET,
        "redirect_uri": GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code"
    }
    tokens = py_requests.post(
        GOOGLE_TOKEN_URL, headers={
            "Content-Type": "application/x-www-form-urlencoded"},
        data=rq_body
    ).json()

    if 'error' in tokens:
        return "FAILED TO GET TOKENS"
    print("BOMXANH_DEBUG_GOOGLE_TOKEN IS: " + f"{tokens}")

    # ID Token Verification & Decoding (Get User info)
    id_token = tokens.get('id_token')
    print("BOMXANH_DEBUG_ID_TOKEN IS: " + f"{id_token}")

    time.sleep(1.5)
    user_info_from_google = gg_id_token.verify_oauth2_token(
        id_token,
        gg_requests.Request(),
        GOOGLE_CLIENT_ID
    )

    print("BOMXANH_DEBUG_USER_INFO_FROM_GOOGLE IS:\n" +
          json.dumps(user_info_from_google, indent=4))

    # Create new account if not exists
    user = User.query.filter_by(sub=user_info_from_google['sub']).first()
    if not user:
        user = User(
            sub=user_info_from_google.get('sub'),
            email=user_info_from_google.get('email'),
            auth_provider='google',
            picture=user_info_from_google.get('picture'),
            username=user_info_from_google.get('name')
        )
        db.session.add(user)
        db.session.commit()

    # Create App access_token & Login
    user = User.query.filter_by(sub=user_info_from_google['sub']).first()
    acc_token = create_access_token(
        identity=str(user.id),
        expires_delta=JWT_ACCESS_TOKEN_EXPIRES
    )
    user.last_login_at = datetime.utcnow()
    db.session.commit()

    return redirect("http://localhost:5173/gg-auth-success?access_token=" + quote(acc_token), code=302)
