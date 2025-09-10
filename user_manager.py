import sqlite3

class User:
    def __init__(self, email, password_hash, salt):   
        self.email = email
        self.password_hash = password_hash
        self.salt = salt

class UserManager:
    def __init__(self, db_name='password_manager.sqlite'):
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("PRAGMA foreign_keys = ON;") 
        self.cur = self.conn.cursor()

        # Create table in sql to store user profiles.
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                salt BlOB NOT NULL,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    # Expects a user object containing email, password hash and salt. Adds user to database
    def add_user(self, user):
        self.cur.execute(
            "INSERT INTO users (email, password_hash, salt) VALUES (?, ?, ?)",
            (user.email, user.password_hash, user.salt,)
        )
        self.conn.commit()
    
    def delete_user(self, user_id):
        self.cur.execute(
            "DELETE FROM users WHERE user_id = ?",
            (user_id,)
        )
        self.conn.commit()
    
    # Gets user by email and returns there details as a dict. Returns none if no user found
    def get_user_by_email(self, email):
        self.cur.execute(
            "SELECT user_id, email, password_hash, salt FROM users WHERE email = ?",
            (email,))
        row = self.cur.fetchone()
        if row:
            user_id, email, password_hash, salt = row
            return {"user_id": user_id, "email": email, "password_hash": password_hash, "salt": salt}
        return None
    
    def close(self):
        self.conn.close()

    


          

