from itertools import islice


# Задание 1
def fib(n):
    """
    Список чисел ряда Фибоначчи
    Возвращает значения не превосходящие данное n
    Например:
    n = 1, lst = [0, 1, 1]
    n = 2, lst = [0, 1, 1, 2]
    n = 5, [0, 1, 1, 2, 3, 5]
    """
    l = []
    a = 0
    b = 1
    while a <= n:
        l.append(a)
        a, b = b, a + b
    return l


# Задание 2
class FibonachiList:
    def __init__(self, instance=None):
        self.instance = instance
        self.lst = [0, 0, 1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.instance is None:
            raise StopIteration
        nextFib = self.lst[-1] + self.lst[-2]
        self.lst[-3] = self.lst[-2]
        self.lst[-2] = self.lst[-1]
        self.lst[-1] = nextFib
        if self.lst[-3] > self.instance[-1]:
            raise StopIteration
        if self.lst[-3] in self.instance:
            return self.lst[-3]


# Задание 3
def fib_iter(it):
    lst = []
    a, b = 0, 1
    for _ in range(len(it)):
        if a in it:
            lst.append(a)
        a, b = b, a + b
    return islice(lst, len(lst))


# Задание 4
# функция-генератор
def my_genn(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

