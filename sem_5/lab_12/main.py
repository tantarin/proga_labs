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


def get_average_weather(api_key=None):
    import requests
    import statistics

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
                result[date] = result.get(date, list())
                result[date].append(int(item['main']['temp']))
        for key, value in result.items():
            result[key] = statistics.mean(value)  # = 20.11111111111111
        return result


def visualise_data(data_with_times=None, average_temp=None):
    if data_with_times and average_temp:
        import matplotlib.pyplot as plt
        dates_times = data_with_times.keys()
        temps = data_with_times.values()
        plt.subplot(121)
        plt.scatter(dates_times, temps)
        plt.xticks(range(len(dates_times)), dates_times, rotation='vertical')
        plt.title("Прогноз температуры на 5 дней")
        plt.xlabel("Дата и время")
        plt.ylabel("Градус Цельсия")
        plt.grid()
        dates = average_temp.keys()
        temps = average_temp.values()
        plt.subplot(122)
        plt.scatter(dates, temps)
        plt.title("Прогноз средней температуры на 5 дней")
        plt.xlabel("Дата")
        plt.ylabel("Градус Цельсия")
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.grid()
        plt.show()


weather_data = getweather(api_key)
average = get_average_weather(api_key)
visualise_data(weather_data, average)
