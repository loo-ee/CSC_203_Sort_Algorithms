from colorama import Fore
from util.util import custom_print, colored_array_print


def __bubble_sort(array: list):
    arr_len = len(array)
    print("Array len: ", arr_len)

    for i in range(arr_len + 1):
        sorted = True

        print()
        colored_array_print("PASS " + str(i+1), Fore.YELLOW, False)
        print()

        for j in range(arr_len - 1):
            el1 = array[j]
            el2 = array[j + 1]

            custom_print(array, [el1], [el2])

            if array[j] > array[j + 1]:
                sorted = False
                print('\t', el1, ' is greater than ', el2, ',  swapping...')

                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            
            else:
                print('\t', el1, ' is less than ', el2, ', no swap needed')

        if sorted:
            print()
            colored_array_print("ARRAY IS NOW SORTED", Fore.GREEN, False)
            print()
            break
    
def run(array: list):
    print('Array before sorting: ', array)
    __bubble_sort(array)
    print('Array after sorting: ', array)
