# scrape_to_db.py

# Import the necessary modules
from scraper_simple import fetch, parse_contacts
import models
from db_utils import get_connection
import time
import os

def scrape_to_db(url, db_path):
    html = fetch(url)
    items = parse_contacts(html)
    db_dir = os.path.dirname(db_path) or "."
    if db_dir and not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)
    
    conn = get_connection(db_path)
    ensure_table(conn)

    if hasattr(models, "init_db"):
        models.init_db(db_path)

    added = 0
    for name, phone in items:
        if models.save_contact_if_new(conn, name, phone):
            added += 1
            time.sleep(1)
            conn.close()
            return added
        
    if __name__ == "__main__":
        import sys
        if len(sys.argv) < 3:
            print("Usage: python scrape_to_db.py <url> <db_path>")
            sys.exit(1)
        url = sys.argv[1]
        db_path = sys.argv[2]
        print(scrape_to_db(url, db_path))