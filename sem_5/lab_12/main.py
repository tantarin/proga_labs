

api_key = '995f52d4b29cb1829a7f4490519144d8'


def getweather(api_key=None):
    import requests

    if api_key:
        result = dict()
        base_url = "https://api.openweathermap.org/data/2.5/forecast?"
        city = "Moscow"
        cnt = "39"
        complete_url = base_url + "appid=" + api_key + "&q=" + city + "&cnt=" + cnt + "&units=metric"
        print(complete_url)
        req = requests.get(complete_url)
        data = req.json()
        if data['cod'] == '200':
            for item in data['list']:
                date_splitted = str(item['dt_txt']).split()[0].split('-')
                date = date_splitted[2] + '.' + date_splitted[1]
                time = str(item['dt_txt']).split()[1][:5]
                if time == '00:00' or time == '06:00':
                    r = '\n'.join([date, time])
                    result[r] = item['main']['temp']
            print(result)
        return result


def visualise_data(dict_data=None):
    if dict_data:
        import matplotlib.pyplot as plt
        dates = dict_data.keys()
        temps = dict_data.values()
        plt.scatter(dates, temps)
        plt.title("Прогноз температуры на 5 дней")
        plt.show()


weather_data = getweather(api_key)
visualise_data(weather_data)
