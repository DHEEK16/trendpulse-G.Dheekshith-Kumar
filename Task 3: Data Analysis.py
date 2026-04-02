import pandas as pd

# Load cleaned data
df = pd.read_csv("/content/clean_weather.csv")

# Basic statistics
avg_temp = df['temperature_C'].mean()
max_temp = df['temperature_C'].max()
min_temp = df['temperature_C'].min()

avg_humidity = df['humidity'].mean()

# Most common weather condition
common_weather = df['weather_desc'].value_counts().idxmax()

print("Weather Analysis Report")
print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Maximum Temperature: {max_temp} °C")
print(f"Minimum Temperature: {min_temp} °C")
print(f"Average Humidity: {avg_humidity:.2f} %")
print(f"Most Common Weather: {common_weather}")
