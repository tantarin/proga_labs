import itertools
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
    l = [0]
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
        l.append(a)
    return l


# Задание 2
class FibonachiList:
    def __init__(self, instance=None):
        if instance is None:
            instance = [0, 1]
        self.instance = instance

    def __iter__(self):
        self.lst = [0, 1]
        return self

    def __next__(self):
        fib_el = self.lst[-1] + self.lst[-2]
        if fib_el > self.instance[-1]:
            raise StopIteration
        if fib_el in self.instance:
            self.lst.append(fib_el)
            return fib_el


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
def my_genn(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print(list(fib_iter(range(14))))
    # f = FibonachiList(list(range(10)))
    # for i in f:
    #     print(i)
