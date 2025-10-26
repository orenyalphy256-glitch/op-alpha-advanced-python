# cli.py

# Import necessary modules
import argparse
from models import Contact, ContactBook, DB_PATH
from helpers import CSV_PATH, write_contact
from db_utils import get_connection

def main():
    parser = argparse.ArgumentParser(prog="contact_manager")
    sub = parser.add_subparsers(dest="cmd")

    p_add = sub.add_parser("add")
    p_add.add_argument("--name", required=True)
    p_add.add_argument("--phone", required=True)

    p_list = sub.add_parser("list")

    p_find = sub.add_parser("find")
    p_find.add_argument("--name", required=True)

    args = parser.parse_args()
    if args.cmd == "add":
        c = Contact(args.name, args.phone)
        book = ContactBook(DB_PATH or "contacts_batch3.db")
        book.add(c)
        print("Added")
    elif args.cmd == "list":
        book = ContactBook(DB_PATH or "contacts_batch3.db")
        rows = book.list_all()
        for r in rows:
            print(r)
    elif args.cmd == "find":
        conn = get_connection(DB_PATH or "contacts_batch3.db")
        rows = conn.execute("SELECT id, name, phone FROM contacts WHERE name LIKE ?", (f"%{args.name}%",)).fetchall()
        for r in rows:
            print(dict(r))

if __name__ == "__main__":
    main()