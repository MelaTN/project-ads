import sys
from DictBinTree import DictBinTree

dict = DictBinTree()

n = 0
for line in sys.stdin:
    dict.insert(int(line))
    n = n+1

def test_search(keys:list):
    for k in keys:
        if dict.search(k) is not None:
            print(dict.search(k).key)
        else:
            print("Not found")

def test_insert():
    
    t = DictBinTree()
    
    t.insert(5)
    t.insert(3)
    t.insert(7)

    assert t.search(5) is not None
    assert t.search(10) is None
    
    t.insert(5)
    print(t.orderedTraversal())

    
def test_orderedTraversal():
    print(dict.orderedTraversal())

    
# test_search([1,5,10])

test_insert()
test_orderedTraversal()




