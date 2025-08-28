Study Timer App
Author: John Karl B. Denisado, Mary Pauline Silvino, Michael M. Estorque, Raymond Eusoff Mendoza, Reynan Christian Dordas, Syrah C. Fundal
Date: August 21, 2025

Project Overview
The Study Timer App is a simple and effective tool that helps users manage their study sessions using focused time intervals and breaks. It improves concentration, reduces procrastination, and helps build better study habits for long-term productivity.

Built with Python, Tkinter(GUI), SQLite3 (Database), and following OOP Principles with SRP (Single Responsibility Principle).

Main Features
Set custom study duration
Start/Stop timer
Notify user when time is up
Track completed study sessions per user

Folder Structure

StudyTimerApp/
│
├── main.py                         # Flask entry point
│
├── database/
│   ├── __init__.py
│   ├── connection.py                # Handles SQLite3 connection
│   └── user_repository.py           # User-related DB operations (CRUD)
│
├── models/
│   ├── __init__.py
│   ├── user.py                      # User class (OOP model)
│   └── session.py                   # Study session class (OOP model)
│
├── services/
│   ├── __init__.py
│   ├── timer_service.py             # Handles study/break timer logic
│   ├── notification_service.py      # Handles notifications (ISP applied)
│   └── session_service.py           # Manages study session tracking
│
├── interfaces/
│   ├── __init__.py
│   ├── notifier_interface.py        # Interface for notifications (ISP)
│   └── timer_interface.py           # Interface for timer (ISP)
│
├── routes/
│   ├── __init__.py
│   ├── user_routes.py               # User input routes
│   ├── timer_routes.py              # Timer actions (start, stop)
│   └── session_routes.py            # Completed session tracking
│
├── templates/                       # Jinja2 HTML templates
│   ├── base.html                    # Base layout
│   ├── index.html                   # Landing page (user form)
│   ├── timer.html                   # Timer UI (start/stop buttons)
│   └── sessions.html                # Completed sessions page
│
├── static/                          # CSS/JS/Images
│   ├── css/
│   │   └── style.css                # Styling
│   ├── js/
│   │   └── timer.js                 # Timer countdown logic (frontend)
│   └── images/
│       └── logo.png
│
└── utils/
    ├── __init__.py
    └── helpers.py                   # Utility/helper functions



User Flow
1. User opens the app
2. App asks for user name and study duration
3. Users clicks Start
4. Timer runs and updates in real time 
5. App notifies when time is up
6. Session is saved to database and user can track completed sessions

Installation
1. Clone the repository

git clone https://github.com/yourusername/StudyTimerApp.git
cd StudyTimerApp

2. Make sure you have Python 3.10+ installled
3. Install required dependencies (Tkinter is usually bundled with python)
pip install -r requirements.txt

Running the App
python main.py

Database
Uses SQLite3 (study_timer.db)
Tables:
    users (id, name)
    sessions (id, user_id, duration, completed_at)

Principles Applied
OOP - User and Session models, encapsulated logic
SRP - Each module has a single responsibility (DB, models, GUI, Services)

Future Improvents
For individual feature to be implemented by our group.