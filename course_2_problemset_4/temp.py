class Vertex: # This is the outline for a vertex data structure
    
    def __init__ (self,  i, j):
        self.x = i # The x coordinate
        self.y = j  # The y coordinate
        self.d = float('inf') # the shortest path estimate
        self.processed = False # Has this vertex's final shortest path distance been computed
        # this is important for Dijksatra's algorithm
        # We will track where the vertex is in the priority queue.
        self.idx_in_priority_queue = -1 # The index of this vertex in the queue
        self.pi = None # the parent vertex in the shortest path tree.
        
    def reset(self):
        self.d = float('inf')
        self.processed = False # Has this vertex's final shortest path distance been computed
        # this is important for Dijksatra's algorithm
        # We will track where the vertex is in the priority queue.
        self.idx_in_priority_queue = -1 # The index of this vertex in the queue
        self.pi = None # the parent vertex in the shortest path tree.

# However, if you want Dijkstra efficiently, we will need a priority queue
# We will provide you with a heap data structure from course 1.
class PriorityQueue:
    # Constructor:  Implement a empty heap data structure
    def __init__(self):
        self.q = [None] # pad it with one element
    
    # Function: insert
    # Insert a vertex v of type Vertex into the queue.
    # Remember to set the field `idx_in_priority_queue` and
    # keep updating it.
    def insert(self, v):
        n = len(self.q)
        self.q.append(v)
        v.idx_in_priority_queue = n
        self.bubble_up(n)
        # self.check_invariant()
        
    # Function: swap two elements in the priority queue.
    # Remember to swap the vertices at positions i and j
    # But also remember to update the positions of the vertices in the
    # priority queue.
    # You can use this to implement bubble_up and bubble_down
    def swap(self, i, j):
        tmp = self.q[i]
        self.q[i] = self.q[j]
        self.q[i].idx_in_priority_queue = i
        self.q[j] = tmp
        self.q[j].idx_in_priority_queue = j
        
    # Function: bubble_up
    # bubble up an element j
    # until min heap property is restored.
    def bubble_up(self, j):
        assert j >= 1
        assert j < len(self.q)
        if j == 1:
            return
        val = self.q[j].d
        parent_idx = j // 2
        parent_val = self.q[parent_idx].d
        if val < parent_val:
            self.swap(j, parent_idx)
            self.bubble_up(parent_idx)
        return
    
    # Function: bubble_down
    # Bubble down an element j until
    # min heap property is restored.
    def bubble_down(self, j):
        n = len(self.q)
        left_child_idx = 2 * j
        right_child_idx = 2 * j + 1
        if left_child_idx >= n:
            return
        if right_child_idx >= n:
            child_idx = left_child_idx
            child_d = self.q[left_child_idx].d
        else:
            (child_d, child_idx) = min ( (self.q[left_child_idx].d, left_child_idx), 
                                         (self.q[right_child_idx].d, right_child_idx)
                                       )
        if self.q[j].d > child_d:
            self.swap(j, child_idx)
            self.bubble_down(child_idx)
        return 
        
    # Function: get_and_delete_min
    # Find the minimum weight vertex and delete it from the heap.
    # return the deleted vertex back
    def get_and_delete_min(self):
        n = len(self.q)
        assert n > 1
        v = self.q[1]
        if n > 2: 
            self.q[1] = self.q[n-1]
            self.q[n-1].idx_in_priority_queue = 1
            del self.q[n-1]
            self.bubble_down(1)
        #self.check_invariant()
        return v
    
    # Is the heap empty?
    def is_empty(self):
        return len(self.q) == 1
    
    # This is a useful function since in Dijkstra
    # the weight of a vertex updates on the fly.
    # We will need to call this to update the vertex weight.
    def update_vertex_weight(self, v):
        j = v.idx_in_priority_queue
        n = len(self.q)
        assert j >= 0 and j < n
        self.bubble_down(j)
        self.bubble_up(j)
        # self.check_invariant()

class DummyGraphClass:
    def __init__(self, adj_list, verts):
        self.verts=verts
        self.adj_list = adj_list
                
    def get_vertex_from_coords(self, i, j):
        assert (i,j) in self.verts
        return self.verts[(i,j)]
    
    def get_list_of_neighbors(self, vert):
        coords = (vert.x, vert.y)
        if coords in self.adj_list:
            return self.adj_list[(vert.x, vert.y)]
        else:
            return []

verts = {(i,j): Vertex(i,j) for i in range(3) for j in range(3)}

adj_list= {}

def connect_nodes(src, dest, weight):
    v1 = src
    v2 = verts[dest]
    if v1 in adj_list:
        adj_list[v1].append((v2, weight))
    else:
        adj_list[v1] = [(v2, weight)]
# Let's build a graph
connect_nodes((0,0),(0,1),1.0)
connect_nodes((0,0),(1,0),0.5)
connect_nodes((1,0),(0,1), 0.5)
connect_nodes((0,1),(0,0), 0.5)
connect_nodes((1,0),(1,1), 0.5)
connect_nodes((1,1), (2,2), 0.25)
connect_nodes((1,1),(1,2), 0.5)
connect_nodes((1,1),(2,1), 1.2)
connect_nodes((2,1), (2,2), 0.25)
connect_nodes((1,2), (2,2), 0.25)

