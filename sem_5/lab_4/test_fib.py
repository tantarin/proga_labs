from main import fib, FibonachiList, fib_iter, my_genn


def test_zadanie_1():
    assert fib(1) == [0, 1, 1], "Тривиальный случай n = 1, список [0, 1]"
    assert fib(2) == [0, 1, 1, 2]
    assert fib(5) == [0, 1, 1, 2, 3, 5]
    assert fib(7) == [0, 1, 1, 2, 3, 5]


def test_zadanie_2():
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    test_lst = list()
    for f in FibonachiList(lst):
        test_lst.append(f)
    assert test_lst == [0, 1, 1, 2, 3, 5, 8]


def test_zadanie_3():
    assert list(fib_iter(range(14))) == [0, 1, 1, 2, 3, 5, 8, 13]


def test_zadanie_4():
    test_lst = list()
    for f in my_genn(7):
        test_lst.append(f)
    assert test_lst == [0, 1, 1, 2, 3, 5, 8]


if __name__ == "__main__":
    test_zadanie_1()
    test_zadanie_2()
    test_zadanie_3()
    test_zadanie_4()
