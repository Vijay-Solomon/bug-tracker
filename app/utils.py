from flask import session
from .models import User

def login_user(user):
    session["user_id"] = user.id
    session["username"] = user.username
    session["role"] = user.role

def logout_user():
    session.pop("user_id", None)
    session.pop("username", None)
    session.pop("role", None)

def current_user():
    uid = session.get("user_id")
    if not uid:
        return None
    return User.query.get(uid)
