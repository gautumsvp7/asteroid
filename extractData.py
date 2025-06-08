import requests
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

API_KEY = os.getenv("NASA_API_KEY")

# Define date range — you can loop over several days
start_date = datetime.today() - timedelta(days=7)
end_date = datetime.today()

# Format as yyyy-mm-dd
start_str = start_date.strftime('%Y-%m-%d')
end_str = end_date.strftime('%Y-%m-%d')

# API endpoint
url = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_str}&end_date={end_str}&api_key={API_KEY}'

# Make request
response = requests.get(url)
data = response.json()

# Extract asteroid details
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

# Convert to DataFrame
df = pd.DataFrame(asteroids)
print(df.head())
df.to_csv('asteroid_data.csv', index=False)
print("Data saved as asteroid_data.csv ✅")
