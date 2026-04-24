import sys
from DictBinTree import DictBinTree

dict = DictBinTree()

n = 0
for line in sys.stdin:
    dict.insert(int(line))
    n = n+1

print(dict.orderedTraversal(dict.root))