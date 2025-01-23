import requests
import pandas as pd
import matplotlib.pyplot as plt
import json

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(api_key, city_ids):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    weather_data = []
    for city_id in city_ids:
        response = requests.get(base_url, params={"id": city_id, "appid": api_key, "units": "metric"})
        if response.status_code == 200:
            data = response.json()
            weather_data.append({
                "City": data["name"],
                "Temperature (°C)": data["main"]["temp"],
                "Humidity (%)": data["main"]["humidity"]
            })
        else:
            print(f"Failed to fetch data for city ID {city_id}: {response.status_code}")
    return weather_data

# Sorting function
def sort_weather_data(data, key, ascending=True):
    return sorted(data, key=lambda x: x[key], reverse=not ascending)

# Visualization function
def visualize_weather_data(data, key):
    df = pd.DataFrame(data)
    df.sort_values(by=key, ascending=True, inplace=True)
    df.plot.bar(x="City", y=key, color="skyblue", legend=False)
    plt.title(f"{key} by City")
    plt.ylabel(key)
    plt.xlabel("City")
    plt.tight_layout()
    plt.show()

# Main function
def main():
    # Replace with your OpenWeatherMap API key
    with open('config.json', 'r') as file:
        config = json.load(file)
        api_key = config.get('api_key')

    print(f"Your API key is: {api_key}")
    
    # Example city IDs (you can add more or replace with your own)
    city_ids = [5128581, 2643743, 2988507, 1850147, 2147714]  # New York, London, Paris, Tokyo, Sydney

    # Fetch weather data
    weather_data = fetch_weather_data(api_key, city_ids)

    if not weather_data:
        print("No weather data available.")
        return

    # Display unsorted data
    print("Unsorted Weather Data:")
    for item in weather_data:
        print(item)

    # Sort by temperature
    sorted_data = sort_weather_data(weather_data, key="Temperature (°C)", ascending=True)

    # Display sorted data
    print("\nSorted Weather Data (by Temperature):")
    for item in sorted_data:
        print(item)

    # Visualize the sorted data
    visualize_weather_data(sorted_data, key="Temperature (°C)")

if __name__ == "__main__":
    main()
