from colorama import Fore
from python.util.util import custom_print, colored_array_print


def comb_sort(array: list):
    gap = len(array)
    shrink_factor = 1.3
    sorted = False
    iterations = 0

    while not sorted:
        iterations += 1
        gap = int(gap / shrink_factor)

        if gap <= 1:
            gap = 1
            sorted = True

            print()
            colored_array_print("USING BUBBLE SORT", Fore.GREEN, False)
        
        print(f'\nPass {iterations}, Gap: {gap}')

        i = 0
        while i + gap < len(array):
            custom_print(array, [array[i]], [array[i + gap]])

            if array[i] > array[i + gap]:
                print(f'{array[i]} > {array[i + gap]}, swapping')
                array[i], array[i + gap] = array[i + gap], array[i]
                sorted = False
            else:
                print(f'{array[i]} < {array[i + gap]}, no swap needed')

            i += 1

    print('\nARRAY IS NOW SORTED')

def run(array: list):
    print('Array before sorting: ', array)
    comb_sort(array)
    print('Array after sorting: ', array)
