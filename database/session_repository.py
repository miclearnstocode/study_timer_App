from database.connection import DatabaseConnection
import datetime

class SessionRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def add_session(self, user_id: int, duration: int):
        """Insert completed session with timestamp and return session_id."""
        conn = self.db.connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO sessions (user_id, duration, completed_at) VALUES (?, ?, ?)",
            (user_id, duration, datetime.datetime.now())
        )
        session_id = cur.lastrowid   # ✅ get inserted session ID
        conn.commit()
        print(f"[DEBUG] Session added for user_id={user_id}, duration={duration} min, session_id={session_id}")
        return session_id   # ✅ return new session ID

    def get_user_sessions(self, user_id: int):
        """Fetch all sessions for a user."""
        conn = self.db.connect()
        cur = conn.cursor()
        cur.execute("SELECT id, duration, completed_at FROM sessions WHERE user_id = ?", (user_id,))
        return cur.fetchall()

    def get_session_summary(self, user_id: int):
        """Get session count + last completed_at timestamp."""
        conn = self.db.connect()
        cur = conn.cursor()
        cur.execute(
            "SELECT COUNT(*), MAX(completed_at) FROM sessions WHERE user_id = ?", (user_id,)
        )
        count, last_completed = cur.fetchone()
        return count or 0, last_completed
