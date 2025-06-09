import os
from dotenv import load_dotenv
from threads_scraper.scraper import ThreadsScraper

load_dotenv()

INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")
DRIVER_PATH = "/usr/local/bin/chromedriver"
KEYWORDS = ["交友軟體", "交友軟體看法", "交友軟體比較", "dating app", "tinder", "bumble", "soga app", "coffee meet bagel", "workheart", "boo dating app"]

# Initialize the scraper
scraper = ThreadsScraper(
    username=INSTAGRAM_USERNAME,
    password=INSTAGRAM_PASSWORD,
    driver_path=DRIVER_PATH
)

# Start the scraper
scraper.get_driver()

if scraper.login_to_threads():
    data = scraper.scrape(KEYWORDS, 10)
    scraper.save_to_csv(data, "data/threads_post.csv", True)

scraper.close()
