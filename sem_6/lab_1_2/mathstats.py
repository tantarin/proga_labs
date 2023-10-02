"""
Для вычисления дисперсии и ср. квадр. отклонения использовать
https://myslide.ru/documents_3/b9d7b50c38e81a4b8b7645742d3b22c7/img10.jpg
"""
import math

import numpy as np


class MathStats():
    def __init__(self, file):
        import csv

        self._file = file
        self._data = []
        self._mean = None
        self._max = float('-Inf')
        self._min = float('Inf')
        with open(self._file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for _r in reader:
                row = {
                    'Date': _r[''],
                    'Offline': float(_r['Offline Spend']),
                    'Online': float(_r['Online Spend']),
                }
                self._data.append(row)

    @property
    def data(self):
        return self._data

    def get_mean(self, data):
        """
        Вычисление средних значений по оффлайн и онлайн тратам
        """
        sums = {'offline': 0, 'online': 0}
        for _l in data:
            sums['offline'] += _l['Offline']
            sums['online'] += _l['Online']

        self._mean = (sums['offline'] / len(data), sums['online'] / len(data))
        return self._mean

    @property
    def max(self):
        if self._max == float('-Inf'):
            for row in self._data:
                offline_spend = row['Offline']
                online_spend = row['Online']
                if offline_spend > self._max:
                    self._max = offline_spend
                if online_spend > self._max:
                    self._max = online_spend
        return self._max

    @property
    def min(self):
        if self._min == float('Inf'):
            for row in self._data:
                offline_spend = row['Offline']
                online_spend = row['Online']
                if offline_spend < self._min:
                    self._min = offline_spend
                if online_spend < self._min:
                    self._min = online_spend
        return self._min

    # Дисперсия — это величина, показывающая, как именно и насколько сильно разбросаны значения
    @property
    def disp(self):
        mean_offline, mean_online = self.get_mean(self.data)
        variance_offline = sum((row['Offline'] - mean_offline) ** 2 for row in self.data) / len(self.data)
        variance_online = sum((row['Online'] - mean_online) ** 2 for row in self.data) / len(self.data)
        return (variance_offline, variance_online)

    # среднее квадратичное отклонение
    @property
    def sigma_sq(self):
        variance_offline, variance_online = self.disp
        sigma_offline = round(math.sqrt(variance_offline), 2)
        sigma_online = round(math.sqrt(variance_online), 2)
        return {'offline': sigma_offline, 'online': sigma_online}

    @property
    def numpy_disp(self):
        offline_values = [row['Offline'] for row in self.data]
        online_values = [row['Online'] for row in self.data]

        variance_offline = np.var(offline_values)
        variance_online = np.var(online_values)

        return variance_offline, variance_online

    @property
    def numpy_sigma_sq(self):
        variance_offline, variance_online = self.numpy_disp

        sigma_offline = np.sqrt(variance_offline)
        sigma_online = np.sqrt(variance_online)

        return sigma_offline, sigma_online

