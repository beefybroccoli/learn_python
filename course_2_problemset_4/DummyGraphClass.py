from Vertex import *

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
    

"""
graph.verts - <class 'tuple'>,(0, 0)
graph.verts - <class 'tuple'>,(0, 1)
graph.verts - <class 'tuple'>,(0, 2)
graph.verts - <class 'tuple'>,(1, 0)
graph.verts - <class 'tuple'>,(1, 1)
graph.verts - <class 'tuple'>,(1, 2)
graph.verts - <class 'tuple'>,(2, 0)
graph.verts - <class 'tuple'>,(2, 1)
graph.verts - <class 'tuple'>,(2, 2)
debug ----
graph.adj_list <class 'tuple'>,(0, 0)
graph.adj_list <class 'tuple'>,(1, 0)
graph.adj_list <class 'tuple'>,(0, 1)
graph.adj_list <class 'tuple'>,(1, 1)
graph.adj_list <class 'tuple'>,(2, 1)
graph.adj_list <class 'tuple'>,(1, 2)
"""