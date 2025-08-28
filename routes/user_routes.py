import re
from flask import Blueprint, render_template, request, redirect, url_for, flash
from database.connection import DatabaseConnection
from database.user_repository import UserRepository
from database.session_repository import SessionRepository

user_bp = Blueprint("user", __name__)
db = DatabaseConnection()
repo = UserRepository(db)
session_repo = SessionRepository(db)

def validate_name(name: str) -> bool:
    return bool(re.match(r"^[A-Za-z ]+$", name.strip()))

def parse_duration(duration_input: str) -> int:
    """Convert input like '1', '1:30', '02:45', '1:30:00' into total seconds."""
    parts = duration_input.split(":")
    if len(parts) == 1 and parts[0].isdigit():
        # Just minutes
        return int(parts[0]) * 60
    elif len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
        # mm:ss
        minutes, seconds = map(int, parts)
        return minutes * 60 + seconds
    elif len(parts) == 3 and all(p.isdigit() for p in parts):
        # hh:mm:ss
        hours, minutes, seconds = map(int, parts)
        return hours * 3600 + minutes * 60 + seconds
    else:
        raise ValueError("Invalid duration format")

@user_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        duration_input = request.form.get("duration", "").strip()

        # ✅ Validation
        if not validate_name(name):
            flash("❌ Invalid name. Only letters and spaces allowed.", "error")
            return redirect(url_for("user.index"))

        try:
            duration = parse_duration(duration_input)
            if duration <= 0:
                flash("❌ Duration must be greater than 0.", "error")
                return redirect(url_for("user.index"))
        except ValueError:
            flash("❌ Invalid duration format. Use numbers or mm:ss.", "error")
            return redirect(url_for("user.index"))

        # Handle sound file
        sound = request.files.get("sound")
        sound_file = None
        if sound and sound.filename:
            sound_file = f"static/sound/{sound.filename}"
            sound.save(sound_file)

        # Save user & session
        user_id = repo.add_user(name, sound_file)
        session_repo.add_session(user_id, duration)

        return redirect(url_for("timer.timer_view", user_name=name, duration=duration, sound_file=sound_file, user_id=user_id))
    return render_template("index.html")
