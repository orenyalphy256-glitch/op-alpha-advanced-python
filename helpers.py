# helpers.py
# Import necessary modules
import os
import csv

# Define the directory and file path for storing CSV
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "03-Data")
os.makedirs(DATA_DIR, exist_ok=True)
CSV_PATH = os.path.join(DATA_DIR, "contacts_batch3.csv")

# Function to write a contact to the CSV file
def write_contact(name: str, phone: str) -> None:
    with open(CSV_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone])