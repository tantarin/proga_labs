

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
        if data['cod'] == '200':
            for item in data['list']:
                date = str(item['dt_txt']).split()[0]
                result[date] = item['main']['temp']
            print(result)
        return result


def visualise_data(dict_data=None):
    if dict_data:
        import matplotlib.pyplot as plt
        dates = dict_data.keys()
        temps = dict_data.values()
        plt.scatter(dates, temps)
        plt.show()


weather_data = getweather(api_key)
visualise_data(weather_data)
