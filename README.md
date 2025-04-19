# ⚾ MLB Home Run Projection App

This Streamlit app predicts MLB home run probabilities daily using AI and real-time data (including sportsbook odds).

## 🔧 Setup Instructions

1. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Make sure you have Chrome + Chromedriver installed.

3. Run the app locally:
    ```
    streamlit run main.py
    ```

For Streamlit Cloud:
- Make sure `packages.txt` is included in the root directory
- Upload the model file to `/models/hr_model.pkl`

## 📁 Folder Structure

```
mlb_hr_project/
├── main.py
├── mlb_hr_model.py
├── mlb_data.py
├── requirements.txt
├── packages.txt
├── README.md
├── models/
│   └── hr_model.pkl        ← Dummy model included
├── scraper/
│   ├── player_stats.py
│   ├── odds_scraper_selenium.py
│   ├── weather.py          ← Placeholder
│   ├── ballpark_factors.py← Placeholder
│   └── pitcher_scraper.py ← Placeholder
```