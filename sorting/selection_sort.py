import math
from util.util import custom_print


def swap(array: list, x_pos: int, y_pos: int):
    temp = array[x_pos]
    array[x_pos] = array[y_pos]
    array[y_pos] = temp


def selection_sort(array: list):
    smallest: int
    swap_index = 0
    arr_len = len(array)

    for i in range(arr_len):
        smallest = math.inf

        for j in range(i, arr_len):
            if array[j] < smallest:
                smallest = array[j]
                swap_index = j

        custom_print(array, array[:i + 1], [smallest])
        print(smallest, ' is smallest, swap with ', array[i])
        swap(array, swap_index, i)


def run(array: list):
    print('Array before sorting: ', array)
    selection_sort(array)
    print('Array after sorting: ', array)
