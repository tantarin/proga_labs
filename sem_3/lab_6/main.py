from prettytable import PrettyTable


def print_results(*inp_args):
    """
    Вывод в табличном виде результатов вычислений

    Функция принимает переменное число значений, которые нужно вывести в табличном виде.
    последний аргумент в упакованном кортеже - результат вычислений,
    предпоследний - действие, которое выполнилось,остальные — аргументы, с которыми это действие выполнилось.
    """
    operands = [str(x) for x in inp_args[:len(inp_args) - 2]]
    result = inp_args[-1]
    action = inp_args[-2]
    alph = list()
    for i in range(65, 65 + len(operands)):
        alph.append(chr(i))
    t = PrettyTable([action.join(alph), 'Результат'])
    t.add_row([action.join(operands), result])
    print(t)


# +-------------+-----------+
# |    A+B+C    | Результат |
# +-------------+-----------+
# | 100+200+200 |    500    |
# +-------------+-----------+

print_results(100, 200, 200, '+', 500)
