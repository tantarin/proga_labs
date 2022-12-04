"""
Использование декоратора
"""
import csv
import json
import os

import requests
from bs4 import BeautifulSoup


class BaseCurrenciesList():
    def get_currencies(self, currencies_ids_lst: list) -> dict:
        pass


class CurrenciesList(BaseCurrenciesList):
    """
        aka ConcreteComponent
    """

    def __init__(self):
        self.all_valutes = dict()
        cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        soup = BeautifulSoup(cur_res_str.content, 'xml')
        self.valutes = soup.find_all('Valute')
        for _v in self.valutes:
            id = _v['ID']
            valute_cur_name, valute_cur_val = _v.find('Name').text, _v.find('Value').text
            valute_charcode = _v.find('CharCode').text
            self.all_valutes[id] = (valute_charcode, valute_cur_name, float(valute_cur_val.replace(',', '.')))

    def get_currencies(self, currencies_ids_lst: list) -> dict:
        # result = {
        #     'R01090B': ('29,4282', 'Белорусский рубль'),
        #     'R01565': ('17,7405', 'Польский злотый'),
        #     'R01720': ('27,5078', 'Украинских гривен')
        # }
        if not currencies_ids_lst:
            return self.all_valutes
        result = dict()
        for r in currencies_ids_lst:
            result[r] = (self.all_valutes.get(r)[2], self.all_valutes.get(r)[1])

        return result


class Decorator(BaseCurrenciesList):
    """
    aka Decorator из примера паттерна
    """

    __wrapped_object: BaseCurrenciesList = None

    def __init__(self, currencies_lst: BaseCurrenciesList):
        self.__wrapped_object = currencies_lst

    @property
    def wrapped_object(self) -> str:
        return self.__wrapped_object

    def get_currencies(self, currencies_ids_lst: list) -> dict:
        return self.__wrapped_object.get_currencies(currencies_ids_lst)


class ConcreteDecoratorJSON(Decorator):

    def create_currencies(self, currencies_ids_lst: list) -> str:
        with open('result/result.json', 'w', encoding='utf-8') as file:
            json.dump(self.wrapped_object.get_currencies(currencies_ids_lst),
                      file,
                      indent=4,
                      ensure_ascii=False)

    def get_currencies(self, currencies_ids_lst: list) -> str:  # JSON

        return f"ConcreteDecoratorJSON({self.wrapped_object.get_currencies(currencies_ids_lst)})"

    def __str__(self, currencies_ids_lst: list) -> str:
        return f"ConcreteDecoratorJSON({self.wrapped_object.get_currencies(currencies_ids_lst)})"

    def __repr__(self):
        return f"{self.__class__}"


class ConcreteDecoratorCSV(Decorator):

    def create_currencies(self, currencies_ids_lst: list) -> str:
        with open('result/result.csv', 'w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Цена', 'Название'])

        result_list = []
        for index, tuple in self.wrapped_object.get_currencies(
                currencies_ids_lst).items():
            result_list.append([index, tuple[0], tuple[1]])

        for item in result_list:
            with open('result/result.csv', 'a', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerows([item])

    def get_currencies(self, currencies_ids_lst: list) -> str:  # CSV

        return f"ConcreteDecoratorCSV({self.wrapped_object.get_currencies(currencies_ids_lst)})"

    def __str__(self, currencies_ids_lst: list) -> str:
        return f"ConcreteDecoratorCSV({self.wrapped_object.get_currencies(currencies_ids_lst)})"

    def __repr__(self):
        return f"{self.__class__}"


def show_currencies(currencies: BaseCurrenciesList):
    """
       aka client_code()
    """

    print(currencies.get_currencies(['R01010', 'R01500', 'R01585F']))


if __name__ == '__main__':
    # Таким образом, клиентский код может поддерживать как простые компоненты...
    # simple = ConcreteComponent()
    # print("Client: I've got a simple component:")
    # client_code(simple)
    # print("\n")

    if not os.path.exists('result'):
        os.mkdir('result')

    curlistdict = CurrenciesList()  # base
    print("Client: I've got a simple component:")

    print("\n")
    show_currencies(curlistdict)

    print("\n")
    wrappedcurlist = Decorator(curlistdict)
    wrappedcurlist_json = ConcreteDecoratorJSON(wrappedcurlist)
    print(wrappedcurlist_json.get_currencies(['R01010', 'R01500', 'R01585F']))
    wrappedcurlist_json.create_currencies(['R01010', 'R01500', 'R01585F'])

    print("\n")
    wrappedcurlist_csv = ConcreteDecoratorCSV(wrappedcurlist)
    print(wrappedcurlist_csv.get_currencies(['R01010', 'R01500', 'R01585F']))
    wrappedcurlist_csv.create_currencies(['R01010', 'R01500', 'R01585F'])

    print("\n")
    print('Данные в JSON:')
    show_currencies(wrappedcurlist_json)

    print("\n")
    print('Данные в CSV:')
    show_currencies(wrappedcurlist_csv)
