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
        