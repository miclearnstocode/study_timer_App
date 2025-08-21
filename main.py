import tkinter as tk
from PIL import Image, ImageTk
from gui.main_window import MainWindow
from database.connection import DatabaseConnection

def main():
    # Initialize database
    db = DatabaseConnection()
    db.initialize()

    # Start GUI
    root = tk.Tk()
    root.title("Study Timer App")
    root.geometry("400x300")
    # Load and resize background image
    image = Image.open("study_timer_App/assests/study_timer.jpg")  # <-- fixed "assets"
    image = image.resize((400, 300))  # resize to match window size
    photo = ImageTk.PhotoImage(image)
    
    # Set background as a label
    background_label = tk.Label(root, image=photo)
    background_label.image = photo   # keep reference to avoid garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    app = MainWindow(root)
    app.pack(fill=tk.BOTH, expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()
