import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def get_hr_odds(date=None):
    options = Options()
    options.binary_location = "/usr/bin/chromium-browser"
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)

    url = "https://sportsbook.fanduel.com/navigation/mlb?tab=home-run-props"
    driver.get(url)
    time.sleep(10)

    odds_data = []
    try:
        players = driver.find_elements(By.CLASS_NAME, "event-cell__name-text")
        odds = driver.find_elements(By.CLASS_NAME, "sportsbook-outcome-cell__line")

        for p, o in zip(players, odds):
            if p.text and o.text:
                odds_data.append({"Player": p.text.strip(), "HR Odds": o.text.strip()})
    finally:
        driver.quit()

    return pd.DataFrame(odds_data)