graph = DummyGraphClass(adj_list, verts)

for element in graph.verts:
    print(f'virt = {element}')
print("")

print("----------------------------------------")
print(f'type of graph.adj_list = {type(graph.adj_list)}')
print(graph.adj_list.keys())
for key in graph.adj_list.keys():
    temp_list = graph.adj_list.get(key)
    print(f'\n--type of temp = {type(temp_list)}')
    print(f'--len of temp_list is {len(temp_list)}')
    print(f'--key = {key}')

    for tuple in temp_list:
        print(f'------type = {type(element)}')
        print(f'------tuple[0].x = {tuple[0].x}')
        print(f'------tuple[0].y = {tuple[0].y}')
        print(f'------tuple[0].d = {tuple[0].d}')
        print(f'------tuple[0].processed = {tuple[0].processed}')
        print(f'------tuple[0].idx_in_priority_queue = {tuple[0].idx_in_priority_queue}')
        print(f'------tuple[0].pi (parent) = {tuple[0].pi}')
        print(f'------tuple[1] (weight) = {tuple[1]}')
        print(f'------')

"""
virt = (0, 0)
virt = (0, 1)
virt = (0, 2)
virt = (1, 0)
virt = (1, 1)
virt = (1, 2)
virt = (2, 0)
virt = (2, 1)
virt = (2, 2)

----------------------------------------
type of graph.adj_list = <class 'dict'> 
dict_keys([(0, 0), (1, 0), (0, 1), (1, 1), (2, 1), (1, 2)])

--type of temp = <class 'list'>
--len of temp_list is 2
--key = (0, 0)
------type = <class 'tuple'>
------tuple[0].x = 0
------tuple[0].y = 1
------tuple[0].d = inf
------tuple[0].processed = False
------tuple[0].idx_in_priority_queue = -1
------tuple[0].pi (parent) = None
------tuple[1] (weight) = 1.0
------
------type = <class 'tuple'>
------tuple[0].x = 1
------tuple[0].y = 0
------tuple[0].d = inf
------tuple[0].processed = False
------tuple[0].idx_in_priority_queue = -1
------tuple[0].pi (parent) = None
------tuple[1] (weight) = 0.5
------

--type of temp = <class 'list'>
--len of temp_list is 2
--key = (1, 0)
------type = <class 'tuple'>
------tuple[0].x = 0
------tuple[0].y = 1
------tuple[0].d = inf
------tuple[0].processed = False
------tuple[0].idx_in_priority_queue = -1
------tuple[0].pi (parent) = None
------tuple[1] (weight) = 0.5
------
------type = <class 'tuple'>
------tuple[0].x = 1
------tuple[0].y = 1
------tuple[0].d = inf
------tuple[0].processed = False
------tuple[0].idx_in_priority_queue = -1
------tuple[0].pi (parent) = None
------tuple[1] (weight) = 0.5
------

--type of temp = <class 'list'>
--len of temp_list is 1
--key = (0, 1)
------type = <class 'tuple'>
------tuple[0].x = 0
------tuple[0].y = 0
------tuple[0].d = inf
------tuple[0].processed = False
------tuple[0].idx_in_priority_queue = -1
------tuple[0].pi (parent) = None
------tuple[1] (weight) = 0.5
------

--type of temp = <class 'list'>
--len of temp_list is 3
--key = (1, 1)
------type = <class 'tuple'>
------tuple[0].x = 2
------tuple[0].y = 2
------tuple[0].d = inf
------tuple[0].processed = False
------tuple[0].idx_in_priority_queue = -1
------tuple[0].pi (parent) = None
------tuple[1] (weight) = 0.25
------
------type = <class 'tuple'>
------tuple[0].x = 1
------tuple[0].y = 2
------tuple[0].d = inf
------tuple[0].processed = False
------tuple[0].idx_in_priority_queue = -1
------tuple[0].pi (parent) = None
------tuple[1] (weight) = 0.5
------
------type = <class 'tuple'>
------tuple[0].x = 2
------tuple[0].y = 1
------tuple[0].d = inf
------tuple[0].processed = False
------tuple[0].idx_in_priority_queue = -1
------tuple[0].pi (parent) = None
------tuple[1] (weight) = 1.2
------

--type of temp = <class 'list'>
--len of temp_list is 1
--key = (2, 1)
------type = <class 'tuple'>
------tuple[0].x = 2
------tuple[0].y = 2
------tuple[0].d = inf
------tuple[0].processed = False
------tuple[0].idx_in_priority_queue = -1
------tuple[0].pi (parent) = None
------tuple[1] (weight) = 0.25
------

--type of temp = <class 'list'>
--len of temp_list is 1
--key = (1, 2)
------type = <class 'tuple'>
------tuple[0].x = 2
------tuple[0].y = 2
------tuple[0].d = inf
------tuple[0].processed = False
------tuple[0].idx_in_priority_queue = -1
------tuple[0].pi (parent) = None
------tuple[1] (weight) = 0.25
------
"""