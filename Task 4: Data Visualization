import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("/content/clean_weather.csv")

# Line chart: Temperature vs Time
plt.figure()
plt.plot(df['hour'], df['temperature_C'], marker='o')

plt.title("Temperature Variation Throughout the Day")
plt.xlabel("Hour of Day")
plt.ylabel("Temperature (°C)")

plt.grid()
plt.tight_layout()

plt.show()
