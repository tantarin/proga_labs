# import required modules
import requests, json

# Enter your API key here
api_key = '995f52d4b29cb1829a7f4490519144d8'


def getweather(api_key=None):
    import requests

    if api_key:
        result = dict()

        base_url = "https://api.openweathermap.org/data/2.5/forecast?"
        city = "Moscow"
        cnt = "70"
        complete_url = base_url + "appid=" + api_key + "&q=" + city + "&cnt=" + cnt
        print(complete_url)
        req = requests.get(complete_url)
        data = req.json()
   #     print(json.dumps(data, sort_keys=True, indent=4))
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

def visualise_data(json_data=''):

    if json_data:
        import matplotlib.pyplot as pplt
        import pandas
        # Мы можем загрузить данные в пригодный для дальнейшей обработки формат
        # с помощью метода read_json из pandas.
        data = pandas.read_json(json_data)
        # print(data)
        city_name = data['city']

        # получим отдельные столбцы с датами
        dates = [_d['dt'] for _d in data['temps'][:]]
        # и тепературами
        temps = [_t['temp'] for _t in data['temps'][:]]

        # построим их на диаграмме рассеяния
        pplt.scatter(dates, temps)


weather_data_json = getweather(api_key)
