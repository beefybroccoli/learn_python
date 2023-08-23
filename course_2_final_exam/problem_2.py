from TreeNode import *

def sumOfBranches(root_node):
    # return a list of sums 
    # your code here
    pass

def make_tree(insertion_list):
    assert len(insertion_list) > 0
    root_node = TreeNode(insertion_list[0])
    for elt in insertion_list[1:]:
        root_node.insert(elt)
    return root_node

print('-- Test 1 --')
# Same as the example from problem 1
tree1 = make_tree([11, 18, 15,  13, 21, 17, 4])
lst1 = sumOfBranches(tree1)
print(lst1)
assert lst1 == [15, 57, 61, 50]

print('-- Test 2 --')
# Same as example from problem 2

tree2 = make_tree([11,4, 18, -1, 7, 15, 21, 2, 13, 17])
lst2 = sumOfBranches(tree2)
print(lst2)
assert lst2 == [16, 22, 57, 61, 50]

print('-- Test 3 --')
tree3 = make_tree([15])
lst3 = sumOfBranches(tree3)
print(lst3)
assert lst3 == [15]

print('-- Test 4 --')
tree4 = make_tree([4, 1, 2, 3, 8, 5, 6, 7,  10, 9])
lst4 = sumOfBranches(tree4)
print(lst4)
assert lst4 == [10, 30, 31]

print('All tests passed: 15 points!')

