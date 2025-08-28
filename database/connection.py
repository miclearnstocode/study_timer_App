import sqlite3
import os

class DatabaseConnection:
    def __init__(self, db_name="study_timer.db"):
        self.db_name = db_name

    def connect(self):
        """Always return a new database connection (thread-safe)."""
        return sqlite3.connect(self.db_name, check_same_thread=False)

    def initialize(self):
        """Create required tables if they don’t exist."""
        conn = self.connect()
        cursor = conn.cursor()

        # Users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                sound_file TEXT,
                sessions_completed INTEGER DEFAULT 0
            )
        """)

        # Sessions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                duration INTEGER,
                completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)

        conn.commit()
        conn.close()

    def close(self, conn):
        """Close a given database connection."""
        if conn:
            conn.close()
