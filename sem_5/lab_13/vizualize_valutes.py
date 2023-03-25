from datetime import datetime
from urllib.request import urlopen
from xml.etree import ElementTree as ET

import matplotlib.pyplot as plt

plt.rcdefaults()

'''
<Valute ID="R01035">
<NumCode>826</NumCode>
<CharCode>GBP</CharCode>
<Nominal>1</Nominal>
<Name>Фунт стерлингов Соединенного королевства</Name>
<Value>43,8254</Value>
</Valute>
'''
def get_currencies(currencies_ids_lst=None):
    if currencies_ids_lst is None:
        currencies_ids_lst = ['R01239', 'R01235', 'R01035']

    cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")

    result = {}

    valutes = ET.parse(cur_res_str).getroot().findall('Valute')
    for el in valutes:
        valute_id = el.get('ID')
        if str(valute_id) in currencies_ids_lst:
            valute_charcode = el.find('CharCode').text
            valute_cur_val = el.find('Value').text
            result[valute_charcode] = valute_cur_val
    return result


ten_valutes = ['R01010', 'R01035', 'R01060', 'R01100', 'R01115', 'R01135', 'R01200', 'R01215', 'R01235', 'R01239']
cur_vals_dict = get_currencies(ten_valutes)  # {'AUD': '51,1207', 'GBP': '94,1532'}


# TODO 0 Вывести на графике 10 валют (получить по кодам валюты из ЦБС)
def chart_ten_valutes(vals):
    x = vals.keys()
    # TODO #1 переписать лямбда-функцию из следующей строки через list comprehension
    y = [float(v.replace(",", ".")) for v in vals.values()]
    # TODO #2 Подписи должны быть у осей (x, y), у графика, у «рисок» (тиков),
    #  столбцы должны быть разных цветов с легендой
    col_map = plt.get_cmap('Paired')
    plt.bar(x, y, color=col_map.colors)
    plt.title('График 10 валют')
    plt.xlabel('Наименования валют')
    plt.ylabel('Значения валют')
    return plt


# chart_ten_valutes(cur_vals_dict).show()


# TODO #3 Нарисовать отдельный график с колебанием одной (выбранной вами) валюты (получить данные с сайта ЦБ за год)
#  и отобразить его наиболее оптимальным образом (типом графика)
def get_currency_year_dynamic(currency_id=''):
    cur_res_str = urlopen(
        f"http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=27/12/2021&date_req2=27/12/2022&VAL_NM_RQ={currency_id}")

    result = {}

    cur_res_xml = ET.parse(cur_res_str)

    root = cur_res_xml.getroot()
    records = root.findall('Record')
    for el in records:
        date = el.get('Date')
        valute_val = float(el.find('Value').text.replace(',', '.'))
        result[date] = valute_val

    return result


val_year_dict = get_currency_year_dynamic('R01035')


def chart_year_valute(val_year):
    days = [datetime.strptime(s, '%d.%m.%Y').date() for s in val_year.keys()]
    values = val_year.values()
    plt.plot(days, values)
    plt.title('Фунт стерлингов Соединенного королевства')
    plt.xlabel('Период')
    plt.ylabel('Значения валюты')
    return plt


# chart_year_valute(val_year_dict).show()


# # TODO #4 Отобразить это на одном изображении (2 графика)
def two_charts(vals, val_year):
    fig, axs = plt.subplots(2, 1, constrained_layout=True)
    fig.set_size_inches(15, 8)

    x = vals.keys()
    y = [float(v.replace(",", ".")) for v in vals.values()]
    col_map = plt.get_cmap('Paired')
    axs[0].bar(x, y, color=col_map.colors)
    axs[0].set_title('График 10 валют')
    axs[0].set_xlabel('Наименования валют')
    axs[0].set_ylabel('Значения валют')

    days = [datetime.strptime(s, '%d.%m.%Y').date() for s in val_year.keys()]
    values = val_year.values()
    axs[1].plot(days, values)
    axs[1].set_title('Фунт стерлингов Соединенного королевства')
    axs[1].set_xlabel('Период')
    axs[1].set_ylabel('Значения валюты')

    plt.show()


two_charts(cur_vals_dict, val_year_dict)
