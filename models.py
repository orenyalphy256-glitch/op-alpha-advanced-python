# models.py
# Import necessary modules
import sqlite3
from datetime import datetime

# Database file path
DB_PATH = None

# Initialize the database and create table if not exists
def init_db(path):
    global DB_PATH
    DB_PATH = path
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        created_at TEXT
    )
    """)
    conn.commit()
    conn.close()

# Contact class to represent a contact entry
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.created_at = datetime.utcnow().isoformat() + "Z"

# ContactBook class to manage contacts in the database
class ContactBook:
    def __init__(self, db_path):
        init_db(db_path)

# Method to add a contact to the database
    def add(self, contact: Contact):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("INSERT INTO contacts (name,phone,created_at) VALUES (?,?,?)",
                  (contact.name, contact.phone, contact.created_at))
        conn.commit()
        conn.close()

# Method to list all contacts from the database
    def list_all(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT id, name, phone, created_at FROM contacts ORDER BY id DESC")
        rows = c.fetchall()
        conn.close()
        return rows

# Method to save a contact to the database if new
    def save_contact_if_new(conn, name, phone):
        c = conn.cursor()
        c.execute("SELECT 1 FROM contacts WHERE phone = ? LIMIT 1", (phone))
        if c.fetchone():
            return False
        c.execute("INSERT INTO contacts (name, phone, created_at) VALUES (?, ?,datetime('now'))", (name, phone))
        conn.commit()
        return True