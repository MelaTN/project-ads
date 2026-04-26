## PROJECT DEL 2 ##
## Af Lasse Banke Rasmussen (lrasm24@student.sdu.dk) og Melanie Toudahl Nielsen (melni24@student.sdu.dk) ##

## Class BinNode ##

class BinNode:
    """"
    Node in binary search tree.
    Attributes: float key, BinNode left (left child), BinNode right (right child).
    """
    def __init__(self, key: float, left: "BinNode" = None, right: "BinNode" = None):
        self.key = key
        self.left = left   
        self.right = right

## Class DictBinTree ##

class DictBinTree:
    """
    Binary search tree
    Attributes: Binary node root (the root of the tree)
    Methods: search (for finding a given key), insert (for inserting a given key) 
    and orderedTraversal (for performing an inorder tree walk)

    """
    def __init__(self, root: BinNode = None):
        self.root = root

    ## Tree search ##

    def search(self, k: float) -> BinNode:
        "Returns a pointer to a node with key k if such a node exists in the binary search tree."
        return self._search(self.root, k)

    def _search(self, x: BinNode, k: float) -> BinNode:
        "Performs recursive step in tree search starting at node x."
        
        # Terminate if x is a leaf (in which case the whole tree was searched and the key was not found)
        # or if the key is found.
        if x == None or k == x.key: 
            return x
        
        # Else, continue looking either in the left or right subtree of x depending on whether 
        # key in x is less than or greater than k respectively. 
        if k < x.key:
            return self._search(x.left,k)
        else:
            return self._search(x.right,k)
        
    ## Insert ##

    def insert(self, k: float) -> None:
        "Inserts node with key k into the binary search tree."
        
        x = self.root # Will be the pointer to candidate note to replace with the new one
        y = None # Will be the ponter to the parent of x
        while x != None:
            y = x
            if k < x.key:
                x = x.left
            else:
                x = x.right
        
        # Now, x is points to the leaf where we will place the new node.  
        # In order to change the tree strucutre, we change the child of y that x is pointing to.

        if y == None:
            self.root = BinNode(k) # Tree was empty
        elif k < y.key:
            y.left = BinNode(k)
        else:
            y.right = BinNode(k)
        
    ## Inorder tree walk ##

    def orderedTraversal(self) -> list:
        "Returns a sorted list of the keys in the binary search tree."
        return self._orderedTraversal(self.root,[])

    def _orderedTraversal(self, x: BinNode, keys: list) -> list:
        "Performs recursive step in inorder walk starting at node x."
        if x != None:
            self._orderedTraversal(x.left, keys) # keys now contains ordered list of keys in the left subtree 
            keys.append(x.key) # append the key in x to keys
            self._orderedTraversal(x.right, keys) # Extends keys with the sorted keys in the right subtree
        return keys
    
## Tests ##

def _test():
    "Runs a basic module of tests of the methods for the class DictBinTree."
    # Empty tree
    t = DictBinTree()
    assert t.search(5) == None
    assert t.orderedTraversal() == []
    t.insert(5)
    assert t.root.key == 5 # Checks if 5 is indeed inserted as the root

    # Test of insert
    t.insert(7)
    t.insert(2)
    assert t.root.left.key == 2
    assert t.root.right.key == 7 

    t.insert(5) # Duplicates
    assert t.root.right.left.key == 5 

    # Test of search
    assert t.search(1) == None # Non-existent keys
    assert t.search(5) != None # Existent keys

    # Test of inorder walk
    assert t.orderedTraversal() == [2,5,5,7]
    
if __name__ == "__main__":
    _test()




