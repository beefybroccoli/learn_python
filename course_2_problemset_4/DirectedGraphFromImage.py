import math 
def fixPixelValues(px):
    # convert the RGB values into floating point to avoid an overflow that will give me wrong answers
    return [ float(px[0]), float(px[1]), float(px[2]) ]   

class DirectedGraphFromImage:
    def __init__(self, img):
        self.img = img
        self.coords2vertex = {} # construct a dictionary that maps coordinates [(i,j)] to corresponding vertices in graph
    
        
    def get_vertex_from_coords(self, i, j):
        if (i,j) in self.coords2vertex: # is pixel (i,j) already there? 
            return self.coords2vertex[(i,j)] # if yes, just return the vertex corresponding
        v = Vertex(i, j)
        self.coords2vertex[(i,j)] = v
        return v
    
    ## Given (x,y) coordinates of two neighboring pixels, calculate the edge weight.
    # We take the squared euclidean distance between the pixel values and add 0.1
    def getEdgeWeight(self, u, v):
        img = self.img
        # get edge weight for edge between u, v
        i0,j0 = u.x, u.y
        i1,j1 = v.x, v.y
        height, width, _ = img.shape
        # First make sure that the edge is legit
        # Edges can only go from each pixel to neighboring pixel
        assert i0 >= 0 and j0 >= 0 and i0 < width and j0 < height # pixel position valid?
        assert i1 >= 0 and j1 >= 0 and i1 < width and j1 < height # pixel position valid?
        assert -1 <= i0 - i1 <= 1 # edge between node and neighbor?
        assert -1 <= j0 - j1 <= 1
        px1 = fixPixelValues(img[j0,i0])
        px2 = fixPixelValues(img[j1,i1])
        return 0.1 + (px1[0] - px2[0])**2 + (px1[1] - px2[1])**2 + (px1[2]- px2[2])**2

    # Function: get_list_of_neighbors
    # Given a vertex in the graph, get its list of neighbors
    #  I.e, for given vertex `vert` return a list [(v1, w1), (v2, w2),..,(vk,wk)]
    #  Such that vert has an edge to v1 with weight w1, edge to v2 with weight w2 and ... 
    #   edge to vk with weight wk
    # Note that rather than build an adjacency list up front, we simply call this function
    # to get the neighbors of a vertex.
    def get_list_of_neighbors(self, vert):
        img = self.img
        i = vert.x
        j = vert.y
        height, width, _ = img.shape
        lst = []
        if i > 0:
             # Get the adjacent vertex directly to the WEST
            # What is the weight of the edge from pixel (i,j) to (i-1,j)
            v0 = self.get_vertex_from_coords(i-1, j)
            w0 = self.getEdgeWeight(vert, v0)
            # Append the adjacent vertex and its weight.
            lst.append((v0, w0))
        if j > 0:
            # Get the adjacent vertex directly to the SOUTH
            v1 = self.get_vertex_from_coords(i, j-1)
            w1 = self.getEdgeWeight(vert, v1)
            # Append the adjacent vertex and its weight.
            lst.append((v1, w1))    
        if i < width-1:
            # EAST
            v2 = self.get_vertex_from_coords(i+1, j)
            w2 = self.getEdgeWeight( vert, v2)
            lst.append((v2, w2))
        if j < height-1:
            # NORTH
            v3 = self.get_vertex_from_coords(i, j+1)
            w3 = self.getEdgeWeight(vert, v3)
            lst.append((v3, w3))
        return lst