import math
from colorama import Fore
from util.util import custom_print, colored_array_print


def shell_sort(array: list):
    arr_len = len(array)
    gap = math.floor(arr_len / 2)
    iter_pass = 0

    while gap > 0:
        iter_pass += 1
        print('PASS ', iter_pass)

        for i in range(gap, arr_len):
            temp = array[i]
            temp_array = []
            j = i

            while j >= gap and array[j - gap] > temp:
                custom_print(array, [temp], [array[j - gap]])
                print()
                array[j] = array[j - gap]
                j -= gap

            array[j] = temp

        colored_array_print(array, Fore.BLUE)
        print('\n')

        gap = math.floor(gap / 2)


def run(array: list):
    print('Array before sorting: ', array)
    shell_sort(array)
    print('Array after sorting: ', array)
