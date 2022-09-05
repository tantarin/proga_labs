import configparser
import logging

PARAMS = {
        'precision': None,
        'output_type': None,
        'possible_types': None,
        'dest': None
}

def print_results(*args):
    """
    Вывод в табличном виде результатов вычислений

    Функция принимает переменное число значений, которые нужно вывести в табличном виде.
    последний аргумент в упакованном кортеже - результат вычислений,
    предпоследний - действие, которое выполнилось,остальные — аргументы, с которыми это действие выполнилось.
    """
    operands = args[:len(args)]
    result = args[-1]
    action = args[-2]

    print('inp_args in pretty mode', operands, action, result)

def load_params(path="lab_5/params.ini"):
    config = configparser.ConfigParser()
    config.read(path)
    global PARAMS
    PARAMS['precision'] = config.get("Settings", "precision")
    PARAMS['output_type'] = config.get("Settings", "output_type")
    PARAMS['possible_types'] = config.get("Settings", "possible_types")
    PARAMS['dest'] = config.get("Settings", "dest")
    print(PARAMS)


load_params()

def write_log(action=None, result=None, file='history.txt'):
    logging.basicConfig(filename=file, level=logging.INFO)
    logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                                  "%Y-%m-%d %H:%M:%S")
    logging.info("Informational message")
