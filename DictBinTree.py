class BinNode:
    def __init__(self, key: float, left = None, right = None):
        self.key = key
        self.left = left   
        self.right = right

class DictBinTree:
    def __init__(self, root: BinNode = None):
        self.root = root

    ## Tree search ##

    def search(self, k):
        "Returns a pointer to a node with key k if such a node exists."
        return self._search(self.root, k)

    def _search(self, x, k): 
        "Performs recursive step in tree search starting at node x."
        if x == None or k == x.key:
            return x
        if k < x.key:
            return self.search(x.left,k)
        else:
            return self.search(x.right,k)
        
    ## Insert ##

    def insert(self, k):
        "Inserts node with key key into the binary search tree."
        x = self.root
        y = None 
        while x != None:
            y = x
            if k < x.key:
                x = x.left
            else:
                x = x.right
        
        # Now, x is poiting to a None and y is poiting to the 
        # parent of this leaf. In order to replace the value None in the
        # tree structure we need to change that child of y.

        if y == None:
            self.root = BinNode(k) # Tree was empty
        elif k < y.key:
            y.left = BinNode(k)
        else:
            y.right = BinNode(k)
        
    ## Inorder tree walk ##

    def orderedTraversal(self, k):
        "Returns a sorted list of the keys in the binary search tree."
        return self._orderedTraversal(self.root, [], k)

    def _orderedTraversal(self, x, l, k):
        "Returns an ordered list of the keys in the binary subtree with root x."       
        l.append(self.orderedTraversal(x.left, k))
        l.append(x.key)
        l.append(self.orderedTraversal(x.right, k))

        return l
    