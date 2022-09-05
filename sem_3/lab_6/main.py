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
