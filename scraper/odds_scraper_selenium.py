
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

def get_hr_odds(date=None):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)

    url = "https://sportsbook.fanduel.com/navigation/mlb?tab=home-run-props"  # Example, may need updating
    driver.get(url)
    time.sleep(10)  # wait for JS to load

    odds_data = []
    try:
        player_elements = driver.find_elements(By.CLASS_NAME, "event-cell__name-text")
        odds_elements = driver.find_elements(By.CLASS_NAME, "sportsbook-outcome-cell__line")

        for name_elem, odd_elem in zip(player_elements, odds_elements):
            player_name = name_elem.text.strip()
            hr_odds = odd_elem.text.strip()
            if player_name and hr_odds.startswith("+"):
                odds_data.append({
                    "Player": player_name,
                    "HR Odds": hr_odds
                })
    finally:
        driver.quit()

    return pd.DataFrame(odds_data)
