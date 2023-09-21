from colorama import Fore
from util.util import custom_print, colored_array_print, find_target


def __linear_search(array: list, target: int):
    arr_len = len(array)

    for index in range(arr_len):
        print()
        colored_array_print("PASS " + str(index + 1), Fore.YELLOW, False)
        print()

        if array[index] == target:
            custom_print(array, [array[index]], [])
            print('\n')
            return index
        else:
            custom_print(array, [], [array[index]])
            print('\n')

    return -1


def run(array: list):
    target = find_target()
    found_index = __linear_search(array, target)

    if found_index != -1:
        colored_array_print("ELEMENT FOUND AT INDEX " + str(found_index), Fore.BLUE, False)
    else:
        colored_array_print("ELEMENT WAS NOT FOUND", Fore.RED, False)
    
    print('\n')
    