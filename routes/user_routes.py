from flask import Blueprint, render_template, request, redirect, url_for
from database.connection import DatabaseConnection
from database.user_repository import UserRepository
from database.session_repository import SessionRepository

user_bp = Blueprint("user", __name__)
db = DatabaseConnection()
repo = UserRepository(db)
session_repo = SessionRepository(db)

@user_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        duration = request.form.get("duration")

        if not name or not duration:
            return "❌ Name and duration are required", 400

        duration = int(duration)
        sound = request.files.get("sound")

        sound_file = None
        if sound and sound.filename:
            sound_file = f"static/sound/{sound.filename}"  # ✅ match folder
            sound.save(sound_file)

        # Save user
        user_id = repo.add_user(name, sound_file)

        # Save session
        session_id = session_repo.add_session(user_id, duration)

        # Redirect with user_id included ✅
        return redirect(url_for(
            "timer.timer_view",
            user_name=name,
            duration=duration,
            sound_file=sound_file,
            user_id=user_id
        ))

    return render_template("index.html")
