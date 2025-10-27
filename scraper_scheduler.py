# scraper_scheduler.py

# Import necessary modules
from apscheduler.schedulers.blocking import BlockingScheduler
from scraper_simple import scrape_and_save

sched = BlockingScheduler()
sched.add_job(scrape_and_save, 'interval', minutes=2, args=["https://localhost/testpage.html"])
print("Scheduler started. Scraping every 2 minutes.")
sched.start()