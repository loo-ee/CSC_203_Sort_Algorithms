from python import insertion_sort, merge_sort, quick_sort, selection_sort, shell_sort, bubble_sort, bucket_sort, comb_sort
from python.util import util

def main():
    array_original = [45, 3, -2, 55, 1, 0, 5, 89, 78, 2, 9, 8, 4, 79, 85, 99, 100, 101]
    choice: int

    while (True):
        array = array_original[:]
        getting_input = True
        print_menu()

        while getting_input:
            try:
                choice = int(input('Enter choice: '))
            except:
                print("Enter a valid input...")

            if choice in range(10):
                getting_input = False


        if choice == 0:
            break

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
    ''')


if __name__ == '__main__':
    main()
