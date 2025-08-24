from interfaces.notifier_interface import NotifierInterface
import tkinter.messagebox as msg
import pygame
import os


class NotificationService(NotifierInterface):
    def __init__(self, sound_name="i_feel_good.mp3"):
        pygame.mixer.init()

        # Get project root (parent of "services")
        PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.sound_file = os.path.join(PROJECT_ROOT, "assets", "sound", sound_name)

        # Ensure file exists
        if not os.path.exists(self.sound_file):
            print(f"[WARNING] Sound file {self.sound_file} not found. No sound will play.")

    def notify(self, message: str):
        """Show a notification with sound + messagebox."""
        # Play sound if file exists
        if os.path.exists(self.sound_file):
            try:
                pygame.mixer.music.load(self.sound_file)
                pygame.mixer.music.play()
            except Exception as e:
                print(f"[ERROR] Could not play sound: {e}")

        # Show Tkinter popup
        msg.showinfo("Study Timer", message)
        print(f"Notification: {message}")
        # Stop sound after messagebox is closed
        if os.path.exists(self.sound_file):
            pygame.mixer.music.stop()