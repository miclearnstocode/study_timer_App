import tkinter as tk
import os, sys
# Add parent directory (study_timer_App) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gui.user_form import UserForm
from gui.timer_view import TimerView
from database.connection import DatabaseConnection
from database.user_repository import UserRepository
from database.session_repository import SessionRepository

class MainWindow(tk.Frame):   # Inherit from Frame
    def __init__(self, root):
        super().__init__(root)  # initialize Frame
        self.root = root

        # Initialize database
        self.db = DatabaseConnection()
        self.repo = UserRepository(self.db)
        self.session = SessionRepository(self.db)

        self.user_form = UserForm(self, self.show_timer_view)  # attach to self (frame)
        self.user_form.pack(fill="both", expand=True)
        self.timer_view = None

    def show_timer_view(self, user_name, duration):
        # Save user first
        print(f"[DEBUG] Saving user {user_name} to DB...")
        user_id = self.repo.add_user(user_name)
        print(f"[DEBUG] Inserted user_id = {user_id}")

        # Save session
        print(f"[DEBUG] Starting session for user_id={user_id}, duration={duration}")
        session_id = self.session.add_session(user_id, duration)
        print(f"[DEBUG] Inserted session_id = {session_id}")

        # Switch views
        self.user_form.pack_forget()
        self.timer_view = TimerView(self, user_name, duration)
        self.timer_view.pack(fill="both", expand=True)

