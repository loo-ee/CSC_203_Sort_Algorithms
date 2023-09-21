from binarytree import Node
from colorama import Fore
from util import custom_print, colored_array_print


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


def max_heapify(array: list, parent_index: int):
    left = find_left(parent_index)
    right = find_right(parent_index)

    if left < len(array) and array[left] > array[parent_index]:
        largest = left
    else:
        largest = parent_index

    if right < len(array) and array[right] > array[largest]:
        largest = right

    print('Largest Node: ', end="")
    custom_print(array, [array[parent_index]], [array[largest]])
    print()

    if largest != parent_index:
        print('Swapping positons...')

        array[parent_index], array[largest] = array[largest], array[parent_index]
        print('Next index to find max: ', largest)
        custom_print(array, [array[largest]], [])
        print()

        global root
        root = Node(array[0])
        construct_heap(array, 0, root)
        print(root)
        max_heapify(array, largest)


def build_max_heap(array: list):
    count = 0
    mid_arr = int((len(array) // 2) - 1)

    for i in range(mid_arr, -1, -1):
        count += 1
        print('\nITERATION ', count, ' index: ', i)
        max_heapify(array, i)
        print('<------------------------------------------->')

    global root
    print('\n')
    colored_array_print("FINAL MAX HEAP TREE", Fore.BLUE, False)
    print()
    print(root)


array = [10, 20, 15, 12, 40, 25, 18]
build_max_heap(array)
print(array)
