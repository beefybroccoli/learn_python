from TreeNode import *

"""
## Problem 1 (15 points)

In this problem, you are given a binary search tree whose keys are numbers. We would like to convert it to a list of all nodes with keys at depth 1 (root), depth 2 (children of root), and so on. At each depth, the keys must appear from left to right.

The example below will clarify the problem.

### Example

Consider the BST below as input:
<img src="attachment:tree1.png" width="25%"/>

You will need to output the list
~~~
[11, 4, 18, 15, 21, 13, 17]
~~~
"""

def traverseTree(root_node):
    temp_list = []
    if root_node.left != None:
        temp_list.append(root_node.left.key)
    if root_node.right != None:
        temp_list.append(root_node.right.key)
    
    if root_node.left != None :
        temp_list = temp_list + traverseTree(root_node.left)
    
    if root_node.right != None :
        temp_list = temp_list + traverseTree(root_node.right)  
    
    return temp_list
    # return [root_node.key] + traverseTree(root_node)

# TODO: Implement the function depthWiseTraverse below
def depthWiseTraverse(root_node):
    # This function inputs the root node of the tree.
    # root_node is an instance of the TreeNode class provided to you above
    # See description and example above.
    # your code here
    # ---------------------------------------------------------------
    # perform BFS on a tree
    # use python list as a FIFO data structure to queue nodes
    visited_node = []
    visited_key = []
    queue = []
    queue.append(root_node)
    while (len(queue) > 0):
        # get the first node from queue
        current_node = queue[0]
        # delete the first node from queue
        queue = queue[1:]
        # append the current_node to list of visited_nodes
        visited_node.append(current_node)
        # append the current key to list of visited keys
        visited_key.append(current_node.key)
        # append the left child node to queue
        if current_node.left != None:
            queue.append(current_node.left)
        # append the right child node to queue
        if current_node.right != None:
            queue.append(current_node.right)
        # debug
        # print(f'debug - current_node = {current_node.key}')
        # for element in queue:
            # print(f'debug - element = {element.key}')
        # print("debug - ---------------")
    
    return visited_key
    

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
print(f'return {lst1}')
assert lst1 == [11, 4, 18, 15, 21, 13, 17]
print("")

print('-- Test 2 --')
tree2 = make_tree([3, 1, 2, 4, 6, 7])
lst2 = depthWiseTraverse(tree2)
print(lst2)
assert lst2 == [3, 1, 4, 2, 6, 7]
print("")

print('-- Test 3 --')
tree3 = make_tree([7, 3, 1, 2, 4, 6, 15, 8, 11, 10, 9])
lst3 = depthWiseTraverse(tree3)
print(f'return  {lst3}')
assert lst3 == [7, 3, 15, 1, 4, 8, 2, 6, 11, 10, 9]
print("")

print('All tests passed: 15 points')