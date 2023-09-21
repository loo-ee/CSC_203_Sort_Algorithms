from util.util import custom_print


def bubble_sort(array: list):
    arr_len = len(array)
    print("Array len: ", arr_len)

    for i in range(arr_len + 1):
        sorted = True

        print('\nPASS ', i + 1, ': ')

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
            print('\nARRAY IS NOW SORTED')
            break
    
def run(array: list):
    print('Array before sorting: ', array)
    bubble_sort(array)
    print('Array after sorting: ', array)
