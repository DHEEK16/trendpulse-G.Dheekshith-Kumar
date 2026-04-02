import pandas as pd

# Load raw data
df = pd.read_csv("/content/raw_weather.csv")

# Convert data types
df['temperature_C'] = df['temperature_C'].astype(int)
df['humidity'] = df['humidity'].astype(int)
df['wind_speed_kmph'] = df['wind_speed_kmph'].astype(int)

# Convert time (proper hour format)
df['time'] = df['time'].astype(int)
df['hour'] = df['time'] // 100

# Clean text
df['weather_desc'] = df['weather_desc'].str.strip().str.lower()

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv("clean_weather.csv", index=False)

print("Cleaned Data:")
print(df.head())
