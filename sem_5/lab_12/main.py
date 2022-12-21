# import required modules
import requests, json

# Enter your API key here
api_key = '995f52d4b29cb1829a7f4490519144d8'



def getweather(api_key=None):
    import json
    import requests
    city, lat, lon = "Saint Petersburg, RU", 59.57, 30.19

    dt = 1671047690  # datetime of Wed Dec 14 2022 19:54:50 GMT+0000 in unix-like format
    # Для определения unixtime диапазона для получения температур,
    # можно использовать сервис https://unixtime-converter.com/

    if api_key:
        result = dict()

        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = "Berlin"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        print(complete_url)
        response = requests.get(complete_url)
        x = response.json()
        print(x)

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
