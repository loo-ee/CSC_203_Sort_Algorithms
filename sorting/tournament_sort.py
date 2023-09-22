import math
from colorama import Fore
from util.util import custom_print, colored_array_print


def __tournament_sort(original_array: list, sorted_array: list):
    array = original_array[:]
    original_arr_size = len(array)
    temp_array = []
    is_eliminating = True
    iterations = 0

    while len(sorted_array) != original_arr_size:
        iterations += 1
        is_eliminating = True
        array = original_array[:]

        print()
        colored_array_print("PASS " + str(iterations), Fore.YELLOW, False)    
        print()
        
        while is_eliminating:
            temp_array_size = len(array)

            custom_print(array, [], [-math.inf])
            print()

            if temp_array_size == 1:
                is_eliminating = False

            if temp_array_size % 2 != 0:
                array.append(-math.inf)

            for i in range(0, len(array), 2):
                if array[i] > array[i+1]:
                    temp_array.append(array[i]) 
                else:
                    temp_array.append(array[i+1])

            array = temp_array[:]
            temp_array.clear()

        max_val = array[0]
        sorted_array.append(max_val)
        original_array[original_array.index(max_val)] = -math.inf


def run(array: list):
    sorted_array = []

    print('Array before sorting: ', array)
    print()
    __tournament_sort(array, sorted_array)
    print()
    print('Array after sorting: ', sorted_array)
