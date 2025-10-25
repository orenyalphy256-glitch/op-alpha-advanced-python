# scraper_simple.py
# Import necessary modules
import requests
import time
from helpers import CSV_PATH, write_contact
from bs4 import BeautifulSoup

# Define headers for HTTP requests
HEADERS = {"User-Agent": "AgentALO-Scraper/1.0 (contact: your-email@example.com)"}

# Function to fetch HTML content from a URL
def fetch(url):
    r = requests.get(url, headers=HEADERS, timeout=8)
    r.raise_for_status()
    return r.text

# Function to parse HTML and extract contact information
def parse_contacts(html):
    soup = BeautifulSoup(html, "html.parser")
    results = []
    for div in soup.select(".contact"):
        elem = div.select_one(".name")
        name = elem.get_text(strip=True) if elem else "Unknown"
        phone_elem = div.select_one(".phone")
        phone = phone_elem.get_text(strip=True) if phone_elem else ""
        results.append((name, phone))
    return results

# Main function to scrape and save contacts
def scrape_and_save(url):
    html = fetch(url)
    items = parse_contacts(html)
    for name, phone in items:
        write_contact(name, phone) # Append to CSV
        time.sleep(1) # Be polite with a delay