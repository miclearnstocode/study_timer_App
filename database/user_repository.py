from database.connection import DatabaseConnection

class UserRepository:
    def __init__(self, db: DatabaseConnection):
        self.db = db

    def add_user(self, name):
        try:
            conn = self.db.connect()
            cur = conn.cursor()
            cur.execute("INSERT INTO users (name) VALUES (?)", (name,))
            conn.commit()
            user_id = cur.lastrowid
            print(f"[DEBUG] Inserted user: {name} with id={user_id}", flush=True)
            return user_id
        except Exception as e:
            print(f"[ERROR] add_user failed: {e}", flush=True)
            raise
    

    def get_user(self, user_id: int):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()

    def get_all_users(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM users")
        return cursor.fetchall()
