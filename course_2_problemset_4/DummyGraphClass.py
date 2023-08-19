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