import timeit
import matplotlib.pyplot as plt

from lab_2.bin_tree_non_recursive import gen_bin_tree_non_recursive
from lab_2.bin_tree_recursive import gen_bin_tree_recursive


def setup_data() -> list:
    root = 5
    min_height = 2
    max_height = 9
    data = list()
    for h in range(min_height, max_height + 1):
        data.append((h, root))
    return data


def timer_func(func, h, r):
    start_time = timeit.default_timer()
    func(h, r)
    return timeit.default_timer() - start_time


def main():
    res_recursive = []
    res_non_recusive = []
    data = setup_data()
    for h, r in data:
        time_non_recursive = timer_func(gen_bin_tree_non_recursive, h, r)
        time_recursive = timer_func(gen_bin_tree_recursive, h, r)
        res_non_recusive.append(time_non_recursive)
        res_recursive.append(time_recursive)
    plt.title('Comparison of recursive and non-recursive methods')
    plt.xlabel("Height of tree")
    plt.ylabel("Time")
    plt.plot(res_recursive)
    plt.plot(res_non_recusive)
    plt.legend(['recursive', 'non recursive'])
    plt.grid()
    plt.show()


main()
