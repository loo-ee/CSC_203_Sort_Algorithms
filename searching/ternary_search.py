from colorama import Fore
from util.util import custom_print, colored_array_print, find_target
from sorting import selection_sort


__iterations = 0


def __ternary_search(array: list, start: int, end: int, target: int):
    if start > end:
        return -1

    global __iterations
    __iterations += 1

    mid1 = start + (end - start) // 3
    mid2 = end - (end - start) // 3

    print()
    colored_array_print("PASS " + str(__iterations), Fore.YELLOW, False)
    print()

    if array[mid1] == target:
        custom_print(array, [array[mid1]], [array[mid2]])
        print()

        return mid1

    if array[mid2] == target:
        custom_print(array, [array[mid2]], [])
        print()

        return mid2

    custom_print(array, [], [array[mid1], array[mid2]])
    print()

    if array[mid1] > target:
        return __ternary_search(array, start, mid1 -1, target)
    elif array[mid2] < target:
        return __ternary_search(array, mid2 +1, end, target)
    else:
        return __ternary_search(array, mid1 +1, mid2 -1, target)
    

def run(array: list):
    print()
    colored_array_print("USING SELECTION SORT TO SORT ARRAY", Fore.YELLOW, False)
    print()

    selection_sort.run(array)
    target = find_target()
    print()

    found_index = __ternary_search(array, 0, len(array) -1, target)
    print()

    if found_index != -1:
        colored_array_print(
            "ELEMENT FOUND AT INDEX " + str(found_index), Fore.CYAN, False
        )
    else:
        colored_array_print("ELEMENT WAS NOT FOUND", Fore.RED, False)

    print("\n")


