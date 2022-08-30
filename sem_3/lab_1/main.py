import math


def test_sum():
    assert calculate(1, 2,
                     "+") == 3, "Сумма должна быть равна числу 3 типа int"


def test_mod():
    assert calculate(19, 8,
                     "mod") == 3


def test_lcm():
    assert calculate(330, 75,
                     "lcm") == 1650


def test_type_of_result_sum():
    assert type(calculate(1, 2,
                          "+")) is int, "Сумма должна быть равна числу 3 типа int"


def main():
    operand1 = float(input("Введите 1 число: "))
    operand2 = float(input("Введите 2 число: "))
    action = input("Введите действие: ")
    res = calculate(operand1, operand2, action)
    print("Результат вычисления: ", res)


def calculate(op1, op2, act):
    if act == "+":
        r = op1 + op2
    elif act == "-":
        r = op1 - op2
    elif act == "*":
        r = op1 * op2
    elif act == "/":
        if op2 != 0:
            r = op1 / op2
        else:
            r = "деление на ноль невозможно"
    elif act == "^":
        if op2 % 1 == 0:
            r = op1 ** op2
        else:
            r = "возведение в вещественную степень невозможно"
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


test_sum()
test_type_of_result_sum()
test_mod()
test_lcm()


