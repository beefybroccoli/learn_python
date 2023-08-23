class TreeNode:
    # Constructor for tree nodde
    def __init__(self, key, parent_node=None):
        self.key = key # set the key
        self.parent = parent_node # set the parent_node
        self.left = None # set the left child to None -- no left child to begin with
        self.right = None # set the right child to None - no right child to begin with.
    
    def is_root(self):
        return parent_node == None
    
    # Function: insert
    # insert a node with key `new_key` into the current tree.
    def insert(self, new_key):
        key = self.key 
        if new_key == key:
            print(f'Already inserted key {key}. Ignoring')
        elif new_key < key: # new_key must go into the left subtree
            if self.left == None: # no left child?
                new_node = TreeNode(new_key, self) # create one with self as parent
                self.left = new_node # set the left pointer
            else:
                self.left.insert(new_key) # recursively call insert on left subtree
        else:  # new_key must go into the right subtree.
            assert new_key > key
            if self.right == None: # no right child?
                new_node = TreeNode(new_key, self) # create one
                self.right = new_node
            else: 
                self.right.insert(new_key) # recusively call insert on right subtree.