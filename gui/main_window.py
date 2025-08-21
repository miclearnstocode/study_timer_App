import tkinter as tk
from .user_form import UserForm
from .timer_view import TimerView

class MainWindow(tk.Frame):   # Inherit from Frame
    def __init__(self, root):
        super().__init__(root)  # initialize Frame
        self.root = root
        self.user_form = UserForm(self, self.show_timer_view)  # attach to self (frame)
        self.user_form.pack(fill="both", expand=True)
        self.timer_view = None

    def show_timer_view(self, user_name, duration):
        self.user_form.pack_forget()
        self.timer_view = TimerView(self, user_name, duration)
        self.timer_view.pack(fill="both", expand=True)
