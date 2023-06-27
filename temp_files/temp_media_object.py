class MedianMaintainingHeap:
    def __init__(self):
        self.hmin = MinHeap()
        self.hmax = MaxHeap()
        
    def satisfies_assertions(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0
            return 
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1
            return 
        # 1. min heap min element >= max heap max element
        assert self.hmax.max_element() <= self.hmin.min_element(), f'Failed: Max element of max heap = {self.hmax.max_element()} > min element of min heap {self.hmin.min_element()}'
        # 2. size of max heap must be equal or one lessthan min heap.
        s_min = self.hmin.size()
        s_max = self.hmax.size()
        assert (s_min == s_max or s_max  == s_min -1 ), f'Heap sizes are unbalanced. Min heap size = {s_min} and Maxheap size = {s_max}'
    
    def __repr__(self):
        return 'Maxheap:' + str(self.hmax) + ' Minheap:'+str(self.hmin)
    
    def get_median(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0, 'Sizes are not balanced'
            assert False, 'Cannot ask for median from empty heaps'
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1, 'Sizes are not balanced'
            return self.hmin.min_element()
        # your code here
#
# ============================================================================
print('Inserting 1')
# odd, size = 1
# min_heap = [1]
# max_heap = []
# [ [] [1]  ]

# (n - 1)/2th element
# (1-1)/2th elment
# (0)  /2th element

median = 1

print('Inserting 1, 5')
# even, size = 2
# min_heap = [1]
# max_heap = [5]
# modify to meet the rules
# min_heap = [5]
# max_heap = [1]

# [ min_heap max_heap ]
# [ [1] [5] ]

# ( (n/2 -1) element + (n/2) element) / 2
# ( (1 -1) element + (2/2) element) / 2
# (0th element + 1th element) / 2
# (1 + 5)/2 = 3
median = 3


# The data will be maintained as the union of the elements in two heaps $H_{\min}$ and $H_{\max}$, wherein $H_{\min}$ is a min-heap and $H_{\max}$ is a max-heap.  We will maintain the following invariant:
#  - The max element of  $H_{\max}$ will be less than or equal to the min element of  $H_{\min}$. 
#  - The sizes of $H_{max}$ and $H_{min}$ are equal (if number of elements in the data structure is even) or $H_{max}$ may have one less element than $H_{min}$ (if the number of elements in the data structure is odd).
  
print('Inserting 1, 5, 2')
# odd, size = 3
# before insert 
# min_heap = [5], min elment = 5
# max_heap = [1], max element = 1

# after  insert
# min_heap = [2,5], min elment = 2
# max_heap = [1], max element = 1

# [ min_heap max_heap ]
# [ [2,5] [1] ]

# (n-1) / 2th element
# (3-1) / 2th element
# 2 / 2th element
# 2 / 1 = 2
median = 2










print('Inserting 1, 5, 2, 4')
# even, size = 4
# before insert 
# min_heap = [2,5], min elment = 2
# max_heap = [1], max element = 1

# afer insert 4
# min_heap = [2,5], min elment = 2
# max_heap = [1,4], max element = 4

# after fixing max_heap
# min_heap = [2,5], min elment = 2
# max_heap = [4,1], max element = 4

# after modify to fit rules
# min_heap = [4,5], min elment = 4
# max_heap = [2,1], max element = 2

# [ min_heap max_heap ]
# [ [4,5] [2,1] ]

# ( (n/2 -1) element + (n/2) element) / 2
# ( (4/2 -1) element + (4/2) element) / 2
# ( 1st element      + 2th element )  / 2
# ( 5                + 2 ) / 2 = 7    / 2 = 3
# ??????????? should be 3.5, not 3??????????????????????????????????
median = 3















print('Inserting 1, 5, 2, 4, 18')
# odd, size = 5

# before insert
# min_heap = [4,5], min elment = 4
# max_heap = [2,1], max element = 2

# after insert
# min_heap = [4,5,18], min elment = 4
# max_heap = [2,1], max element = 2

# after insterting, fixing heaping and modify to fit rules
# min_heap = [4,5,18], min elment = 4
# max_heap = [2,1], max element = 2

# [ min_heap max_heap]
# [ [4,5,18] [2,1]  ]

# (n-1) / 2th element
# (5-1) / 1 
# 4     / 1 = 4
median = 4


















print('Inserting 1, 5, 2, 4, 18, -4')
# even, size = 6

# before insert
# min_heap = [4,5,18], min elment = 4
# max_heap = [2,1], max element = 2

# after insert
# min_heap = [4,5,18], min elment = 4
# max_heap = [2,1], max element = 2

# min_heap = [4,5,18], min elment = 4
# max_heap = [2,1,-4], max element = 2

# after fixing heaps, and modify to fit rules
# min_heap = [4,5,18], min elment = 4
# max_heap = [2,1,-4], max element = 2

# [ min_heap max_heap ]
# [ [4,5,18] [2,1,-4] ]

# ( (n/2 -1) element + (n/2) element) / 2
# ( (6/2 -1) element + (6/2) element) / 2
# ( (3   -1) element + (3)   element) / 2
# ( 2th element      + 3rd element)   / 2
#?????????????????????????????????????????????
# (1 + -4) /2 = 3
median = 3





















print('Inserting 1, 5, 2, 4, 18, -4, 7')
# odd, size = 7

# before insert
# min_heap = [4,5,18], min elment = 4
# max_heap = [2,1,-4], max element = 2

# after insert
# min_heap = [4,5,18,7], min elment = 4
# max_heap = [2,1,-4], max element = 2

# after fixing heap, verify it meets the rule
# min_heap = [4,5,18,7], min elment = 4
# max_heap = [2,1,-4], max element = 2

# [ min_heap max_heap ]
# [ [4,5,18,7] [2,1,-4] ]

# ??????????????????????????????????????????
# (n-1) / 2th element
# (7-1) / 1 
# 6     / 1 = 7 
median = 4


















##??????????????????????????????????
print('Inserting 1, 5, 2, 4, 18, -4, 7, 9')
# even, size = 8

# before insert

# min_heap = [4,5,18,7], min elment = 4
# max_heap = [2,1,-4], max element = 2

# after insert

# min_heap = [4,5,18,7], min elment = 4
# max_heap = [2,1,-4,9], max element = 2

# after fixing max_heap
# min_heap = [4,5,18,7], min elment = 4
# max_heap = [2,9,-4,1], max element = __

# after fixing max_heap
# min_heap = [4,5,18,7], min elment = 4
# max_heap = [9,2,-4,1], max element = 9

# after fixing max_heap
# min_heap = [4,5,18,7,9], min elment = 4
# max_heap = [2,-4,1], max element = 9

# [ mean_heap max_heap ]
# [ [4,5,18,7,9] [2,-4,1] ]

# ( (n/2 -1) element + (n/2) element) / 2
# ( (8/2 -1) element + (8/2) element) / 2
# ( (4   -1) element + (4th) element) / 2
# ( 3th element + 4th element) / 2
# ??????????????????????????????????????????????????
# (7 + 9) / 2 = 8.0
median = 4.5























