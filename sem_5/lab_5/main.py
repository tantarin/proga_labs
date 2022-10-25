import requests
from bs4 import BeautifulSoup


class Bank:
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

    def __del__(self):
        print('Object destroyed')

    def get_all_currencies(self) -> dict:
        return self.all_valutes

    def get_currencies(self, lst) -> dict:
        d = dict()
        for r in lst:
            d[r] = (self.all_valutes.get(r)[2], self.all_valutes.get(r)[1])
        return d

    def set_valute(self, id, valute_charcode, valute_cur_name, valute_cur_val):
        self.all_valutes[id] = (valute_charcode, valute_cur_name, float(valute_cur_val.replace(',', '.')))

    def get_valute(self, id):
        return {id, self.all_valutes.get(id, None)}

    def get_name(self, id):
        valute = self.all_valutes[id]
        return valute[1]


b = Bank()
res = b.get_currencies(['R01035', 'R01335', 'R01700J'])
print(res)


