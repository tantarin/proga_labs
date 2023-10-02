from typing import List
from mathstats import MathStats
import pandas as pd
from matplotlib import pyplot as plt

FILE = 'Retail.csv'
FILE2 = 'MarketingSpend.csv'


def main():
  data = read_data(FILE)
  c = count_invoice(data)
  print(f'Всего инвойсов (invoices): {c}')  # 16522

  data2 = MathStats(FILE2)
  slice_test2 = data2.data[::]
  print(len(slice_test2))
  print(count_different_values(data, 'InvoiceNo'))

  print(data2.get_mean(slice_test2))

  print(
    f'Общее количество проданного товара для stock_code 21422: {get_total_quantity(data, 21422)}'
  )

  print(
    f'Число различных значений для InvoiceNo: {count_different_values(data, "InvoiceNo")}'
  )

  print(data2.min, data2.max) #320.25 5000.0
  slice_test1 = data2.data[:2]
  # среднее значение
  print(data2.get_mean(slice_test1))  # (4500.0, 2952.43)
  # дисперсия
  print(data2.disp)  # (904376.35, 652456.945)
  print(data2.numpy_disp)
  # среднее квадратичное отклонение
  print(data2.sigma_sq) #{'offline': 950.99, 'online': 807.75}
  print(data2.numpy_sigma_sq)


def read_data(file: str) -> List[dict]:
  import csv
  data = []
  with open(file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for _r in reader:
      row = _r
      data.append(row)
  return data


def count_invoice(data: List[dict]) -> int:
  invoices = [_el['InvoiceNo'] for _el in data]
  unique_invoices = set(invoices)
  count = len(unique_invoices)
  return count


def count_different_values(data: List[dict], key: str) -> int:
  """
    Функция должна возвращать число различных значений для столбца key в списке data

    key - InvoiceNo или InvoiceDate или StockCode
    """
  unique_values = set(_el[key] for _el in data)
  return len(unique_values)


def get_total_quantity(data: List[dict], stock_code: int) -> int:
  """
    Возвращает общее количество проданного товара для данного stock_code
    """
  total_quantity = 0
  for item in data:
    if int(item['StockCode']) == stock_code:
      total_quantity += int(item['Quantity'])
  return total_quantity


def load_data(file_path):
  data = pd.read_csv(file_path,
                     header=None,
                     names=['Date', 'Offline Spend', 'Online Spend'],
                     skiprows=1)
  return data


def group_data_by_month(data):
  print(data)
  data['Date'] = pd.to_datetime(data['Date'])
  data['Month'] = data['Date'].dt.month
  monthly_summary = data.groupby('Month')[['Offline Spend',
                                           'Online Spend']].sum()
  print(monthly_summary)
  return monthly_summary


def plot_marketing_graph(grouped_data):
  months = [
    'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август',
    'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
  ]
  offline_spend = grouped_data['Offline Spend']
  online_spend = grouped_data['Online Spend']

  fig, ax = plt.subplots(figsize=(12, 10))

  bars1 = ax.barh(months, offline_spend, label='Offline Spend', alpha=0.6)
  bars2 = ax.barh(months, online_spend, label='Online Spend', alpha=0.6)

  ax.bar_label(bars1)
  ax.bar_label(bars2)

  plt.xlabel('Сумма расходов')
  plt.title('Расходы по месяцам')
  plt.legend(loc='best')

  plt.show()


def retail_graph():
  data = pd.read_csv('Retail.csv')
  data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
  daily_sum = data.groupby(data['InvoiceDate'].dt.dayofyear)['Quantity'].sum()

  fig, ax = plt.subplots(figsize=(12, 10))
  ax.scatter(daily_sum.index, daily_sum.values)
  ax.set_xlabel('Дни в году')
  ax.set_ylabel('Количество в день')
  plt.show()


if __name__ == "__main__":
  main()
  # data = load_data('MarketingSpend.csv')
  # grouped_data = group_data_by_month(data)
  # plot_marketing_graph(grouped_data)
  # retail_graph()