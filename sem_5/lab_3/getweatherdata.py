import json

import requests


def get_weather_data(city_name, api_key=None):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    data = response.json()
    result = {}

    if data["cod"] != "404":
        result["name"] = data["name"]
        result["coord"] = data["coord"]
        result["country"] = data["sys"]["country"]
        result["feels_like"] = data["main"]["feels_like"]
        hours = int(data["timezone"]) // 3600
        result["timezone"] = f"UTC+{hours}"
    print(result)
    return json.dumps(result)


if __name__ == '__main__':
    owm_api_key = "your own api key"
    get_weather_data('Chicago', api_key=owm_api_key)
    get_weather_data('Saint Petersburg', api_key=owm_api_key)
    get_weather_data('Dhaka', api_key=owm_api_key)
