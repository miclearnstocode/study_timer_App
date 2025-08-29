from flask import Blueprint, render_template
from database.connection import DatabaseConnection
from database.session_repository import SessionRepository
from database.user_repository import UserRepository

session_bp = Blueprint("sessions", __name__)
db = DatabaseConnection()
repo = UserRepository(db)
session_repo = SessionRepository(db)

@session_bp.route("/sessions/<int:user_id>")
def sessions(user_id):
    # Get user info (dict)
    user = repo.get_user(user_id)

    # Access name from dict instead of .name
    user_name = user["name"]

    # Fetch sessions by name
    sessions = session_repo.get_user_sessions_by_name(user_name)

    count = len(sessions)
    last_completed = sessions[0].completed_at if sessions else None

    return render_template("session.html", user=user, sessions=sessions, count=count, last_completed=last_completed)
