import math


def convert_precision(precision=0.01):
    if isinstance(precision, float):
        l = len(str(precision))
        for i in range(1, l+1):
            if precision * 10 ** i >= 1:
                return i


# среднеквадратичное отклонение
def std(*args, **kwargs):
    xV = 0
    n = 0
    Sigma = 0.0
    for x in args:
        xV += x
        n += 1
    xV = xV / n
    for x in args:
        Sigma += (x - xV) ** 2
    res = math.sqrt(Sigma / n)
    p = kwargs['precision']
    if p:
        ndigits = convert_precision(p)
        res = round(res, ndigits)
    return res


settings = {'precision': 0.00001}


def test_cp_with_1():
    assert convert_precision(0.1) == 1, "Должна быть 1"


def test_cp_with_2():
    assert convert_precision(0.01) == 2, "Должно быть 2"


def test_cp_with_5():
    assert convert_precision(0.00001) == 5, "Должно быть 5"


test_cp_with_1()
test_cp_with_2()
test_cp_with_5()


def sum(op1, op2):
    """Возвращает сумму двух чисел"""
    return op1 + op2


def subtract(op1, op2):
    """Вычитает одно число из другого"""
    return op1 - op2


def mult(op1, op2):
    """Перемножает два числа"""
    return op1 * op2


def divide(op1, op2):
    """Делит одно число на другое"""
    if op2 != 0:
        r = op1 / op2
    else:
        r = "деление на ноль невозможно"
    return r

def pow(op1, op2):
    """Возводит число в степень"""
    if op2 % 1 == 0:
        r = op1 ** op2
    else:
        r = "возведение в вещественную степень невозможно"
    return r


def gcd(op1, op2):
    """Наибольший общий делитель"""
    if type(op1) is int and type(op2) is int:
        r = math.gcd(op2, op2)
    else:
        r = None
    return r


def lcm(op1, op2):
    """Наименьшее общее кратное"""
    if type(op1) is int and type(op2) is int:
        r = math.lcm(op1, op2)
    else:
        r = None
    return r


def mod(op1, op2):
    """Возвращает остаток от деления"""
    return op1 % op2


def calculate(op1, op2, act):
    if act == "+":
        r = sum(op1, op2)
    elif act == "-":
        r = subtract(op1, op2)
    elif act == "*":
        r = op1 * op2
    elif act == "/":
        r = divide(op1, op2)
    elif act == "^":
        r = pow(op1, op2)
    elif act == "gcd":
        if type(op1) is int and type(op2) is int:
            r = math.gcd(op2, op2)
        else:
            pass
    elif act == "lcm":
        if type(op1) is int and type(op2) is int:
            r = math.lcm(op1, op2)
        else:
            pass
    elif act == "mod":
        r = op1 % op2
    else:
        r = "операция не распознана"
    return r


print(std(*[1, 2, 3, 4, 5, 6], **settings))
