from colorama import Fore
from util.util import custom_print, colored_array_print, find_target
from sorting import selection_sort

def __binary_search(array: list, start: int, end: int, target: int):
    if start > end:
        return -1

    mid = start + ((end - start) // 2)

    if array[mid] == target:
        custom_print(array, [array[mid]], array[:start] + array[end +1:])
        print()

        return mid
    elif array[mid] > target:
        custom_print(array, [], array[:start] + array[end +1:], [array[mid]])
        print('-->', array[start:end + 1])

        return __binary_search(array, start, mid - 1, target)
    else:
        custom_print(array, [], array[:start] + array[end +1:], [array[mid]])
        print('-->', array[start:end + 1])

        return __binary_search(array, mid + 1, end, target)
    

def run(array: list):
    print()
    colored_array_print("USING SELECTION SORT TO SORT ARRAY", Fore.YELLOW, False)
    print()

    selection_sort.run(array)
    target = find_target()
    print()
    found_index = __binary_search(array, 0, len(array) - 1, target)
    print()

    if found_index != -1:
        colored_array_print(
            "ELEMENT FOUND AT INDEX " + str(found_index), Fore.BLUE, False
        )
    else:
        colored_array_print("ELEMENT WAS NOT FOUND", Fore.RED, False)

    print("\n")
