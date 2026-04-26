# Sorts inputfile via repeated inserts into a binary search tree followed by an inorder tree walk. 

import sys
from DictBinTree import DictBinTree

dict = DictBinTree() # Creates empty tree

# Insert values in input files into dict
n = 0
for line in sys.stdin:
    dict.insert(int(line))
    n = n+1

print(dict.orderedTraversal()) # Print the ordered traversal to the output