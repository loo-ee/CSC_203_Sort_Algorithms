from binarytree import Node
from colorama import Fore
from util.util import custom_print, colored_array_print


class __TreeNode:

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


tree: __TreeNode
visual_tree: Node


def __insert_to_tree(node: __TreeNode, value: int):
    tree_ptr = node
    prev_node = None

    while tree_ptr is not None:
        prev_node = tree_ptr

        if value > tree_ptr.value:
            tree_ptr = tree_ptr.right
        else:
            tree_ptr = tree_ptr.left

    if value > prev_node.value:
        prev_node.right = __TreeNode(value)
    else:
        prev_node.left = __TreeNode(value)


def __create_visual_tree(tree: __TreeNode, visual_tree: Node):
    if tree is None:
        return

    if tree.left is not None:
        visual_tree.left = Node(tree.left.value)
        __create_visual_tree(tree.left, visual_tree.left)

    if tree.right is not None:
        visual_tree.right = Node(tree.right.value)
        __create_visual_tree(tree.right, visual_tree.right)


def __tree_sort(tree: __TreeNode, output_array: list):
    if tree.left is not None:
        __tree_sort(tree.left, output_array)

    output_array.append(tree.value)

    if tree.right is not None:
        __tree_sort(tree.right, output_array)


def run(array: list):
    global tree
    global visual_tree
    output_array = []

    tree = __TreeNode(array[0])
    visual_tree = Node(tree.value)

    for element in array[1:]:
        print()
        colored_array_print("INSERTING " + str(element), Fore.YELLOW, False)
        print()

        __insert_to_tree(tree, element)
        __create_visual_tree(tree, visual_tree)

        print(visual_tree)
        custom_print(array, [element], [])
        print('\n*****************************************************************')

    __create_visual_tree(tree, visual_tree)
    __tree_sort(tree, output_array)
    print(visual_tree)
    print('\n')
    colored_array_print("FINAL SORTED ARRAY", Fore.BLUE, False)
    print()
    colored_array_print(output_array, Fore.RED)
    print('\n')
