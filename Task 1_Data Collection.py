!pip3 install requests  

import requests

url = "https://wttr.in/india"

response = requests.get(url, params = {"format": "j1"})
print(response)


response.json()

import requests
import pandas as pd

# API URL
url = "https://wttr.in/india"

# Fetch data
response = requests.get(url, params={"format": "j1"})
data = response.json()

# Extract location info
area = data['nearest_area'][0]
area_name = area['areaName'][0]['value']
region = area['region'][0]['value']
country = area['country'][0]['value']

# Extract hourly weather data (today)
hourly_data = data['weather'][0]['hourly']

weather_list = []

for hour in hourly_data:
    record = {
        "area": area_name,
        "region": region,
        "country": country,
        "date": data['weather'][0]['date'],
        "time": hour['time'],
        "temperature_C": hour['tempC'],
        "humidity": hour['humidity'],
        "weather_desc": hour['weatherDesc'][0]['value'],
        "wind_speed_kmph": hour['windspeedKmph']
    }
    weather_list.append(record)

# Convert to DataFrame
df = pd.DataFrame(weather_list)

# Save raw data
df.to_csv("raw_weather.csv", index=False)

print("Raw Data Collected Successfully!")
print(df.head())




df.head()
