from database.connection import DatabaseConnection
from models.session import Session
from datetime import datetime

class SessionRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def add_session(self, user_id: int, duration: int):
        """Insert completed session with timestamp and return session_id."""
        conn = self.db.connect()
        cur = conn.cursor()
        cur.execute("INSERT INTO sessions (user_id, duration, completed_at) VALUES (?, ?, ?)",(user_id, duration, datetime.now().isoformat()))
        session_id = cur.lastrowid
        conn.commit()
        print(f"[DEBUG] Session added for user_id={user_id}, duration={duration}, session_id={session_id}")
        return session_id

    def get_user_sessions(self, user_id: int):
        """Fetch all sessions for a user (return Session objects with datetime)."""
        conn = self.db.connect()
        cur = conn.cursor()
        cur.execute("SELECT id, duration, completed_at FROM sessions WHERE user_id = ?", (user_id,))
        rows = cur.fetchall()

        sessions = []
        for row in rows:
            session_id, duration, completed_at = row
            # ✅ Parse completed_at string into datetime
            if isinstance(completed_at, str):
                try:
                    completed_at = datetime.fromisoformat(completed_at)
                except ValueError:
                    pass  # keep as string if parsing fails
            sessions.append(Session(session_id, user_id, duration, completed_at))
        return sessions
    # to get all the same name use by the user
    def get_user_sessions_by_name(self, name: str):
        """Fetch all sessions for users with the same name."""
        conn = self.db.connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT s.id, s.user_id, s.duration, s.completed_at, u.name
            FROM sessions s
            JOIN users u ON s.user_id = u.id
            WHERE u.name = ?
            ORDER BY s.completed_at DESC
        """, (name,))
        
        rows = cur.fetchall()
        sessions = []
        for row in rows:
            session_id, user_id, duration, completed_at, user_name = row
            # convert completed_at string → datetime
            if isinstance(completed_at, str):
                try:
                    completed_at = datetime.fromisoformat(completed_at)
                except ValueError:
                    pass
            sessions.append(Session(session_id, user_id, duration, completed_at))
        return sessions
    
    def get_session_summary(self, user_id: int):
        """Get session count + last completed_at timestamp."""
        conn = self.db.connect()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*), MAX(completed_at) FROM sessions WHERE user_id = ?", (user_id,))
        count, last_completed = cur.fetchone()

        # ✅ Convert last_completed string into datetime
        if isinstance(last_completed, str):
            try:
                last_completed = datetime.fromisoformat(last_completed)
            except ValueError:
                pass
        return count or 0, last_completed
