class DisjointForests:
    def __init__(self, n):
        assert n >= 1, ' Empty disjoint forest is disallowed'
        self.n = n
        self.parents = [None]*n
        self.rank = [None]*n
        
    # Function: dictionary_of_sets
    # Convert the disjoint forest structure into a dictionary d
    # wherein d has an entry for each representative i
    # d[i] maps to each elements which belongs to the tree corresponding to i
    # in the disjoint forest.
    def dictionary_of_sets(self):
        d = {}
        for i in range(self.n):
            if self.is_representative(i):
                d[i] = set([i])
        for j in range(self.n):
            if self.parents[j] != None:
                root = self.find(j)
                assert root in d
                d[root].add(j)
        return d
    
    def make_set(self, j):
        assert 0 <= j < self.n
        assert self.parents[j] == None, 'You are calling make_set on an element multiple times -- not allowed.'
        self.parents[j] = j
        self.rank[j] = 1
        
    def is_representative(self, j):
        return self.parents[j] == j 
    
    def get_rank(self, j):
        return self.rank[j]
    
    # Function: find
    # Implement the find algorithm for a node j in the set.
    # Repeatedly traverse the parent pointer until we reach a root.
    # Implement the "rank compression" strategy by making all 
    # nodes along path from j to the root point directly to the root.
    def find(self, j):
        assert 0 <= j < self.n
        # assert self.parents[j] != None, 'You are calling find on an element that is not part of the family yet. Please call make_set first.'
        # your code here
        # -------------------- traverse until the parent node is found----------------------
        # if the element does not exist
        #   call makeset
        if self.parents[j] == None or self.rank[j] == None:
            self.make_set(j)
            return self.parents[j]
        #   base case for recursion
        elif self.parents[j] == j:
            return self.parents[j]
        #   find(self, value) again until reach root node
        return self.find(self.parents[j])
    
    # Function : union
    # Compute union of j1 and j2
    # First do a find to get to the representatives of j1 and j2.
    # If they are not the same, then 
    #  implement union using the rank strategy I.e, lower rank root becomes child of the higher ranked root.
    #  break ties by making the first argument j1's root the parent.
    def union(self, j1, j2):
        assert 0 <= j1 < self.n
        assert 0 <= j2 < self.n
        assert self.parents[j1] != None
        assert self.parents[j2] != None
        # your code here
        # --------------------
        if self.rank[j1] >= self.rank[j2]:
            # increse (new) parent rank by one
            self.rank[j1] = self.rank[j2] + 1
            # change (new) child's parent to new parent
            self.parents[j2] = self.parents[j1]
        else:
            # increse (new) parent rank by one
            self.rank[j2] = self.rank[j1] + 1
            # change (new) child's parent to new parent
            self.parents[j1] = self.parents[j2]

# ===================================================================
# =================================================================
print("-----------------------Problem 1-----------------------------------")
d = DisjointForests(10)
for i in range(3,10,1):
    d.make_set(i)

# for i in range(10):
#     print(f'd.parents[{i}] = {d.parents[i]}, d.rank[{i}] = {d.rank[i]}')


for i in range(10):
    assert d.find(i) == i, f'Failed: Find on {i} must return {i} back'

d.union(0,1)
d.union(2,3)
assert(d.find(0) == d.find(1)), '0 and 1 have been union-ed together'
assert(d.find(2) == d.find(3)), '2 and 3 have been union-ed together'
assert(d.find(0) != d.find(3)), '0 and 3 should be in  different trees'
assert((d.get_rank(0) == 2 and d.get_rank(1) == 1) or 
       (d.get_rank(1) == 2 and d.get_rank(0) == 1)), 'one of the nodes 0 or 1 must have rank 2'

assert((d.get_rank(2) == 2 and d.get_rank(3) == 1) or 
       (d.get_rank(3) == 2 and d.get_rank(2) == 1)), 'one of the nodes 2 or 3 must have rank 2'

