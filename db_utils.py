# db_utils.py
# Import necessary libraries
import sqlite3

# Function to get a database connection
def get_connection(path):
    """Establish a connection to the SQLite database."""
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn

# Function to find a contact by name
def find_by_name(conn, name):
    """Find a contact by name."""
    c = conn.cursor()
    c.execute("SELECT id, name, phone, created_at FROM contacts WHERE name LIKE ? ORDER BY id DESC", (f"%{name}%",))
    return c.fetchall()

