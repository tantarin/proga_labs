import matplotlib.pyplot as plt

plt.rcdefaults()
import matplotlib.pyplot as plt

from urllib.request import urlopen
from xml.etree import ElementTree as ET


def get_currencies(currencies_ids_lst=None):
    if currencies_ids_lst is None:
        currencies_ids_lst = ['R01239', 'R01235', 'R01035']
    cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")

    result = {}

    cur_res_xml = ET.parse(cur_res_str)
    root = cur_res_xml.getroot()
    valutes = root.findall('Valute')
    for el in valutes:
        valute_id = el.get('ID')
        if str(valute_id) in currencies_ids_lst:
            valute_charcode = el.find('CharCode').text
            valute_cur_val = el.find('Value').text
            result[valute_charcode] = valute_cur_val
    return result


ten_valutes = ['R01010', 'R01035', 'R01060', 'R01100', 'R01115', 'R01135', 'R01200', 'R01215', 'R01235', 'R01239']
cur_vals_dict = get_currencies(ten_valutes)
print(cur_vals_dict.values())

y_pos = cur_vals_dict.keys()
x_pos = [float(value.replace(",", ".")) for value in cur_vals_dict.values()]

# TODO #2

#  Подписи должны быть у осей (x, y), у графика, у «рисок» (тиков),
# столбцы должны быть разных цветов с легендой
plt.xlabel("char codes")
plt.ylabel("values of valutes")


# TODO #3
# Нарисовать отдельный график с колебанием одной (выбранной вами) валюты
# (получить данные с сайта ЦБ за год) и отобразить его наиболее
# оптимальным образом (типом графика)

# TODO #4
col_map = plt.get_cmap('Paired')
# Отобразить это на одном изображении (2 графика)
plt.bar(y_pos, x_pos, color=col_map.colors)
# plt.xticks(y_pos, objects)
plt.title('Valutes')

plt.show()
