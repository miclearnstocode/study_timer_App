from flask import Blueprint, render_template, request
from services.timer_services import TimerService
from services.notification_service import NotificationService

timer_bp = Blueprint("timer", __name__)

@timer_bp.route("/timer")
def timer_view():
    user_name = request.args.get("user_name")
    duration = int(request.args.get("duration"))
    sound_file = request.args.get("sound_file", None)
    user_id = request.args.get("user_id", None)   # <-- make sure this exists

    return render_template("timer.html", user_name=user_name, duration=duration, sound_file=sound_file, user_id=user_id)
