import tkinter as tk
import threading
import time
from services.timer_services import TimerService
from services.notification_service import NotificationService

class TimerView(tk.Frame):
    def __init__(self, parent, user_name, duration_minutes):
        super().__init__(parent)
        self.user_name = user_name
        self.duration_seconds = duration_minutes * 60
        self.remaining = self.duration_seconds
        self.timer_service = None

        self.label = tk.Label(self, text=f"{self.user_name}, Ready to Study!", font=("Arial", 14))
        self.label.pack(pady=10)

        self.time_label = tk.Label(self, text=self.format_time(self.remaining), font=("Arial", 24))
        self.time_label.pack(pady=10)

        self.start_btn = tk.Button(self, text="Start Timer", command=self.start_timer)
        self.start_btn.pack(side="left", padx=10, pady=20)

        self.stop_btn = tk.Button(self, text="Stop Timer", command=self.stop_timer)
        self.stop_btn.pack(side="right", padx=10, pady=20)

    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02}:{secs:02}"

    def update_display(self):
        self.time_label.config(text=self.format_time(self.remaining))
        if self.remaining > 0 and self.timer_service and self.timer_service._running:
            self.remaining -= 1
            self.after(1000, self.update_display)
        elif self.remaining == 0:
            notifier = NotificationService()
            notifier.notify("⏰ Time’s up! Take a break!")

    def start_timer(self):
        if not self.timer_service:
            self.timer_service = TimerService(self.duration_seconds, self.timer_finished)
        self.remaining = self.duration_seconds
        self.timer_service.start()
        self.update_display()

    def stop_timer(self):
        if self.timer_service:
            self.timer_service.stop()
            self.label.config(text="Timer stopped.")

    def timer_finished(self):
        self.label.config(text="Session Completed!")
