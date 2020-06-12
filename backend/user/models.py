from datetime import datetime

import flask
import flask_jwt_extended
import sqlalchemy.exc

from backend import bcrypt, db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def check_password(self, password: str) -> bool:
        return bcrypt.check_password_hash(self.password, password)

    @classmethod
    def create_user(cls, email: str, password: str) -> 'User':
        encrypted_pass = bcrypt.generate_password_hash(password).decode('utf-8')
        user = cls(email=email, password=encrypted_pass)

        try:
            db.session.add(user)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            flask.abort(409, "User with this email aleady exists.")

        return user

    @classmethod
    def get_token(cls, email: str, password: str) -> str:
        user = cls.query.filter_by(email=email).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            flask.abort(403, "Invalid credentials.")

        return flask_jwt_extended.create_access_token(identity=user.id)

    @classmethod
    def get_user(cls, user_id: int) -> 'User':
        return cls.query.get(user_id)
