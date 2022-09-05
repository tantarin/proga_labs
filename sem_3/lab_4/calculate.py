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
