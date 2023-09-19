from binarytree import Node
from colorama import Fore
from python.util.util import custom_print, colored_array_print


root: Node


def construct_heap(array: list, index, node):
    left = index * 2 + 1
    right = index * 2 +2

    if left < len(array):
        node.left = Node(array[left]) 
        construct_heap(array, left, node.left)

    if right < len(array):
        node.right = Node(array[right])
        construct_heap(array, right, node.right)


def find_left(parent_index: int):
    return 2 * parent_index + 1

def find_right(parent_index: int):
    return 2 * parent_index + 2


def min_heapify(array: list, parent_index: int):
    left = find_left(parent_index)
    right = find_right(parent_index)

    if left < len(array) and array[left] < array[parent_index]:
        least = left
    else:
        least = parent_index

    if right < len(array) and array[right] < array[least]:
        least = right

    print('Largest Node: ', end="")
    custom_print(array, [array[parent_index]], [array[least]])
    print()

    if least != parent_index:
        print('Swapping positons...')

        array[parent_index], array[least] = array[least], array[parent_index]
        print('Next index to find max: ', least)
        custom_print(array, [array[least]], [])
        print()

        global root
        root = Node(array[0])
        construct_heap(array, 0, root)
        print(root)
        min_heapify(array, least)


def build_min_heap(array: list):
    count = 0
    mid_arr = int((len(array) // 2) - 1)

    for i in range(mid_arr, -1, -1):
        count += 1
        print('\nITERATION ', count, ' index: ', i)
        min_heapify(array, i)
        print('<------------------------------------------->')


    global root
    print('\n')
    colored_array_print("FINAL MIN HEAP TREE", Fore.BLUE, False)
    print()
    print(root)


def run():
    array = [15, 33, 45, 9, 7, 2, 5, 85, 23, 1, 10, 99, 3, 67, 22, 6]
    build_min_heap(array)
    colored_array_print("FINAL MIN HEAP SORT", Fore.GREEN, False)
    print()
    colored_array_print(array, Fore.RED)
    print()
