from TreeNode import *

# TODO: Implement the function depthWiseTraverse below
def depthWiseTraverse(root_node):
    # This function inputs the root node of the tree.
    # root_node is an instance of the TreeNode class provided to you above
    # See description and example above.
    # your code here
    pass    


def make_tree(insertion_list):
    assert len(insertion_list) > 0
    root_node = TreeNode(insertion_list[0])
    for elt in insertion_list[1:]:
        root_node.insert(elt)
    return root_node

print('-- Test 1 --')
# Same as the example above
tree1 = make_tree([11, 18, 15,  13, 21, 17, 4])
lst1 = depthWiseTraverse(tree1)
print(lst1)
assert lst1 == [11, 4, 18, 15, 21, 13, 17]

print('-- Test 2 --')

tree2 = make_tree([3, 1, 2, 4, 6, 7])
lst2 = depthWiseTraverse(tree2)
print(lst2)
assert lst2 == [3, 1, 4, 2, 6, 7]

print('-- Test 3 --')
tree3 = make_tree([7, 3, 1, 2, 4, 6, 15, 8, 11, 10, 9])
lst3 = depthWiseTraverse(tree3)
print(lst3)
assert lst3 == [7, 3, 15, 1, 4, 8, 2, 6, 11, 10, 9]

print('All tests passed: 15 points')