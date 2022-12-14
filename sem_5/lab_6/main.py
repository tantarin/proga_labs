import functools

import requests
from bs4 import BeautifulSoup


def singleton(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance

    wrapper.instance = None
    return wrapper


@singleton
class CurrenciesList:
    def __init__(self, lst):
        self.all_valutes = dict()
        cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        soup = BeautifulSoup(cur_res_str.content, 'xml')
        self.valutes = soup.find_all('Valute')
        for _v in self.valutes:
            id = _v['ID']
            valute_cur_name, valute_cur_val = _v.find('Name').text, _v.find('Value').text
            valute_charcode = _v.find('CharCode').text
            self.all_valutes[id] = (valute_charcode, valute_cur_name, float(valute_cur_val.replace(',', '.')))
        self.get_currencies_list(lst)

    def get_currencies(self) -> dict:
        return self.all_valutes

    def get_currencies_list(self, lst):
        res = []
        for r in lst:
            res.append(self.all_valutes.get(r))
        return res

    def set_valute(self, id, valute_charcode, valute_cur_name, valute_cur_val):
        self.all_valutes[id] = (valute_charcode, valute_cur_name, float(valute_cur_val.replace(',', '.')))

    def get_valute(self, id):
        return {id, self.all_valutes.get(id, None)}

    def get_name(self, id):
        valute = self.all_valutes[id]
        return valute[1]


c1 = CurrenciesList(["R01090B", "R01720", "R01565"])
c2 = CurrenciesList(["R01090B", "R01720", "R01565"])
print(id(c1))
print(id(c2))

