from database.connection import DatabaseConnection

class SessionRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def add_session(self, user_id, duration):
        conn = self.db.connect()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO sessions (user_id, duration) VALUES (?, ?)",
            (user_id, duration))
        conn.commit()
        session_id = cur.lastrowid
        conn.close()
        return session_id
