key = "b11b7be7ea161d31db5ba95ebb0b158e"


def getweather(api_key=None):
    import json
    import requests
    city, lat, lon = "Saint Petersburg, RU", 59.57, 30.19

    dt = 1671047690  # datetime of Wed Dec 14 2022 19:54:50 GMT+0000 in unix-like format
    # Для определения unixtime диапазона для получения температур, 
    # можно использовать сервис https://unixtime-converter.com/

    if api_key:
        result = dict()
        req = requests.get(
            f'http://api.openweathermap.org/data/2.5/'
            f'onecall/timemachine?lat={lat}&lon={lon}&dt={dt}&'
            f'appid={api_key}&lang=ru&units=metric')

        # для других параметров см. https://openweathermap.org/api/one-call-api#history

        req_obj = json.loads(req.text)  # Преобразуем объект типа Request в json-формат
        print(req_obj)
        # Сохраним результаты температур в формате json, чтобы ниже их визуализировать
        result['city'] = city
        measures = [{"dt": str(measure['dt']), "temp": str(measure['temp'])} for measure in req_obj["hourly"]]

        result['temps'] = measures
        return json.dumps(result)


weather_data_json = getweather(key)
