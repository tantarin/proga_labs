import requests
from bs4 import BeautifulSoup


class Bank:
    def __init__(self):
        self.result = []

    def get_currencies(self, currencies_ids_lst: list) -> list:
        cur_res_str = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        soup = BeautifulSoup(cur_res_str.content, 'xml')
        # print(soup.prettify())

        valutes = soup.find_all('Valute')
        for _v in valutes:
            valute_id = _v.get('ID')
            valute = {}
            if str(valute_id) in currencies_ids_lst:
                valute_cur_name, valute_cur_val = _v.find('Name').text, _v.find('Value').text
                valute_charcode = _v.find('CharCode').text
                valute[valute_charcode] = (valute_cur_name, valute_cur_val)
                self.result.append(valute)

        return self.result


bank = Bank()
res = bank.get_currencies(['R01035', 'R01335', 'R01700J'])
print(res)
