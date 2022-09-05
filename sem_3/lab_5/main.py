import configparser
import logging
import math
from tabulate import tabulate

PARAMS = {
    'precision': None,
    'output_type': None,
    'possible_types': None,
    'dest': None
}


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
    print_results(op1, op2, act, r)
    write_log(op1, op2, act, r)
    return r


def print_results(*args):
    """
    Вывод в табличном виде результатов вычислений

    Функция принимает переменное число значений, которые нужно вывести в табличном виде.
    последний аргумент в упакованном кортеже - результат вычислений,
    предпоследний - действие, которое выполнилось,остальные — аргументы, с которыми это действие выполнилось.
    """
    l = list()
    numbers = list(args[:len(args)-2])
    result = args[-1]
    action = args[-2]
    l.append(numbers)
    l.append(action)
    l.append(result)
    print(tabulate([l], headers=['Arguments', 'Action', 'Result'], tablefmt='orgtbl'))



def load_params(path="lab_5/params.ini"):
    config = configparser.ConfigParser()
    config.read(path)
    global PARAMS
    PARAMS['precision'] = config.get("Settings", "precision")
    PARAMS['output_type'] = config.get("Settings", "output_type")
    PARAMS['possible_types'] = config.get("Settings", "possible_types")
    PARAMS['dest'] = config.get("Settings", "dest")
    print(PARAMS)


def write_log(*args, file='history.txt'):
    numbers = list(args[:len(args) - 2])
    numbers_str = ', '.join(str(n) for n in numbers)
    result = args[-1]
    action = args[-2]
    logging.basicConfig(filename=file, level=logging.INFO)
    logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                      "%Y-%m-%d %H:%M:%S")
    logging.info(numbers_str + action + str(result))


load_params()
calculate(2, 3, '+')

