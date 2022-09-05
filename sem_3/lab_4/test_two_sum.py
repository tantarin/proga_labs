from two_sum import two_sum


def test_two_sum_base():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 8
    assert two_sum(lst, target) == (0, 6)


test_two_sum_base()