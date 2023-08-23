from DFSTimeCounter import *

class Node:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.parent = None
        self.visited = False
        self.inQueue = False
    
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
    
    def get_pointer(self, i,j):
        print(f'debug -, i = {i}, j = {j}')
        for each_node in self.nodes_list:
            if each_node.i == i and each_node.j == j:
                return each_node
    def bfs(self):
        # create lists
        visited_node = []
        queue = []

        # set the first node's parent to None
        self.nodes_list[0].parent = None

        # append first node to queue
        queue.append(self.nodes_list[0])

        while(len(queue) > 0):
            # get the first node from queue
            current_node = queue[0]
            current_node.visited = True

            # add current_node to visited node
            visited_node.append(current_node)

            # delete first node from queue
            # print(f'debug - before, len(queue) = {len(queue)}')
            queue = queue[1:]
            # print(f'debug - after, len(queue) = {len(queue)}')
            
            print(f'debug - len(visited_node) = {len(visited_node)}')
            print(f'debug - current_node = {current_node.get_set()}')
            
            # print(f'debug - self.get_neighboring_vertices(current_node) return {type(self.get_neighboring_vertices(current_node))}')

            for each_adjacent_node in self.get_neighboring_vertices(current_node):
                pointer = self.get_pointer(each_adjacent_node.i, each_adjacent_node.j)

                if pointer.visited == False and pointer.inQueue == False:
                    print(f'pointer.get_set() = - {pointer.get_set()}')
                    pointer.parent = current_node
                    pointer.inQueue = True
                    queue.append(each_adjacent_node)
            print("-----------------")
        
    
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
        stack.append(self.nodes_list[i])

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
            list_adjacent_nodes = self.get_neighboring_vertices(current_verticy)

            for each_adjacent_node in list_adjacent_nodes:
                # if current_verticy in visited and element in visited:
                #     dfs_back_edges.append(current_verticy)
                #     dfs_back_edges.append(element)
                print(f'edge - {(current_verticy,each_adjacent_node)}')

                print("debug, edge ")
                if each_adjacent_node not in visited and each_adjacent_node not in stack:
                    stack.append(each_adjacent_node)
        
            print("debug, stack = ", stack)
            # print("debug len(stack) = ", len(stack))
        
            #   if temp_verticy not in set_visited
            #       set visited time in discovery_times[i]
            if discovery_times[current_verticy] == None:
                dfs_timer.increment()
                discovery_times[current_verticy] = dfs_timer.get()
                
                
            #   else temp_verticy in set_visited
            #       set finish time in finish_times[i]
            if finish_times[current_verticy] == None:
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