d.union(3,4)
assert(d.find(2) == d.find(4)), '2 and 4 must be in the same set in the family.'

d.union(5,7)
d.union(6,8)
d.union(3,7)
d.union(0,6)

assert(d.find(6) == d.find(1)), '1 and 6 must be in the same set in the family'
assert(d.find(7) == d.find(4)), '7 and 4 must be in the same set in the family'
assert(d.find(8) == 0), 'parent is 0'

for i in range(10):
    print(f'd.parents[{i}] = {d.parents[i]}, d.rank[{i}] = {d.rank[i]}')

print(f'd.dictionary_of_sets() return {d.dictionary_of_sets()}')

print('All tests passed: 10 points.')

print("-----------------------Problem 2A-----------------------------------")

    
class UndirectedGraph:
    
    # n is the number of vertices
    # we will label the vertices from 0 to self.n -1 
    # We simply store the edges in a list.
    def __init__(self, n):
        assert n >= 1, 'You are creating an empty graph -- disallowed'
        self.n = n
        self.edges = []
        self.vertex_data = [None]*self.n
       
    def set_vertex_data(self, j, data):
        assert 0 <= j < self.n
        self.vertex_data[j] = data
        
    def get_vertex_data(self, j):
        assert 0 <= j < self.n
        return self.vertex_data[j] 
        
    def add_edge(self, i, j, wij):
        assert 0 <= i < self.n
        assert 0 <= j < self.n
        assert i != j
        # Make sure to add edge from i to j with weight wij
        self.edges.append((i, j, wij))
        
    def sort_edges(self):
        # sort edges in ascending order of weights.
        self.edges = sorted(self.edges, key=lambda edg_data: edg_data[2])

## 2A: Use union-find data-structures to compute strongly connected components.
"""
We have previously seen  how to use DFS to find maximal strongly connected components with a small twist.

  - We will consider only those edges $(i,j)$ whose weights are less than or equal to a threshold $W$ provided by the user.
  - Edges with weights above this threshold are not considered.
  
Design an algorithm to compute all the maximal strongly connected components for all edges with threshold $W$ using the union-find data structure. What is the running time of your algorithm. Note that this is manually graded answer : you can compare your solution against our solution provided at the end of this assignment.
"""

def compute_scc(g, W):
    # create a disjoint forest with as many elements as number of vertices
    # Next compute the strongly connected components using the disjoint forest data structure
    d = DisjointForests(g.n)
    # your code here
    # ---------------------
    # for edge in g.edges:
    #     if edge[2] <= W:
    #         print(f'edge = {edge}')

    for index in range(g.n):
        # print(f'g.edges[{index}] = {g.edges[index]}')
        d.make_set(index)
        # print(f'd.parents[{index}] = {d.parents[index]}, d.rank[{index}] = {d.rank[index]}')
    
    for edge in g.edges:
        if edge[2] <= W:
            # print(f'edge = {edge}')
            d.union(edge[0], edge[1])
            index_0 = edge[0]
            index_1 = edge[1]
            # print(f'd.parents[{index_0}] = {d.parents[index_0]}, d.rank[{index_0}] = {d.rank[index_0]}')
            # print(f'd.parents[{index_1}] = {d.parents[index_1]}, d.rank[{index_1}] = {d.rank[index_1]}')

    # print(f'd.dictionary_of_sets return {d.dictionary_of_sets()}')
    return d.dictionary_of_sets()

    # extract a set of sets from d
    # return d.dictionary_of_sets()
    pass

g3 = UndirectedGraph(8)
g3.add_edge(0,1,0.5)
g3.add_edge(0,2,1.0)
g3.add_edge(0,4,0.5)
g3.add_edge(2,3,1.5)
g3.add_edge(2,4,2.0)
g3.add_edge(3,4,1.5)
g3.add_edge(5,6,2.0)
g3.add_edge(5,7,2.0)

