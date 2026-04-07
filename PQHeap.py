def createEmptyPQ():
    "Returns an empty heap"
    return []

## extractMin and minHeapify ##

def extractMin(A):
    "Returns and removes the minimum of the min-priority-queue A. "
    "Assumed that A is non-empty. " 

    min = A[0] # Safes the min (root)
    if len(A)>1:
        A[0] = A.pop() # Replaces root with the last leave
        minHeapify(A,0) # Restores heap-order
   
    return min

def minHeapify(A,i):
    "Restores heap-order under the assumption that the subtrees of node i are min-heaps"
    
    l = left(i) # The left child of node i
    r = right(i) # The right child of node i

    # Finding the smallest of node i and its children
    if l < len(A) and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    
    if smallest != i:
        # Exchange A[i] and A[smallest]
        temp = A[i]
        A[i] = A[smallest]
        A[smallest] = temp
        minHeapify(A,smallest)


## insert  ##

def insert(A,e):
    A.append(e)
    i = len(A)-1
    while i > 0 and A[parent(i)] > A[i]:
        # Exchange A[i] and A[parent(i)]
        temp = A[i]
        A[i] = A[parent(i)]
        A[parent(i)] = temp
        i = parent(i)


## Parent and children of node i ##

def left(i):
    "Returns the index of the left child of node i"
    return 2*i + 1

def right(i):
    "Returns the index of the right child of node i"
    return 2*i + 2

def parent(i):
    "Returns the index of the parent of node i"
    return (i-1)//2

