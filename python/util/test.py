from binarytree import tree, bst, heap

# Generate a random binary tree
random_tree = tree(height=3, is_perfect=False)
print(random_tree)

# Generate a random BST
random_bst = bst(height=3, is_perfect=True)
print(random_bst)

# Generate a random max heap
random_heap = heap(height=3, is_max=True, is_perfect=False)
print(random_heap)
