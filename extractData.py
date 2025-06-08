import requests
import pandas as pd
from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NASA_API_KEY")

def fetch_asteroid_data(start_date, end_date):
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except:
        return None

def parse_data(data):
    asteroids = []
    for date in data['near_earth_objects']:
        for obj in data['near_earth_objects'][date]:
            try:
                asteroids.append({
                    'name': obj['name'],
                    'approach_date': date,
                    'diameter_km': round(obj['estimated_diameter']['kilometers']['estimated_diameter_max'], 3),
                    'velocity_kmph': round(float(obj['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']), 2),
                    'distance_km': round(float(obj['close_approach_data'][0]['miss_distance']['kilometers']), 2),
                    'is_hazardous': obj['is_potentially_hazardous_asteroid']
                })
            except:
                continue
    return asteroids

# Loop over past 90 days in 7-day chunks
all_asteroids = []
days_back = 90
for i in range(0, days_back, 7):
    start = datetime.today() - timedelta(days=i+7)
    end = datetime.today() - timedelta(days=i)
    data = fetch_asteroid_data(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'))
    if data:
        all_asteroids += parse_data(data)
    time.sleep(1)  # Be kind to the API

# Save to CSV
df = pd.DataFrame(all_asteroids)
df.to_csv("asteroid_data.csv", index=False)
print(f"✅ Saved {len(df)} records to asteroid_data.csv")
