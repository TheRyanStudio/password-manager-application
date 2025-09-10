import sqlite3

class DBManager:
    def __init__(self, db_name='password_manager.sqlite'):
        self.conn = sqlite3.connect(db_name)
        self.conn.execute("PRAGMA foreign_keys = ON;") 
        self.cur = self.conn.cursor() 

        # Create table in sql to store user password entries. Foreign key associates it with the correct user
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS entries (
                entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                organization TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(user_id) ON DELETE CASCADE
            )
        """)
        self.conn.commit()
 
    def create_entry(self, entry: dict):
        self.cur.execute(
            "INSERT INTO entries (user_id, organization, username, password) VALUES (?, ?, ?, ?)",
            (
                entry["user_id"],  
                entry["organization"],
                entry["username"],
                entry["password"],
            )
        )
        self.conn.commit()
        print("Entry inserted")
    
    def update_entry(self, entry_id, organization= None, username= None, password= None):
        fields = []
        values = []

        # checks each of the variables for a value, if nothing no fields are updated
        if organization:
            fields.append("organization = ?")
            values.append(organization)
        if username:
            fields.append("username = ?")
            values.append(username)
        if password:
            fields.append("password = ?")
            values.append(password)

        if not fields:
            print("No fields to update.")
            return

        values.append(entry_id)
        sql = f"UPDATE entries SET {', '.join(fields)} WHERE id = ?"
        self.cur.execute(sql, values)
        self.conn.commit()

    def delete_entry(self, entry_id):
        # Deletes from entry database based on the entry id 
        self.cur.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
        self.conn.commit()

    # Gets all entries of that user and returns in a list of dicts
    def get_entries(self, user_id) -> dict | None:
        self.cur.execute(
            "SELECT organization, username, password FROM entries WHERE user_id = ?",
            (user_id,)
        )
        rows = self.cur.fetchall()

        if rows is None:
            return None

        entries = []
        for organization, username, password in rows:
            entries.append({
                "organization": organization,
                "username": username,
                "password": password,
            })

        return entries
            
    # Gets a single entry and returns as a dict
    def get_entry(self, entry_id) -> dict | None:
        self.cur.execute("SELECT organization, username, password FROM entries WHERE id = ?", (entry_id,))
        row = self.cur.fetchone()
        if row is None:
            return None

        organization, username, password = row
        return {
            "organization": organization,
            "username": username,
            "password": password,
        }

            