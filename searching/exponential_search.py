from colorama import Fore
from util.util import custom_print, colored_array_print, find_target
from sorting import selection_sort
from searching import binary_search


def __exponential_search(array: list, target):
    if array[0] == target:
        return 0

    index = 1
    iterations = 0
    arr_len = len(array)

    while index < arr_len and array[index] <= target:
        iterations += 1

        print()
        colored_array_print("PASS " + str(iterations), Fore.YELLOW, False)
        print()

        custom_print(array, [], array[:index], [array[index]])
        print()

        index *= 2

    start = index // 2
    end = min(index, arr_len)

    print()
    colored_array_print("USING BINARY SEARCH", Fore.YELLOW, False)
    print()

    return binary_search.binary_search(array, start, end, target) 


def run(array: list):
    print()
    colored_array_print("USING SELECTION SORT TO SORT ARRAY", Fore.YELLOW, False)
    print()

    selection_sort.run(array)
    target = find_target()
    print()
    found_index = __exponential_search(array, target)
    print()

    if found_index != -1:
        colored_array_print(
            "ELEMENT FOUND AT INDEX " + str(found_index), Fore.CYAN, False
        )
    else:
        colored_array_print("ELEMENT WAS NOT FOUND", Fore.RED, False)

    print("\n")
