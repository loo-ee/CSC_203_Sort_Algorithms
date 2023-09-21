from colorama import Fore
from util.util import custom_print, colored_array_print, find_target
from sorting import selection_sort


__iterations = 0


def __interpolation_search(array: list, start: int, end: int, target: int):
    global __iterations
    __iterations += 1

    if start <= end and target >= array[start] and target <= array[end]:
        index = start + ((end - start) / (array[end] - array[start]) * (target - array[start]))
        index = int(index)

        colored_array_print("PASS " + str(__iterations), Fore.YELLOW, False)
        print()

        print(f"""
        index_position = {start} + [(({end} - {start}) / {array[end]} - {array[start]}) * ({target} - {array[start]})] 
        index_position = {index} 
        """)

        if array[index] == target:
            custom_print(array, [array[index]], [])
            print()

            return index

        if array[index] < target:
            custom_print(array, [], [array[index]])
            print()

            return __interpolation_search(array, index +1, end, target)
        
        if array[index] > target:
            custom_print(array, [], [array[index]])
            print()

            return __interpolation_search(array, index -1, start, target)

    return -1


def run(array: list):
    print()
    colored_array_print("USING SELECTION SORT TO SORT ARRAY", Fore.YELLOW, False)
    print()

    selection_sort.run(array)
    target = find_target()
    print()
    print("""
        index_position = start + [((end - start) / A[end] - A[start]) * (target - A[start])]
    """)

    found_index = __interpolation_search(array, 0, len(array) -1, target)
    print()

    if found_index != -1:
        colored_array_print(
            "ELEMENT FOUND AT INDEX " + str(found_index), Fore.BLUE, False
        )
    else:
        colored_array_print("ELEMENT WAS NOT FOUND", Fore.RED, False)

    print("\n")
