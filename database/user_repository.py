from database.connection import DatabaseConnection

class UserRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def add_user(self, name: str, sound_file: str = None):
        """Insert a new user with optional sound file preference."""
        try:
            conn = self.db.connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO users (name, sound_file) VALUES (?, ?)", (name, sound_file))
            conn.commit()
            user_id = cur.lastrowid
            print(f"[DEBUG] Inserted user: {name}, sound_file={sound_file}, id={user_id}", flush=True)
            return user_id
        except Exception as e:
            print(f"[ERROR] add_user failed: {e}", flush=True)
            raise

    def get_user(self, user_id: int):
        """Get a single user (with sound_file)."""
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, sound_file FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()

    def get_all_users(self):
        """Get all users (with sound_file)."""
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, sound_file FROM users")
        return cursor.fetchall()
