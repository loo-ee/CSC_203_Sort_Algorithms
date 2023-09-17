from python import insertion_sort, merge_sort, quick_sort, selection_sort, shell_sort, bubble_sort, bucket_sort, comb_sort, radix_sort
from python.util import util

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

            if choice in range(12):
                getting_input = False


        if choice == 0:
            break

        if choice != 9:
            print(array)
            is_new_array = input('Do you want you use this array? (y/N): ')
        
        if is_new_array == 'N':
            array = util.get_input()
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


def print_menu():
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
    [10] MIN HEAP
    [11] MAX HEAP
    ''')


if __name__ == '__main__':
    main()
