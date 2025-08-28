from interfaces.notifier_interface import NotifierInterface
import os

class NotificationService(NotifierInterface):
    def __init__(self, sound_file=None, default_sound="i_feel_good.mp3"):
        # Ensure the sound file lives in /static/sound/
        if sound_file:
            self.sound_file = sound_file
        else:
            self.sound_file = os.path.join("static", "sound", default_sound)

    def notify(self, message: str):
        """Return a notification payload for the frontend (Flask → Browser)."""
        return {"message": message, "sound_file": self.sound_file}
