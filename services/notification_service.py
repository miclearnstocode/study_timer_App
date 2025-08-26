from interfaces.notifier_interface import NotifierInterface
import tkinter.messagebox as msg
import pygame
import os


class NotificationService(NotifierInterface):
    def __init__(self, sound_file=None, default_sound="i_feel_good.mp3"):
        pygame.mixer.init()

        # Get project root
        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        sounds_dir = os.path.join(PROJECT_ROOT, "assets", "sound")

        # If no custom sound given, fallback to default
        if sound_file and os.path.exists(sound_file):
            self.sound_file = sound_file
        else:
            self.sound_file = os.path.join(sounds_dir, default_sound)

        if not os.path.exists(self.sound_file):
            print(f"[WARNING] Sound file {self.sound_file} not found. No sound will play.")

    def notify(self, message: str):
        """Play sound + show popup."""
        if os.path.exists(self.sound_file):
            try:
                pygame.mixer.music.load(self.sound_file)
                pygame.mixer.music.play()
            except Exception as e:
                print(f"[ERROR] Could not play sound: {e}")

        msg.showinfo("Study Timer", message)
        print(f"Notification: {message}")

        if os.path.exists(self.sound_file):
            pygame.mixer.music.stop()
