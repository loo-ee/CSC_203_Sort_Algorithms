import math
from python.util.util import custom_print
 

def insertion_sort(array: list):
    forward_ptr: int
    backward_ptr: int
    array_len = len(array)
    swap = False

    for i in range(1, array_len):
        forward_ptr = i
        key = array[forward_ptr]
        backward_ptr = forward_ptr - 1

        while backward_ptr >= 0 and array[backward_ptr] > key:
            swap = True
            custom_print(array, [array[backward_ptr]], [array[forward_ptr]])
            array[backward_ptr + 1] = array[backward_ptr]
            print(' ', array[backward_ptr], end="")
            print(" > ", key, " swap")


            backward_ptr -= 1
            forward_ptr -= 1
            array[backward_ptr + 1] = key

        if backward_ptr >= 0 and array[backward_ptr] < key:
            custom_print(array, [array[backward_ptr]], [array[forward_ptr]])
            print(' ', array[backward_ptr], end="")
            print(" < ", key, " no swap")


        backward_ptr += 1

        if swap:
            custom_print(array, [], [], [key])
            print(' -->KEY IS PLACED INTO INDEX', backward_ptr)
        print()


def run(array: list):
    print('Array before sorting: ', array)
    insertion_sort(array)
    print('Array after sorting: ', array)
