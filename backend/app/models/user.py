from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import db
from datetime import datetime


# User model
class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, comment="User ID")
    username = db.Column(db.String(80), unique=True,
                         nullable=False, comment="Username")
    email = db.Column(db.String(120), unique=True,
                      nullable=False, comment="Email")
    auth_provider = db.Column(
        db.String(50), default="local", comment="local or google")

    # Password Authentication
    password_hash = db.Column(db.Text, nullable=True, comment="Password Hash")

    # Google Authentication
    sub = db.Column(db.String(255), unique=True,
                    nullable=True, comment="Google ID")
    picture = db.Column(db.String(500), nullable=True,
                        comment="Avatar URL From Google")

    # Timestamps
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, comment="Created At")
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, comment="Updated At")
    last_login_at = db.Column(
        db.DateTime, nullable=True, comment="Last Login At")

    # Encrypt password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check if login password is correct
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
