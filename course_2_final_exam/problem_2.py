from TreeNode import *

def sumOfBranches(root_node):
    # return a list of sums 
    # your code here
    # ------------------------------------------------------
        # perform BFS on a tree
    # use python list as a FIFO data structure to queue nodes
    visited_node = []
    leaf_node = []
    queue = []
    root_node.parent = None
    queue.append(root_node)
    while (len(queue) > 0):
        # get the first node from queue
        current_node = queue[0]
        # delete the first node from queue
        queue = queue[1:]
        # append the current_node to list of visited_nodes
        visited_node.append(current_node)
        # append the left child node to queue
        if current_node.left != None:
            current_node.left.parent = current_node
            queue = [current_node.left] + queue
        # append the right child node to queue
        if current_node.right != None:
            current_node.right.parent = current_node
            queue = [current_node.right]  + queue
        if current_node.left == None and current_node.right == None:
            leaf_node.append(current_node)
        
        print(f'debug - current_node = {current_node.key}')
        for element in queue:
            print(f'debug - element = {element.key}')
        print("debug - ---------------")
    
    for element in leaf_node:
        if element.parent != None:
            print(f'debug - leaf node = {element.key}, parent = {element.parent.key}')
        else:
            print(f'debug - leaf node = {element.key}, parent = None')
    
    result_list = []
    for index in range(len(leaf_node)-1, -1, -1):
        print(f'leaf_node[{index}].key = {leaf_node[index].key }')
        result_list.append(sum_branch(leaf_node[index]))
    
    return result_list

def sum_branch(current_node):
    if current_node.parent == None:
        return current_node.key
    return current_node.key + sum_branch(current_node.parent)


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

# print('All tests passed: 15 points!')

