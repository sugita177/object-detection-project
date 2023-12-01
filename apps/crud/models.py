from datetime import datetime

from apps.app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    # table name is plural
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, index=True, unique=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )
    user_images = db.relationship(
        "UserImage", backref="user"
    )

    @property
    def password(self):
        raise AttributeError("読み取り不可")

    @password.setter
    def password(self, password: str):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def is_duplicate_email(self) -> bool:
        return User.query.filter_by(email=self.email).first() is not None


@login_manager.user_loader
def load_user(user_id: int):
    return User.query.get(user_id)
