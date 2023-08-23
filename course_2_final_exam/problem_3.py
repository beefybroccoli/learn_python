from math import sqrt
from UndirectedGraph import *

# You may use this function to test if a point lies inside given circle.
def ptInCircle(x,y, circles_list):
    for (xc,yc,rc) in circles_list:
        d = sqrt ( (x-xc)**2 + (y-yc)**2)
        if d <= rc:
            return True
    return False

def findPath(width, height, forbidden_circles_list):
    # width is a positive number
    # height is a positive number
    # forbidden_circles_list is a list of triples [(x1, y1, r1),..., (xk, yk, rk)]
    assert width >= 1
    assert height >= 1
    assert all(x <= width and x >=0 and y <= height and y >= 0 and r > 0 for (x,y,r) in forbidden_circles_list)
    # your code here
    # --------------------------------------
    # append all edges to all_edges list
    all_edges = []
    
    for i in range(width + 1):
        for j in range(height + 1):
            print(f"i = {i}, j = {j}")
            all_edges.append((i,j))
    print(f"debug - possible_paths = {all_edges}")

    # append all possible edges to possible_edges list
    possible_edges = []
    for each_path in all_edges:
        temp_bool = ptInCircle(each_path[0], each_path[1], forbidden_circles_list)
        if temp_bool == False:
            possible_edges.append(each_path)
        print(f"debug - possible_edges = {possible_edges}")
    """
    possible edges = [(0, 0), (0, 1), (0, 3), (1, 0), (2, 0), (2, 1), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
    """

    g = UndirectedGraph()
    for each_edge in possible_edges :
        g.add_node(Node(each_edge[0], each_edge[1]))

    print(f"debug - len(possible_edges) = {len(possible_edges)}")
    print(f'debug - len(g.nodes_list) = {len(g.nodes_list)}')


    #  # create the graph from problem 1A.
    
    for each_edge in possible_edges:
        list_of_neighbor_nodes = []
        temp_x = each_edge[0]
        temp_y = each_edge[1]

        if (temp_x + 1, temp_y) in possible_edges:
            list_of_neighbor_nodes.append(Node(temp_x + 1,temp_y))

        if (temp_x - 1, temp_y) in possible_edges: 
            list_of_neighbor_nodes.append(Node(temp_x - 1,temp_y))

        if (temp_x, temp_y + 1) in possible_edges:
            list_of_neighbor_nodes.append(Node(temp_x, temp_y + 1))

        if (temp_x, temp_y - 1) in possible_edges:
            list_of_neighbor_nodes.append(Node(temp_x, temp_y - 1))
        
        g.add_edge((temp_x,temp_y), list_of_neighbor_nodes)
        print(f'len(g.adj_list) = {len(g.adj_list)}')

    for key in g.adj_list.keys():
        print("----")
        print(f'type of key = {type(key)}')
        print(f'{key} = {g.adj_list[key]}')
        for each_node in g.adj_list[key]:
            print(f"each_node = ({each_node.i}, {each_node.j})")
        print("----")
    
    for each_node in g.nodes_list:
        print("~~~~")
        print(f'each_node = {each_node.get_set()}')
        print(g.get_neighboring_vertices(each_node))
        for each_adjacent_node in g.get_neighboring_vertices(each_node):
            print(f"each_adjacent_node = {each_adjacent_node.get_set()}")
        print("~~~~")
    
    discovery_times = [None]*len(possible_edges)
    finish_times = [None]*len(possible_edges)
    dfs_tree_parents = [None]*len(possible_edges)
    dfs_back_edges = []
    # g.dfs_visit(g.nodes_list[0], DFSTimeCounter(), discovery_times, finish_times, dfs_tree_parents, dfs_back_edges )
    # print(f"dfs_tree_parents = {dfs_tree_parents}")

    return None

def checkPath(width, height, circles, path):
    assert path[0] == (0,0), 'Path must begin at (0,0)'
    assert path[-1] == (width, height), f'Path must end at {(width, height)}'
    (cur_x, cur_y) = path[0]
    for (new_x, new_y) in path[1:]:
        dx = new_x - cur_x
        dy = new_y - cur_y
        assert (dx,dy) in [(1,0),(-1,0), (0,1),(0,-1)]
        assert 0 <= new_x and new_x <= width
        assert 0 <= new_y and new_y <= height
        assert not ptInCircle(new_x, new_y, circles)
        cur_x, cur_y = new_x, new_y
    return

#----------------------------------------------------------------------------
print('-- Test 1 -- ')

circles = [(2,2,0.5), (1,2,1)]
p = findPath(3, 3, circles)
print(p)
# checkPath(3, 3, circles, p)
# print('-- Test 2 -- ')

# circles1 = [(2,2,1), (1,2,1)]
# p1 = findPath(3, 3, circles1)
# print(p1)
# assert p1 == [], 'Answer does not match with ours'

# print('-- Test 3 -- ')
# p2 = findPath(5,5, circles1)
# print(p2)
# checkPath(5, 5, circles1, p2)

# print('-- Test 4 --')

# circles3 = [(1,2,0.5), (2,2,1), (3,3,1),(4,3,1)]
# p3 = findPath(5, 5, circles3)
# print(p3)
# checkPath(5, 5, circles3, p3)

# print('-- Test 5 --')
# circles5 = [ (4,1, 1), (4,4,1),(2,6,1)]
# p5 = findPath(6,6,circles5)
# print(p5)
# assert p5 == []
# print('All tests passed: 15 points!')