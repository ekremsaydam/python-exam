"""Weather Bot."""
import requests


def weather_bot(city_name: str, regional: str = ""):
    """City."""
    api_key = ""
    # url = "http://api.openweathermap.org/geo/1.0/direct?q=\
    # {city_name},{state_code},{country code}&limit={limit}&appid={api_key}"
    url = (
        "http://api.openweathermap.org/data/2.5/weather?q="
        + (city_name if not regional else city_name + "," + regional)
        + "&APPID="
        + api_key
    )

    response = requests.get(url, timeout=10)
    weather_data = response.json()
    # print(weather_data)
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]
    return {
        "city_name": city_name.split(",")[0],
        "temperature": round(temperature - 272.15, 0),
        "humidity": humidity,
        "description": description,
    }

    #     f"{city_name}\n"
    #     + f"sicaklik {round(temperature-272.15,0)}C\n"
    #     + f"NEM:{humidity}\n"
    #     + f"aciklama:{description}"
    # )


print(weather_bot(city_name="Antalya", regional="tr"))