res = compute_scc(g3, 2.0)
print('SCCs with threshold 2.0 computed by your code are:')
assert len(res) == 2, f'Expected 2 SCCs but got {len(res)}'
for (k, s) in res.items():
    print(s)

# Let us check that your code returns what we expect.
for (k, s) in res.items():
    if (k in [0,1,2,3,4]):
        assert (s == set([0,1,2,3,4])), '{0,1,2,3,4} should be an SCC'
    if (k in [5,6,7]):
        assert (s == set([5,6,7])), '{5,6,7} should be an SCC'


# Let us check that the thresholding works
print('SCCs with threshold 1.5')
res2 = compute_scc(g3, 1.5) # This cutsoff edges 2,4 and 5, 6, 7
for (k, s) in res2.items():
    print(s)
assert len(res2) == 4, f'Expected 4 SCCs but got {len(res2)}'

for (k, s) in res2.items():
    if k in [0,1,2,3,4]:
        assert (s == set([0,1,2,3,4])), '{0,1,2,3,4} should be an SCC'
    if k in [5]:
        assert s == set([5]), '{5} should be an SCC with just a single node.'
    if k in [6]:
        assert s == set([6]), '{6} should be an SCC with just a single node.'
    if k in [7]:
        assert s == set([7]), '{7} should be an SCC with just a single node.'
        
print('All tests passed: 10 points')


print("-----------------------Problem 2B-----------------------------------")
"""
Problem 2B Compute Minimum Spanning Tree 

We will now compute the MST of a given undirected weighted graph using Kruskal's algorithm. 
Complete the code below that uses a disjoint set forest data structure for implementing Kruskal's algorithm.

You code simply returns a list of edges with edge weights  as a tuple $(i,j, wij)$ that are part of the MST along with the total weight of the MST.
"""

def compute_mst(g):
    # return a tuple of two items
    #   1. list of edges (i,j) that are part of the MST
    #   2. sum of MST edge weights.
    d = DisjointForests(g.n)
    mst_edges = []
    g.sort_edges()
    # your code here
    # ------------------
    # make set first
    for index in range(g.n):
        d.make_set(index)
    
    # loop through the sorted edges
    for edge in g.edges:

    #   if - test if this new edge will create a cycle in the tree
        if d.find(edge[0]) != d.find(edge[1]):
            
            # add this edge into the tree
            d.union(edge[0], edge[1])
            
            # add edge to mst_edges
            mst_edges.append(edge)

    #   else - set this edge aside, maybe insert into backedge log?

    # return (mst_edges, mst_weight)

    return (mst_edges, sum([edge[2] for edge in mst_edges]) )

# ------------------------------------------------------------------

g3 = UndirectedGraph(8)
g3.add_edge(0,1,0.5)
g3.add_edge(0,2,1.0)
g3.add_edge(0,4,0.5)
g3.add_edge(2,3,1.5)
g3.add_edge(2,4,2.0)
g3.add_edge(3,4,1.5)
g3.add_edge(5,6,2.0)
g3.add_edge(5,7,2.0)
g3.add_edge(3,5,2.0)

(mst_edges, mst_weight) = compute_mst(g3)
print('Your code computed MST: ')
for (i,j,wij) in mst_edges:
    print(f'\t {(i,j)} weight {wij}')
print(f'Total edge weight: {mst_weight}')

assert mst_weight == 9.5, 'Optimal MST weight is expected to be 9.5'

assert (0,1,0.5) in mst_edges
assert (0,2,1.0) in mst_edges
assert (0,4,0.5) in mst_edges
assert (5,6,2.0) in mst_edges
assert (5,7,2.0) in mst_edges
assert (3,5,2.0) in mst_edges
assert (2,3, 1.5) in mst_edges or (3,4, 1.5) in mst_edges

print('All tests passed: 10 points!')


print("-----------------------Problem 2C-----------------------------------")
"""

"""