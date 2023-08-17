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
        print(f'------tuple[0].pi = {tuple[0].pi}')
        print(f'------tuple[1] = {tuple[1]}')
        print(f'------')

"""
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
    ------tuple[0].pi = None
    ------tuple[1] = 1.0 (weight)
    ------
    ------type = <class 'tuple'>
    ------tuple[0].x = 1
    ------tuple[0].y = 0
    ------tuple[0].d = inf
    ------tuple[0].processed = False
    ------tuple[0].idx_in_priority_queue = -1
    ------tuple[0].pi = None
    ------tuple[1] = 0.5 (weight)
    ------
"""