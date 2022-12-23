# import required modules
import requests, json

# Enter your API key here
api_key = '995f52d4b29cb1829a7f4490519144d8'


def getweather(api_key=None):
    import requests

    if api_key:
        result = dict()

        base_url = "http://api.openweathermap.org/data/2.5/forecast/daily?"
        lat = "10.99"
        lon = "44.34"
        cnt = "5"
        complete_url = base_url + "lat" + lat + "&lon" + lon + "&appid=" + api_key + "&q=" + "&cnt=" + cnt
        req = requests.get(complete_url)
        data = req.json()
        print(json.dumps(data, sort_keys=True, indent=4))
        if data['cod'] == '200':
            for item in data['list']:
                 date = str(item['dt_txt']).split()[0]
                 result[date] = item['main']['temp']
            print(result)


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
