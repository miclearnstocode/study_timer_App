import tkinter as tk

class UserForm(tk.Frame):
    def __init__(self, parent, on_submit_callback):
        super().__init__(parent)
        self.on_submit_callback = on_submit_callback

        tk.Label(self, text="Enter your name:").pack(pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5)

        tk.Label(self, text="Study duration (minutes):").pack(pady=5)
        self.duration_entry = tk.Entry(self)
        self.duration_entry.pack(pady=5)

        submit_btn = tk.Button(self, text="Start", command=self.submit)
        submit_btn.pack(pady=10)

    def submit(self):
        name = self.name_entry.get().strip()
        try:
            duration = int(self.duration_entry.get().strip())
        except ValueError:
            duration = 25  # default 25 minutes if invalid input
        if name:
            self.on_submit_callback(name, duration)
