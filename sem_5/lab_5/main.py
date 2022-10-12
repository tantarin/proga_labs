import requests
from bs4 import BeautifulSoup


class Bank:
    def __init__(self):
        self.all_valutes = []
        cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        soup = BeautifulSoup(cur_res_str.content, 'xml')
        self.valutes = soup.find_all('Valute')
        for _v in self.valutes:
            valute = {}
            valute_cur_name, valute_cur_val = _v.find('Name').text, _v.find('Value').text
            valute_charcode = _v.find('CharCode').text
            valute[valute_charcode] = (valute_cur_name, valute_cur_val)
            self.all_valutes.append(valute)
        self.valutes = soup.find_all('Valute')

    def __del__(self):
         print('Object destroyed')

    def get_currencies(self) -> list:
        return self.all_valutes

    def set_valute(self, valute_charcode, valute_cur_name, valute_cur_val):
        valute = {valute_charcode: (valute_cur_name, valute_cur_val)}
        self.all_valutes.append(valute)

    def get_valute(self, valute_charcode):
        for v in self.all_valutes:
            if list(v.keys())[0] == valute_charcode:
                return v[valute_charcode]


bank = Bank()
res = bank.get_currencies()
for r in res:
    print(r)
print(bank.get_valute('AUD'))
