from DFSTimeCounter import *

class Node:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.parent = None
    
    def get_set(self):
        return (self.i, self.j)

class UndirectedGraph:
    
    # n is the number of vertices
    # we will label the vertices from 0 to self.n -1 
    # Initialize to an empty adjacency list
    # We will store the outgoing edges using a set data structure
    def __init__(self):
        self.nodes_list = []
        self.adj_list = {} # tpye of dictionary

    def add_node(self,new_node):
        self.nodes_list.append(new_node)
        
    def add_edge(self, key, list_of_nodes):
        self.adj_list[key] = list_of_nodes
        
    # get a set of all vertices that 
    # are neighbors of the
    # vertex i
    def get_neighboring_vertices(self, node):
        temp_tuple = tuple(node.get_set())
        # print(f'debug - type of temp_tuple = {temp_tuple}')
        # print("")
        return self.adj_list[temp_tuple]
    
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
        #dfs_timer.increment() //delete this line from notebook
        # your code here
        # ----------------------------------------
        import collections
        # create a stack = new Stack
        stack = collections.deque([])
        # create a set_visited = {}
        visited = []
        # add root to into FIFO stack
        stack.append(i)

        debug_counter = 0

        # while (stack is not empty)
        while(len(stack) > 0 and debug_counter < 100):
            debug_counter = debug_counter + 1

            #   temp_verticy = stack.pop
            current_verticy = stack.pop()
            print("------------temp_verticy = ", current_verticy)

            #   add temp_verticy into set_visited
            visited.append(current_verticy)
        
            #   add adjacent_verticies into stack
            #       if elemnt_adjacent_verticy not in stack
            #           add element_adjacent_verticy into stack
            temp_children = list(self.get_neighboring_vertices(current_verticy))
            temp_children.sort(reverse=True)
            print("debug, temp_children = ", temp_children)
            temp_count_of_new_child = 0
            for element in temp_children:
                # if current_verticy in visited and element in visited:
                #     dfs_back_edges.append(current_verticy)
                #     dfs_back_edges.append(element)
                print(f'edge - {(current_verticy,element)}')

                print("debug, edge ")
                if element not in visited and element not in stack:
                    stack.append(element)
                    temp_count_of_new_child = temp_count_of_new_child + 1

        
            print("debug, stack = ", stack)
            # print("debug len(stack) = ", len(stack))
        
            #   if temp_verticy not in set_visited
            #       set visited time in discovery_times[i]
            if discovery_times[current_verticy] == None:
                dfs_timer.increment()
                discovery_times[current_verticy] = dfs_timer.get()
                
                
            #   else temp_verticy in set_visited
            #       set finish time in finish_times[i]
            if len(temp_children) == 1 and temp_count_of_new_child == 0 and finish_times[current_verticy] == None:
                dfs_timer.increment()
                finish_times[current_verticy] = dfs_timer.get()
                
        
            # print("debug, discovery_times = ", discovery_times)
            # print("debug, finish_times = ", finish_times)
            # print("debug, dfs_tree_parent = " , dfs_tree_parent)
            # print("debug, dfs_back_edges = ", dfs_back_edges)

        # end loop

        for i in range(len(visited) - 1, -1, -1):
            if(finish_times[i] == None):
                dfs_timer.increment()
                finish_times[i] = dfs_timer.get()

        print("visited = ", visited)
        print("debug, discovery_times = ", discovery_times)
        print("debug, finish_times = ", finish_times)
        # print("debug, dfs_tree_parent = " , dfs_tree_parent)
        print("debug, dfs_back_edges = ", dfs_back_edges)
    
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
