# Op Alpha ― Contact Manager (Batch 3 / Advanced Python)

A small, testable CLI and data-pipeline project demonstrating:
- Package architecture and editable installation (`pip install -e .`)
- Web scraping with `requests` + BeautifulSoup
- Persistence to SQLite database with idempotent inserts
- A simple CLI for adding/listing/looking up contacts
- Unit tests for validators and core logic
- A scheduler example (APScheduler) to automate periodic jobs

## Project Structure

contact_manager/
├── init.py
├── cli.py # CLI entrypoint (add/list/lookup)
├── helpers.py # CSV/DB I/O utilities
├── validators.py # Phone/email validator functions
├── scraper_simple.py # fetch() + parse_contacts() + scrape_and_save()
├── models.py # DB schema & init_db logic
├── db_utils.py # SQLite helper functions
├── scrape_to_db.py # Integration: fetch → parse → save pipeline
├── scraper_scheduler.py # APScheduler example run script
├── tests/ tests for core modules
├── requirements.txt
└── setup.py /packaging config