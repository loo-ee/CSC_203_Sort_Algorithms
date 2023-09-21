from util.util import custom_print, colored_array_print, swap
from colorama import Fore


def __quick_sort(array: list, start: int, end: int, iter_pass: int):
    if end <= start:
        return
    
    pivot = array[end]
    traversal_ptr = start
    swap_ptr = start

    colored_array_print("PASS " + str(iter_pass), Fore.YELLOW, False)
    print()

    while traversal_ptr < end:
        if array[traversal_ptr] < pivot:
            custom_print(array[start:end + 1], [array[traversal_ptr]], [array[end]])
            print(" ", array[traversal_ptr], " < ", pivot, ' PERFORMING SWAP')

            swap(array, traversal_ptr, swap_ptr)
            swap_ptr += 1
            
        traversal_ptr += 1

    custom_print(array[start:end + 1], [array[traversal_ptr]], [array[swap_ptr]])
    print(' Swapping pivot and red pointer')
    swap(array, traversal_ptr, swap_ptr)
    iter_pass += 1

    colored_array_print(array[start:end + 1], Fore.BLUE)
    print(' from PASS', iter_pass)
    print()

    if swap_ptr > start:
        __quick_sort(array, start, swap_ptr - 1,  iter_pass)
    if swap_ptr < end:
        __quick_sort(array, swap_ptr + 1, end, iter_pass)


def run(array: list):
    iter_pass = 0

    print('Array before sorting: ', array, '\n')
    __quick_sort(array, 0, len(array) -1, iter_pass)
    print('Array after sorting: ', array)
