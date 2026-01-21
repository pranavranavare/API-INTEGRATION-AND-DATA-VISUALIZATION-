import requests
import pandas as pd
import matplotlib.pyplot as plt

# --- API Data Fetching ---
API_KEY = "1f94951d1429cb783caed99fa0a067a3"
CITY = "Mumbai"

url = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

# --- Data Processing ---
# Extract required data
weather_data = []

for item in data["list"]:
    weather_data.append({
        "datetime": item["dt_txt"],
        "temperature": item["main"]["temp"],
        "humidity": item["main"]["humidity"],
        "pressure": item["main"]["pressure"]
    })

df = pd.DataFrame(weather_data)
df["datetime"] = pd.to_datetime(df["datetime"])
print(df.head())
# Extract date from datetime for daily aggregation
df['date'] = df['datetime'].dt.date

# Calculate average humidity per day
daily_avg_humidity = df.groupby('date')['humidity'].mean().reset_index()

# --- Humidity Visualization ---
plt.figure(figsize=(12, 6))
plt.bar(daily_avg_humidity['date'], daily_avg_humidity['humidity'], color='skyblue')
plt.xlabel('Date')
plt.ylabel('Average Humidity (%)')
plt.title('Average Daily Humidity in Mumbai')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- Temperature Visualization ---
plt.figure(figsize=(12, 6))
plt.plot(df['datetime'], df['temperature'])
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time in Mumbai')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()