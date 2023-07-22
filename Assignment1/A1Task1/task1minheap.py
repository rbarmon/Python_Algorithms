# Priority Queue implementation in Python


#Priority Queue using Min Heap
class MinHeapNode:
    def __init__(self, index, key):
        self.index = index
        self.key = key

class Min_Heap_Priority_Queue:
    # Acquired from my FIT1008 notes and adjusted to work with key-value arrays
    def __init__(self):
        self.array = [None]
        self.n = 0
    def __str__(self):
        return self.array
    def __len__(self):
        return self.n

    """
    • Due to its structure, a binary heap can be represented as a flat array array[1..n]
    where the root node is array[1] and for each node array[i], its children (if they exist)
    are elements array[2i] and array[2i + 1].
    
    The standard operations on a min/max heap, implementing the priority queue abstract data
    type are:
    
    The following pseudocode implements a max heap, i.e. a heap that pops the maximum value.
    """

    """
    1. HEAPIFY: Convert a given (not necessarily sorted) array into a min/max heap.
    Algorithm 10 Heapify
    1: function HEAPIFY(array[1..n])
    2:      for i = n/2 to 1 do
    3:          FALL(array[1..n], i)
    """

    """
    2. INSERT: Insert an element into the heap.
    Algorithm 11 Heap: Insert
    1: function INSERT(array[1..n], x )
    2:      array.append(x)
    3:      n += 1
    4:      RISE(array[1..n], n)
    """
    #Keep
    def push(self, x):
        # self.array.append(x)
        # self.count += 1
        # self.min_rise(self.count)
        self.array.append(x)
        self.n += 1
        self.min_rise(self.n)

    """
    1. RISE: Move an element higher up the heap until it satisfies the heap property.
    Algorithm 13 Heap: Rise
    1: function RISE(array[1..n], i)
    2:      parent = [i /2]
    3:      while parent ≥ 1 do
    4:          if array[parent] < array[i] then
    5:              swap(array[parent], array[i])
    6:              i = parent
    7:              parent = bi/2c
    8:          else
    9:              break
    """
    def min_rise(self, i):
        parent = [i//2]
        while i > 1 and self.array[i].key < self.array[i//2].key:
            self.swap(i, i//2)
            i //= 2

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    """
    3. REMOVE: Remove the min/max value from the heap.
    Algorithm 12 Heap: Delete
    1: function EXTRACT_MAX(array[1..n])
    2:      swap(array[1], array[n])
    3:      n = n - 1
    4:      FALL(array[1..n], 1)
    5:      return array.pop_back()
    """
    #Keep
    def pop_min(self):
        self.swap(1, self.n)
        min = self.array.pop(self.n)
        self.n -= 1
        self.sink(1)
        print(min.index,min.key)
        return min

    """
    2. FALL: Move an element down the heap until it satisfies the heap property.
    Algorithm 14 Heap: Fall
    1: function FALL(array[1..n], i)
    2:      child = 2i
    3:      while child ≤ n do
    4:          if child < n and array[child+1] > array[child] then
    5:          child += 1
    6:      if array[i] < array[child] then
    7:          swap(array[i], array[child])
    8:          i = child
    9:          child = 2i
    10:     else
    11:         break
    """
    def sink(self, i):
        while 2*i <= self.n:
            child = self.smallestChild(i)
            if self.array[i].key <= self.array[child].key:
                break
            self.swap(child, i)
            i = child

    def smallestChild(self, i):
        if 2*i == self.n or self.array[2*i].key < self.array[2*i+1].key:
            return 2*i
        else:
            return 2*i + 1




    def getRoot(self):
        return self.array[1]
    def replaceRoot(self, newRoot):
        if self.n >= 1:
            oldRoot = self.array[1]
            self.array[1] = newRoot
            self.sink(1)
            return oldRoot


if __name__ == '__main__':
    start = 0
    Queue = Min_Heap_Priority_Queue()
    Node = MinHeapNode(start, 0)
    Queue.push(MinHeapNode(start, 0))
    Queue.pop_min()
    Queue.push(MinHeapNode(1, 10))
    Queue.push(MinHeapNode(3, 5))
    Queue.pop_min()



    # MHeap = Min_Heap_Priority_Queue()
    # MHeap.push(12)
    # MHeap.push(6)
    # MHeap.push(2)
    # MHeap.push(32)
    # MHeap.push(3)
    # MHeap.push(1)
    # print(MHeap.array)
    # print(MHeap.getRoot())
    # print(MHeap.pop_min())
    # print(MHeap.array)
    # print(MHeap.pop_min())
    # print(MHeap.array)
    # print(MHeap.pop_min())
    # print(MHeap.array)
    # print(MHeap.pop_min())
    # print(MHeap.array)
    # print(MHeap.pop_min())
    # print(MHeap.array)
    # MHeap.push(3)
    # print(MHeap.array)
    # print(MHeap.pop_min())

    """arr = []

    insert(arr, 3)
    insert(arr, 4)
    insert(arr, 9)
    insert(arr, 5)
    insert(arr, 2)

    print ("Max-Heap array: " + str(arr))

    deleteNode(arr, 4)
    print("After deleting an element: " + str(arr))


    #use priority queue
    Queue = Min_Heap_Priority_Queue()
    #Q = priority_queue()
    Queue.push(0, 0)
    Queue.push(1, float('inf'))
    Queue.push(2, float('inf'))
    Queue.push(3, float('inf'))
    Queue.push(4, float('inf'))

    #Q is now Q = [0,inf,inf, inf, .., inf]"""
