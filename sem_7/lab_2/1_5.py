# Напишите программу для реализации многопоточного алгоритма быстрой сортировки.

import threading

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def threaded_quicksort(arr, depth=0):
    if len(arr) <= 1:
        return arr

    if depth > 2:
        return quicksort(arr)

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    left_thread = threading.Thread(target=threaded_quicksort, args=(left, depth + 1))
    right_thread = threading.Thread(target=threaded_quicksort, args=(right, depth + 1))

    left_thread.start()
    right_thread.start()

    left_thread.join()
    right_thread.join()

    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = threaded_quicksort(my_list)
    print("Original List:", my_list)
    print("Sorted List:", sorted_list)

