from flask import Blueprint, render_template, request
from database.connection import DatabaseConnection
from database.user_repository import UserRepository
from database.session_repository import SessionRepository

session_bp = Blueprint("sessions", __name__)
db = DatabaseConnection()
user_repo = UserRepository(db)
session_repo = SessionRepository(db)

@session_bp.route("/sessions/<int:user_id>")
def sessions(user_id):
    user = user_repo.get_user(user_id)  # you may need to add this method if missing
    sessions = session_repo.get_user_sessions(user_id)
    count, last_completed = session_repo.get_session_summary(user_id)

    return render_template("session.html",user=user, sessions=sessions, count=count, last_completed=last_completed)
