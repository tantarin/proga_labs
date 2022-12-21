from sem_5.lab_12.main import weather_data_json


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


        pplt.show()

        # построенный график необходимо оптимизировать:
        #  - добавить название
        #  - правильно расположить ось абсцисс
        #  - упростить вывод дат (на этом графике они выводятся в формате unixtime)
        #  - вывести более строгие значения для подписей осей абсцисс и ординат
        #  (xticks, yticks)
        # - добавить на график температуры остальных дат
        # - добавить второй график со средними значениями

visualise_data(weather_data_json)
