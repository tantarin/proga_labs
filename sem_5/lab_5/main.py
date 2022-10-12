import requests
from xml.etree import ElementTree as ET


class Bank:
    def __init__(self):
        self.result = {
            'usd': 0,
            'eur': 0,
        }

    def get_currencies(self, day, month, year):
        """
        Выполняет запрос к API Банка России.

        :param day: Выбранный день.
        :param month: Выбранный номер месяца.
        :param year: Выбранный год
        :return: dict
        """

        if int(day) < 10:
            day = '0%s' % day

        if int(month) < 10:
            month = '0%s' % month

        try:
            # Выполняем запрос к API.
            get_xml = requests.get(
                'http://www.cbr.ru/scripts/XML_daily.asp?date_req=%s/%s/%s' % (day, month, year)
            )

            # Парсинг XML используя ElementTree
            structure = ET.fromstring(get_xml.content)
        except:
            return self.result

        try:
            # Поиск курса доллара (USD ID: R01235)
            dollar = structure.find("./*[@ID='R01235']/Value")
            self.result['dollar'] = dollar.text.replace(',', '.')
        except:
            self.result['dollar'] = 'x'

        try:
            # Поиск курса евро (EUR ID: R01239)
            euro = structure.find("./*[@ID='R01239']/Value")
            self.result['euro'] = euro.text.replace(',', '.')
        except:
            self.result['euro'] = 'x'

        return self.result


bank = Bank()
res = bank.get_currencies(9, 10, 2022)
print(res)
