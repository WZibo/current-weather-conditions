import requests


def fetch_weather(location):
    api_key = "——————"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Fetching weather data based on location
    if location.isdigit():
        query_param = f"zip={location}"
    else:
        query_param = f"q={location}"

    complete_url = f"{base_url}{query_param}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        # Extracting required weather information
        weather_data = {
            "Temperature": data["main"]["temp"],
            "Feels Like": data["main"]["feels_like"],
            "Description": data["weather"][0]["description"]
        }
        return weather_data
    else:
        return None


def display_weather(weather_data):
    if weather_data:
        print("Current Weather Conditions:")
        for key, value in weather_data.items():
            print(f"{key}: {value}")
    else:
        print("City/zip code not found. Please try again.")


if __name__ == "__main__":
    location = input("Enter city name or zip code: ")
    weather_data = fetch_weather(location)
    display_weather(weather_data)
