from database.connection import DatabaseConnection

class UserRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def add_user(self, name: str, sound_file: str = None):
        """Insert a new user with optional sound file preference."""
        try:
            conn = self.db.connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO users (name, sound_file, sessions_completed) VALUES (?, ?, ?)", (name, sound_file, 0))  # start with 0 sessions
            conn.commit()
            user_id = cur.lastrowid
            print(f"[DEBUG] Inserted user: {name}, sound_file={sound_file}, sessions_completed=0, id={user_id}", flush=True)
            return user_id
        except Exception as e:
            print(f"[ERROR] add_user failed: {e}", flush=True)
            raise

    def increment_sessions(self, user_id: int):
        """Increment session count for a user."""
        try:
            conn = self.db.connect()
            cur = conn.cursor()
            cur.execute("UPDATE users SET sessions_completed = sessions_completed + 1 WHERE id = ?", (user_id,))
            conn.commit()
            print(f"[DEBUG] Incremented sessions for user_id={user_id}", flush=True)
        except Exception as e:
            print(f"[ERROR] increment_sessions failed: {e}", flush=True)
            raise

    def get_user(self, user_id: int):
        conn = self.db.connect()
        cur = conn.cursor()
        cur.execute("SELECT id, name, sound_file, sessions_completed FROM users WHERE id = ?", (user_id,))
        row = cur.fetchone()
        if row:
            return {"id": row[0],  # this is user_id
                "name": row[1], "sound_file": row[2], "sessions_completed": row[3],}
        return None


    def get_all_users(self):
        """Get all users (with sound_file + sessions)."""
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, sound_file, sessions_completed FROM users")
        return cursor.fetchall()
