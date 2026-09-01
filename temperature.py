import os
import requests


def get_weather(api_key, city):
    url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp_celsius = data["main"]["temp"]
        return temp_celsius

    print(
        f"Error getting data for {city}. "
        f"Status code: {response.status_code}"
    )
    return None


def main():

    api_key = os.environ.get("OPENWEATHER_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENWEATHER_API_KEY environment variable is not configured"
        )

    cities = ["New York", "Madrid", "Paris"]

    for city in cities:
        temp = get_weather(api_key, city)

        if temp is not None:
            print(f"La temperatura en {city} is {temp}°C")


if __name__ == "__main__":
    main()