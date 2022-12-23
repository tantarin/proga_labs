# import required modules
import requests, json

# Enter your API key here
api_key = '995f52d4b29cb1829a7f4490519144d8'


def getweather(api_key=None):
    import requests

    if api_key:
        result = dict()

        base_url = "http://api.openweathermap.org/data/2.5/forecast?"
        city_name = "Berlin"
        type = "day"
        cnt = "5"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&type=" + type + "&cnt=" + cnt
        print(complete_url)
        response = requests.get(complete_url)
        x = response.json()
        print(json.dumps(x, sort_keys=True, indent=4))

        #
        # req_obj = json.loads(req.text)  # Преобразуем объект типа Request в json-формат
        # print(req_obj)
        # # Сохраним результаты температур в формате json, чтобы ниже их визуализировать
        # result['city'] = city
        # print(req_obj)
        # measures = [{"dt": str(measure['dt']), "temp": str(measure['temp'])} for measure in req_obj["hourly"]]
        #
        # result['temps'] = measures
        # return json.dumps(result)


weather_data_json = getweather(api_key)
