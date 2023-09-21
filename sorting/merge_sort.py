import math
from colorama import Fore
from util.util import colored_array_print


def __merge(parent_array: list, left_array: list, right_array: list, iter_pass: int):
    i = 0

    while (len(left_array) > 0 and len(right_array) > 0):
        if left_array[0] <= right_array[0]:
            parent_array[i] = left_array[0]
            del left_array[0]
        else:
            parent_array[i] = right_array[0]
            del right_array[0]

        i += 1

    while (len(left_array) > 0):
        parent_array[i] = left_array[0]
        del left_array[0]
        i += 1

    while (len(right_array) > 0):
        parent_array[i] = right_array[0]
        del right_array[0]
        i += 1

    print('\nMerging back sorted sub arrays...')
    colored_array_print(parent_array, Fore.BLUE)
    print(' FROM PASS ', iter_pass)


def __merge_sort(array: list, iter_pass: int):
    arr_len = len(array)
    iter_pass += 1

    if arr_len <= 1:
        return
    
    middle = math.floor(arr_len / 2)
    left_array = array[0: middle]
    right_array = array[middle::]

    print('\nDivide array into two sub arrays...')
    colored_array_print(left_array, Fore.GREEN)
    print(' and ', end="")
    colored_array_print(right_array, Fore.RED)
    print()

    __merge_sort(left_array, iter_pass)
    __merge_sort(right_array, iter_pass)

    __merge(array, left_array, right_array, iter_pass)


def run(array: list):
    iter_pass = 0

    print('Array before sorting: ', array)
    print()
    __merge_sort(array, iter_pass)
    print()
    print('Array after sorting: ', array)
