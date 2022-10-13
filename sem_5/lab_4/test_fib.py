from main import fib, FibonachiList


def test_fib():
    assert fib(1) == [0, 1], "Тривиальный случай n = 1, список [0, 1]"
    assert fib(2) == [0, 1, 1]
    assert fib(5) == [0, 1, 1, 2, 3, 5]


def fib(n):
    myiter = iter(FibonachiList())

    while (myiter.lst[-1] + myiter.lst[-2] <= n):
        next(myiter)
    return myiter.lst

if __name__ == "__main__":
    n = int(input())

    print(fib(n))
