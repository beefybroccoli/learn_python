# This is a useful data structure for implementing 
# a counter that counts the time.
class DFSTimeCounter:
    def __init__(self):
        self.count = 0
    
    def reset(self):
        self.count = 0
    
    def increment(self):
        self.count = self.count + 1
        
    def get(self):
        return self.count 
    
class UndirectedGraph:
    
    # n is the number of vertices
    # we will label the vertices from 0 to self.n -1 
    # Initialize to an empty adjacency list
    # We will store the outgoing edges using a set data structure
    def __init__(self, n):
        self.n = n
        self.adj_list = [ set() for i in range(self.n) ]
        
    def add_edge(self, i, j):
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        assert i != j
        # Make sure to add edge from i to j
        self.adj_list[i].add(j)
        # Also add edge from j to i
        self.adj_list[j].add(i)
        
    # get a set of all vertices that 
    # are neighbors of the
    # vertex i
    def get_neighboring_vertices(self, i):
        assert 0 <= i < self.n
        return self.adj_list[i]
    
    # Function: dfs_visit
    # Program a DFS visit of a graph.
    # We maintain a list of discovery times and finish times.
    # Initially all discovery times and finish times are set to None.
    # When a vertex is first visited, we will set discovery time
    # When DFS visit has processed all the neighbors then set the finish time.
    # DFS visit should update the list of discovery and finish times in-place 
    #  
    # Arguments
    #  i         --> id of the vertex being visited.
    #  dfs_timer --> An instance of DFSTimeCounter structure provided for you.
    #  discovery --> discovery time of each vertex -- a list of size self.n
    #                None if the vertex is yet to be visited.
    #  finish    --> finish time of each vertex -- a list of size self.n
    #                None if the vertex is yet to be finished.
    #  dfs_tree_parent --> the parent for for each node 
    #                      if we visited node j from node i, then j's parent is i.
    #                      Do not forget to set tree_parent when you call dfs_visit on node j from node i.
    #  dfs_back_edges --> a list of back edges.
    #                     a back edge is an edge from i to j wherein DFS has already discovered j when i is discovered,
    #                       but not finished j
    
    def dfs_visit(self, i, dfs_timer, discovery_times, finish_times, dfs_tree_parent, dfs_back_edges):
        assert 0 <= i < self.n
        assert discovery_times[i] == None
        assert finish_times[i] == None
        discovery_times[i] = dfs_timer.get()
        dfs_timer.increment()
        # your code here
        # ----------------------------------------
        import collections
        stack = collections.deque([])
        
        
        current_verticy = i
        temp_children = list(self.get_neighboring_vertices(current_verticy))
        temp_children.sort()
        print("-------------------")
        print(f'parent = {dfs_tree_parent[current_verticy]}')
        print(f'current_verticy = {current_verticy}')
        print("debug, temp_children = ", temp_children)
        print(f'discovery_times = {discovery_times}')
        print("")

        if len(temp_children) == 0:
            print("base case - pass")
        elif discovery_times[i] != None and discovery_times[i] > dfs_timer.get() + 1:
            print("already visited")
        else:
            for element in temp_children:
                if(discovery_times[element] == None):
                    dfs_tree_parent[element] = current_verticy
                    self.dfs_visit(element, dfs_timer, discovery_times, finish_times, dfs_tree_parent, dfs_back_edges)

    
        # ===================================================================================================
    # Function: dfs_traverse_graph
    # Traverse the entire graph.
    def dfs_traverse_graph(self):
        dfs_timer = DFSTimeCounter()
        discovery_times = [None]*self.n
        finish_times = [None]*self.n
        dfs_tree_parents = [None]*self.n
        dfs_back_edges = []
        for i in range(self.n):
            if discovery_times[i] == None:
                self.dfs_visit(i,dfs_timer, discovery_times, finish_times, 
                               dfs_tree_parents, dfs_back_edges)
        # Clean up the back edges so that if (i,j) is a back edge then j cannot be i's parent.
        non_trivial_back_edges = [(i,j) for (i,j) in dfs_back_edges if dfs_tree_parents[i] != j]
        return (dfs_tree_parents, non_trivial_back_edges, discovery_times, finish_times)


# create the graph from problem 1A.
g = UndirectedGraph(5)
# print("g.n = ", g.n); print(g.adj_list); g.add_edge(0,1); print(g.adj_list); g.add_edge(0,2); print(g.adj_list)
# g.add_edge(0,4); print(g.adj_list); g.add_edge(2,3); print(g.adj_list); g.add_edge(2,4); print(g.adj_list); g.add_edge(3,4)
# print(g.adj_list)

print("g.n = ", g.n); g.add_edge(0,1); g.add_edge(0,2); g.add_edge(0,4); g.add_edge(2,3); g.add_edge(2,4); g.add_edge(3,4)
print(g.adj_list)

# Test DFS visit
discovery_times = [None]*5; finish_times = [None]*5; dfs_tree_parents = [None]*5; dfs_back_edges = []
g.dfs_visit(0, DFSTimeCounter(), discovery_times, finish_times, dfs_tree_parents, dfs_back_edges )
print(f'dfs_tree_parents = {dfs_tree_parents}')

# # for i in range(5):
# #     print(f'{i} \t {discovery_times[i]}\t\t {finish_times[i]}')

# assert(discovery_times[0] == 0), f'Fail: Node 0 expected discovery time must be 0'
# assert(discovery_times[1] == 1), f'Fail: Node 1 expected discovery is 1'
# assert(discovery_times[2] == 3), f'Fail: Node 2 expected discovery is 3'
# assert(discovery_times[3] == 4),f'Fail: Node 3 discovery time expected value is 4'
# assert(discovery_times[4] == 5),f'Fail: Node 4 discovery time expected value is 5'

# assert(finish_times[1] == 2), f'Fail: Node 1 finish time expected value is 2 (are you incrementing counter before you return from dfs_visit function and before recording finish times)'
# assert(finish_times[2] == 8), f'Fail: Node 2 finish time expected value is 8'
# assert(finish_times[3] == 7), f'Fail: Node 3 finish time expected value is 7'
# assert(finish_times[4] == 6), f'Fail: Node 4 finish time expected value is 6'

# print()
# # Filter out all trivial back eddges (i,j)  where j is simply the parent of i.
# # such back edges occur because we are treating an undirected edge as two directed edges
# # in either direction.