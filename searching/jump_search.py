import math
from colorama import Fore
from util.util import custom_print, colored_array_print, find_target
from sorting import selection_sort


def __jump_search(array: list, target: int):
    arr_len = len(array)
    steps = math.floor(math.sqrt(arr_len))
    prev = 0

    while array[min(steps, arr_len) -1] < target:
        prev = steps
        steps += steps

        custom_print(array, [], array[:prev])
        print()

        if prev >= arr_len:
            return -1

    while array[prev] < target:
        prev += 1
        custom_print(array, [], array[:prev])
        print()

        if prev == min(steps, arr_len):
            return -1


    if array[prev] == target:
        custom_print(array, [array[prev]], array[:prev])
        print()

        return prev

    return -1


def run(array: list):
    print()
    colored_array_print("USING SELECTION SORT TO SORT ARRAY", Fore.YELLOW, False)
    print()

    selection_sort.run(array)
    target = find_target()
    print()
    found_index = __jump_search(array, target)
    print()

    if found_index != -1:
        colored_array_print(
            "ELEMENT FOUND AT INDEX " + str(found_index), Fore.CYAN, False
        )
    else:
        colored_array_print("ELEMENT WAS NOT FOUND", Fore.RED, False)

    print("\n")
