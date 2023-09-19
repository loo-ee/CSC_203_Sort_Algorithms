from colorama import Fore
from python import insertion_sort, merge_sort, quick_sort, selection_sort, shell_sort, bubble_sort, bucket_sort, comb_sort, radix_sort, max_heap, min_heap, tree_sort
from python.util.util import get_input, colored_array_print

def main():
    array_original = [10, -5, 5, 55, 23, 0, -1, 8, 99, 34, 56, 67, 3, 58, -9]
    choice: int

    while (True):
        array = array_original[:]
        getting_input = True
        is_new_array = 'Y'
        print_menu()

        while getting_input:
            try:
                choice = int(input('Enter choice: '))
            except:
                print("Enter a valid input...")
                continue

            if choice in range(13):
                getting_input = False


        if choice == 0:
            break

        if choice != 9:
            print(array)
            is_new_array = input('Do you want you use this array? (y/N): ')
        
        if is_new_array == 'N':
            array = get_input()
            array_original = array[:]

        if choice == 1:
           insertion_sort.run(array) 
        elif choice == 2:
            merge_sort.run(array)
        elif choice == 3:
            quick_sort.run(array)
        elif choice == 4:
            selection_sort.run(array)
        elif choice == 5:
            shell_sort.run(array)
        elif choice == 6:
            bucket_sort.run(array)
        elif choice == 7:
            bubble_sort.run(array)
        elif choice == 8:
            comb_sort.run(array)
        elif choice == 9:
            radix_sort.run()
        elif choice == 10:
            max_heap.run()
        elif choice == 11:
            min_heap.run()
        elif choice == 12:
            tree_sort.run(array)


def print_menu():
    print()
    colored_array_print("SELECT OPERATION", Fore.GREEN, False)

    print('''

    [0] EXIT
    [1] INSERTION SORT
    [2] MERGE SORT
    [3] QUICK SORT
    [4] SELECTION SORT
    [5] SHELL SORT
    [6] BUCKET SORT
    [7] BUBBLE SORT
    [8] COMB SORT
    [9] RADIX SORT
    [10] MAX HEAP SORT
    [11] MIN HEAP SORT
    [12] TREE SORT
    ''')


if __name__ == '__main__':
    main()
