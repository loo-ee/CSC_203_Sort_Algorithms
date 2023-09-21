from colorama import Fore
from util.util import colored_array_print 


def __radix_sort(array: list):
    bins = [[] for _ in range(10)]
    output_arr = []
    max_el = max(array)
    multiplier = 10
    divisor = 1
    modulo_factor = 10

    while max_el >= divisor: 
        for element in array:
            if element < divisor:
                num_to_sort = 0
            else:
                num_to_sort = int(element / divisor) % modulo_factor

            bins[num_to_sort].append(element)

        for queue in bins:
            while len(queue) != 0:
                item = queue.pop(0) 
                output_arr.append(item)

        bins = [[] for _ in range(10)]
        array = output_arr[:]
        output_arr.clear()

        colored_array_print(array, Fore.BLUE)
        print(f" -> {divisor}'s place")

        divisor *= multiplier


def __get_input():
    input_arr = []

    while True:
    
        try:
            num = int(input('Enter number: '))

            if num < 0:
                print('Input must not be negative...')
            else:
                input_arr.append(num)
        except:
            break

    return input_arr


def run():
    array = [100, 230, 56, 34, 67, 1]

    print(array)
    is_new_array = input('Do you want you use this array? (y/N): ')

    if is_new_array == 'N':
        array = __get_input()

    print('\nArray before sorting: ', array)
    print()
    __radix_sort(array)
    print('\nArray after sorting: ', array)