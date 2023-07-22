from collections import deque

"""
1 Should I give a ride? (10 marks)
"""


def optimalRoute(start, end, passengers, roads):
    """NOT DONE
            google how to format pycharm comments
        You should implement a function optimalRoute(start, end, passengers, roads) that re- turns one optimal route to go from start to end with the minimum possible total travel time.
        Your function should return the optimal route as a list of integers. If there are multiple route achieving the optimal time, you can return any one of them.
        Args:
            start:
            end:
            passengers:
            roads:

        Returns:
    	Function description: This function returns an output array containing only the unique integers contained within the input array via the use of a modified Merge Sort to discard duplicates during merging.

    	Approach description: Since the titles of the books are integers, we can sort this using Merge Sort. However during the merging process of Merge Sort, if we are ever doing a comparison between two equal integers when choosing which element to place into the merged array first, then we can simply discard one of these integers and place the other in the merged array (and updating pointers appropriately). This means that this modified Merge Sort will not only output a sorted array, but that sorted array will contain only the unique integers contained in the input. This output array is then returned.

    	Given n is the number of elements in the input list:

    	The Merge Sorting section costs O(n*log(n)), as no additional work is being done via the modification to Merge Sort.


    	Merge sort and output array both require O(n) aux space O(n) + O(n) = O(n).

    	Input:
    		bookcase: an array based list containing integers

    	Time complexity: O(n*log(n)), where n is the number of elements in the input array
    	Aux space complexity: O(n),  where n is the number of elements in the input array

    """




    #graph = generateGraph(roads)
    #graph.print_graph()

    #Need to set up adjacency list
    no_of_vertices = find_no_of_vertices(roads)

    print(no_of_vertices)

    carpoolgraph = CarpoolGraph(no_of_vertices)

    #you could combine this with find_no_of_vertices
    for i in range(len(roads)):
        # add edges
        carpoolgraph.add_directed_edge(roads[i][0], roads[i][1], roads[i][2], roads[i][3])
        #add_directed_edge(start, end, single, double)
        #roads = [(0, 3, 5, 3),
        # (3, 4, 35, 15),
        # (3, 2, 2, 2),
        # (4, 0, 15, 10),
        # (2, 4, 30, 25),
        # (2, 0, 2, 2),
        # (0, 1, 10, 10),
        # (1, 4, 30, 20)]

    carpoolgraph.print_graph()

    CarpoolDjikstra(carpoolgraph, start, end, passengers)
    #carpoolgraph = adjacency list with single double weight
    # 0 -> 1 -> 3
    # 1 -> 4
    # 2 -> 0 -> 4
    # 3 -> 2 -> 4
    # 4 -> 0
    #start = 0
    #end = 4
    #passengers = [2, 1]

    #carpoolgraph = adjacency list with single double weight
    #This means 0 can go to 1 and 3
    # 0 -> Vertex No: 1 .single(10).double(10) -> Vertex No: 3 .single(5).double(3)
    # 1 -> Vertex No: 4 .single(30).double(20)
    # 2 -> Vertex No: 0 .single(2).double(2) -> Vertex No: 4 .single(30).double(25)
    # 3 -> Vertex No: 2 .single(2).double(2) -> Vertex No: 4 .single(35).double(15)
    # 4 -> Vertex No: 0 .single(15).double(10)
    #start = 0
    #end = 4
    #passengers = [2, 1]



    #return val = [0, 3, 2, 0, 3, 4]


def find_no_of_vertices(roads):
    """NOT DONE
    Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

    Input:
    	input_array: an array based list containing integers

    	Output: An array based list containing only the unique integers from the input array

    	Time complexity: O(n*log(n)), where n is the number of elements in the input array
    	Aux space complexity: O(n),  where n is the number of elements in the input array
    """
    #Find no_of vertices of the roads graph. Finding max because assignment specification rules.
    # 0,1,2....L
    #O(E)
    max = float('-inf')

    for i in range(len(roads)):
        if roads[i][0] >= max:
            max = roads[i][0]
        if roads[i][1] >= max:
            max = roads[i][1]

    return max + 1

"""
def generateGraph(roads):

    #start = 0
    #end = 4

    # The locations where there are potential passengers
    #passengers = [2, 1]

    # The roads represented as a list of tuple
    #roads = [(0, 3, 5, 3), (3, 4, 35, 15), (3, 2, 2, 2), (4, 0, 15, 10), (2, 4, 30, 25), (2, 0, 2, 2), (0, 1, 10, 10), (1, 4, 30, 20)]
    # Your function should return the optimal route (which takes 27 minutes).

    #optimalRoute(start, end, passengers, roads)
    # [0, 3, 2, 0, 3, 4]

    #for i in range(len(roads)):
        #get max using merge sort


    carpoolgraph = CarpoolGraph(5) #change later

    for i in range(len(roads)):
        #add edges
        carpoolgraph.add_directed_edge(roads[i][0],roads[i][1],roads[i][2],roads[i][3])

    return carpoolgraph

"""

class AdjacencyNode:
    """NOT DONE
    Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

    Input:
    	input_array: an array based list containing integers

    	Output: An array based list containing only the unique integers from the input array

    	Time complexity: O(n*log(n)), where n is the number of elements in the input array
    	Aux space complexity: O(n),  where n is the number of elements in the input array
    """

    def __init__(self, value):
        """NOT DONE
        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array
        """
        self.vertexNo = value
        self.next = None
        # not sure maybe store cost in node?
        self.single = None
        self.double = None

# Directed Weighted Adjacency List Graph
class CarpoolGraph:

    def __init__(self, vertices):
        """NOT DONE
        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array
        """
        self.NoOfVertices = vertices
        #[None, None, None, None, None]
        self.adjgraph = [None] * self.NoOfVertices

    def add_directed_edge(self, start, end, single, double):
        """NOT DONE
        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array
        """
        #directed so we only do one way, no shit but just saying
        adjnode = AdjacencyNode(end)
        adjnode.next = self.adjgraph[start]
        adjnode.single = single
        adjnode.double = double
        self.adjgraph[start] = adjnode

        #add_directed_edge(start, end, single, double)
        #roads = [(0, 3, 5, 3),
        # (3, 4, 35, 15),
        # (3, 2, 2, 2),
        # (4, 0, 15, 10),
        # (2, 4, 30, 25),
        # (2, 0, 2, 2),
        # (0, 1, 10, 10),
        # (1, 4, 30, 20)]

    def print_graph(self):
        for i in range(self.NoOfVertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.adjgraph[i]
            while temp:
                print(" -> Vertex No: {}".format(temp.vertexNo), end="")
                print(".single({}".format(temp.single), end=")")
                print(".double({}".format(temp.double), end=")")
                temp = temp.next
            print(" \n")

#Priority Queue using Min Heap
class MinHeapNode:
    """NOT DONE
    Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

    Input:
    	input_array: an array based list containing integers

    	Output: An array based list containing only the unique integers from the input array

    	Time complexity: O(n*log(n)), where n is the number of elements in the input array
    	Aux space complexity: O(n),  where n is the number of elements in the input array
    """
    def __init__(self, index, key, is_passenger_node):
        self.index = index
        self.key = key
        self.is_passenger_node = is_passenger_node

class Min_Heap_Priority_Queue:
    """NOT DONE
    Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

    Input:
    	input_array: an array based list containing integers

    	Output: An array based list containing only the unique integers from the input array

    	Time complexity: O(n*log(n)), where n is the number of elements in the input array
    	Aux space complexity: O(n),  where n is the number of elements in the input array
    """
    # Acquired from my FIT1008 notes and adjusted to work with key-value arrays
    def __init__(self):
        self.array = [None]
        self.n = 0

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

    # Keep
    def push(self, x):
        """NOT DONE
        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array
        """
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
        """NOT DONE
        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array
        """
        parent = [i // 2]
        while i > 1 and self.array[i].key < self.array[i // 2].key:
            self.swap(i, i // 2)
            i //= 2

    def swap(self, i, j):
        """NOT DONE
        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array
        """
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

    # Keep
    def pop_min(self):
        """NOT DONE
        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array
        """
        self.swap(1, self.n)
        min = self.array.pop(self.n)
        self.n -= 1
        self.sink(1)
        print("Pop [{},{}]".format(min.index, min.key))
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
        """NOT DONE
        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array
        """
        while 2 * i <= self.n:
            child = self.smallestChild(i)
            if self.array[i].key <= self.array[child].key:
                break
            self.swap(child, i)
            i = child

    def smallestChild(self, i):
        """NOT DONE
        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array
        """
        if 2 * i == self.n or self.array[2 * i].key < self.array[2 * i + 1].key:
            return 2 * i
        else:
            return 2 * i + 1


    def printPQ(self):
        temp = []
        for node in self.array[1::]:
            temp.append([node.index, node.key, node.is_passenger_node])
        print("Priority Q: {}".format(temp))

def CarpoolDjikstra(graph, start, end, passengers):
    #carpoolgraph = adjacency list with single double weight
    #This means 0 can go to 1 and 3
    # 0 -> Vertex No: 1 .single(10).double(10) -> Vertex No: 3 .single(5).double(3)
    # 1 -> Vertex No: 4 .single(30).double(20)
    # 2 -> Vertex No: 0 .single(2).double(2) -> Vertex No: 4 .single(30).do uble(25)
    # 3 -> Vertex No: 2 .single(2).double(2) -> Vertex No: 4 .single(35).double(15)
    # 4 -> Vertex No: 0 .single(15).double(10)
    #start = 0
    #end = 4
    #passengers = [2, 1]
    #return val = [0, 3, 2, 0, 3, 4]

    dist = [float('inf')] * graph.NoOfVertices
    #[inf, inf, inf, inf, inf]
    # dist[1..n] = ∞
    dist[start] = 0
    print("Dist list: {}".format(dist))
    #[0, inf, inf, inf, inf]
    #dist[s] = 0

    #pred = list(range(0, graph.NoOfVertices)) why did i do this? [0, 1, 2, 3, 4]
    pred = [None] * graph.NoOfVertices
    print("Pred list: {}".format(pred))
    #[None, None, None, None, None]
    #pred[1..n] = 0

    #use priority queue
    Queue = Min_Heap_Priority_Queue()
    #Q = priority_queue()
    Queue.push(MinHeapNode(start, 0, False))
    Queue.printPQ()

    #----------------------------------------------------------------------------------
    # Up until here works as expected.
    #----------------------------------------------------------------------------------

    print("----------------------------------------------------------------------------------")
    print("Up until here works as expected.")
    print("----------------------------------------------------------------------------------")

    # 0 -> Vertex No: 1 .single(10).double(10) -> Vertex No: 3 .single(5).double(3)
    # 1 -> Vertex No: 4 .single(30).double(20)
    # 2 -> Vertex No: 0 .single(2).double(2) -> Vertex No: 4 .single(30).do uble(25)
    # 3 -> Vertex No: 2 .single(2).double(2) -> Vertex No: 4 .single(35).double(15)
    # 4 -> Vertex No: 0 .single(15).double(10)

    """
    Adjacency list of vertex 0
     head -> Vertex No: 7.single(5).double(5) -> Vertex No: 9.single(1).double(1) 

    Adjacency list of vertex 1
     head -> Vertex No: 8.single(2).double(1) -> Vertex No: 9.single(6).double(5) 

    Adjacency list of vertex 2
     head -> Vertex No: 1.single(2).double(2) -> Vertex No: 3.single(5).double(5) -> Vertex No: 4.single(6).double(2) -> Vertex No: 9.single(6).double(4) 

    Adjacency list of vertex 3
     head -> Vertex No: 5.single(1).double(1) 

    Adjacency list of vertex 4
     head 

    Adjacency list of vertex 5
     head -> Vertex No: 3.single(6).double(6) 

    Adjacency list of vertex 6
     head -> Vertex No: 9.single(6).double(5) -> Vertex No: 4.single(5).double(4) 

    Adjacency list of vertex 7
     head -> Vertex No: 3.single(8).double(7) -> Vertex No: 4.single(3).double(1) 

    Adjacency list of vertex 8
     head -> Vertex No: 7.single(6).double(1) 

    Adjacency list of vertex 9
     head -> Vertex No: 0.single(7).double(4) 

    """


    #start = 0
    #end = 4
    #passengers = [2, 1]
    #dist = [0, inf, inf, inf, inf]
    #pred = [None, None, None, None, None]
    #Q should be Q = [0]
    #return val = [0, 3, 2, 0, 3, 4]
    passenger_condition = False    #PASSENGER CONDITION BEGINNING OR END
    Queue.printPQ()
    completed = []
    while Queue.array[1:]: #slice for now
    #while Q is not empty do
        u = Queue.pop_min()
        completed.append(u.index)
        print("Completed: {}".format(completed))
        # dist = [0, 10, 7, 5, 37]
        # pred = [None, 0, 3, 0, 2]
        if passenger_condition == False and u.index in passengers:
            passenger_condition = True
            print("passenger_condition is True")
            loop_start_index = u.index
            new_dist = dist[:] #[:] prevents it from being a reference to dist
            new_pred = pred[:]
            new_completed = []
            # for i in completed[:len(completed)-1]:
            #     dist[i] = float('inf')
            #for i in completed[:len(completed)]:
            for i in completed:
                new_dist[i] = float('inf')
            # dist = [0, 10, 7, 5, 40]
            # new_dist = [inf, 10, inf, inf, 40]
            # pred = [None, 0, 3, 0, 2]
            print("Pred list: {}".format(pred))
            print("New Pred list: {}".format(new_pred))
            print("Dist list: {}".format(dist))
            print("New Dist list: {}".format(new_dist))
            #Queue.printPQ()
            #if u.index == loop_start_index: to skip if dist[u.index] == u.key:
            while Queue.array[1::]:
                print("----------------------------------------------------------------------------------")
                print("Dist list: {}".format(dist))
                print("New Dist list: {}".format(new_dist))
                Queue.printPQ()

                if u.index is loop_start_index:
                    # if dist[u] = key then
                    temp = graph.adjgraph[u.index]
                    while temp:  # halts on None for adj node
                        # for each edge e that is adjacent to u do
                        if new_dist[temp.vertexNo] > dist[u.index] + temp.double:  # think about the case for when it turns to double
                            # if dist[v] > dist[u] + w(u, v) then
                            new_dist[temp.vertexNo] = dist[u.index] + temp.double
                            # dist[v] = dist[u] + w(u, v)
                            new_pred[temp.vertexNo] = u.index
                            # pred[v] = u
                            Queue.push(MinHeapNode(temp.vertexNo, new_dist[temp.vertexNo], u.is_passenger_node))
                            # temp = temp.next
                            # Queue.printPQ()
                            # Q.push(v, key=dist[v])
                        # elif dist[temp.vertexNo] is float('inf'):
                        #     new_dist[temp.vertexNo] = dist[u.index] + temp.double
                        #     # dist[v] = dist[u] + w(u, v)
                        #     new_pred[temp.vertexNo] = u.index
                        #     # pred[v] = u
                        #     Queue.push(MinHeapNode(temp.vertexNo, new_dist[temp.vertexNo], u.is_passenger_node))
                        #     # temp = temp.next
                        #     # Queue.printPQ()
                        temp = temp.next
                        Queue.printPQ()
                    print("Pred list: {}".format(pred))
                    print("New Pred list: {}".format(new_pred))
                    print("Dist list: {}".format(dist))
                    print("New Dist list: {}".format(new_dist))
                    print("hey")

                    print("----------------------------------------------------------------------------------")
                elif not u.is_passenger_node and dist[u.index] == u.key:
                    # if dist[u] = key then
                    temp = graph.adjgraph[u.index]
                    while temp:  # halts on None for adj node
                        # for each edge e that is adjacent to u do
                        if dist[temp.vertexNo] > dist[
                            u.index] + temp.single:  # think about the case for when it turns to double
                            # if dist[v] > dist[u] + w(u, v) then
                            dist[temp.vertexNo] = dist[u.index] + temp.single
                            # dist[v] = dist[u] + w(u, v)
                            pred[temp.vertexNo] = u.index
                            # pred[v] = u
                            Queue.push(MinHeapNode(temp.vertexNo, dist[temp.vertexNo], u.is_passenger_node))
                            # temp = temp.next
                            # Queue.printPQ()
                            # Q.push(v, key=dist[v])
                        temp = temp.next
                        Queue.printPQ()
                    print("Dist list: {}".format(dist))
                    print("Pred list: {}".format(pred))
                    print("----------------------------------------------------------------------------------")
                #if dist[u.index] == new_dist[u.index]:
                    #to solve the 1 10 problem
                #   dist[u.index] != new_dist[u.index] and
                elif new_dist[u.index] == u.key: #7 == 7
                    # if dist[u] = key then
                    temp = graph.adjgraph[u.index]
                    while temp:  # halts on None for adj node
                        # for each edge e that is adjacent to u do
                        if new_dist[temp.vertexNo] > new_dist[u.index] + temp.double:  # think about the case for when it turns to double
                            # if dist[v] > dist[u] + w(u, v) then
                            new_dist[temp.vertexNo] = new_dist[u.index] + temp.double
                            # dist[v] = dist[u] + w(u, v)
                            new_pred[temp.vertexNo] = u.index
                            # pred[v] = u
                            Queue.push(MinHeapNode(temp.vertexNo, new_dist[temp.vertexNo], temp.vertexNo in passengers))
                            # temp = temp.next
                            # Queue.printPQ()
                            # Q.push(v, key=dist[v])
                        temp = temp.next
                        Queue.printPQ()
                    print("Dist list: {}".format(dist))
                    print("Pred list: {}".format(pred))
                    print("New Pred list: {}".format(new_pred))
                    print("New Dist list: {}".format(new_dist))
                    print("----------------------------------------------------------------------------------")
                u = Queue.pop_min()
                completed.append(u.index)
                print("Completed: {}".format(completed))
                if u.index == loop_start_index:
                    #break #something along the lines
                    path = deque()
                    index = end
                    while index != loop_start_index:
                        path.appendleft(index)
                        index = new_pred[index]
                    if index == loop_start_index:
                        while index is not start:
                            path.appendleft(index)
                            index = pred[index]
                    print(index)
                    if index is start:
                        path.appendleft(start)

                    final_path = []
                    for item in path:
                        final_path.append(item)

                    print("New Dist list: {}".format(new_dist))
                    print("Pred list: {}".format(pred))
                    print("New Pred list: {}".format(new_pred))
                    Queue.printPQ()
                    print(path)
                    print(final_path)

                    return final_path
    #u, key = Q.pop_min()
            print("hello")
            print("Pred list: {}".format(pred))
            print("New Pred list: {}".format(new_pred))
            print("Dist list: {}".format(dist))
            print("New Dist list: {}".format(new_dist))
            print("Loop Start Index: {}".format(loop_start_index))
            Queue.printPQ()
            index = end
            path = deque()
            path.appendleft(end)

            if dist[end] is float('inf') or dist[end] > new_dist[end]:
                while index is not loop_start_index or new_pred[index] is not None:
                    path.appendleft(new_pred[index])
                    index = new_pred[index]
                if index == loop_start_index:
                    while index is not start:
                        path.appendleft(pred[index])
                        index = pred[index]
                final_path = []
                for item in path:
                    final_path.append(item)
                print(path)
                print(final_path)
                return final_path

        # print(dist[u.index])
        # print(u.key)

        # IF ITS JUST BELOW THEN NO PASSENGERS
        #----------------------------------------------------------------------------------
        # THIS IS THE BASE CASE
        if dist[u.index] == u.key:
        #if dist[u] = key then
            temp = graph.adjgraph[u.index]
            while temp: #halts on None for adj node
            #for each edge e that is adjacent to u do
                if dist[temp.vertexNo] > dist[u.index] + temp.single: #think about the case for when it turns to double
                #if dist[v] > dist[u] + w(u, v) then
                    dist[temp.vertexNo] = dist[u.index] + temp.single
                    #dist[v] = dist[u] + w(u, v)
                    pred[temp.vertexNo] = u.index
                    #pred[v] = u
                    Queue.push(MinHeapNode(temp.vertexNo, dist[temp.vertexNo], temp.vertexNo in passengers))
                    # temp = temp.next
                    # Queue.printPQ()
                    #Q.push(v, key=dist[v])
                temp = temp.next
                Queue.printPQ()
            print("Dist list: {}".format(dist))
            print("Pred list: {}".format(pred))
            print("----------------------------------------------------------------------------------")


    #print(passenger_condition)
    print("Dist list: {}".format(dist))
    print("Pred list: {}".format(pred))
    print("Completed list: {}".format(completed))
    #[4, None, 0, 1, 3, 1]
    index = end
    path = deque()
    path.appendleft(end)
    while index is not start:
        path.appendleft(pred[index])
        index = pred[index]
    final_path = []
    for item in path:
        final_path.append(item)
    print(path)
    print(final_path)
    return final_path
    #return dist[1..n], pred[1..n]

    #return val = [0, 3, 2, 0, 3, 4]


"""
DUMP
    #Q.push(s, key=0)
    #list(range(0, 5))

    #Q is now Q = [0,inf,inf, inf, .., inf]
    #Q should be Q = [0]

     I dont need to do this
    for i in list(range(0, graph.NoOfVertices)):
        if i == start:
            continue
        else:
            Queue.push(i, float('inf'))

    #set up queue

"""


"""
function DIJKSTRA(G=(V,E),s) 
    dist[1..n] = ∞
    pred[1..n] = 0
    dist[s]=0
    Q = priority_queue() 
    Q.push(s , key = 0) 
    while Q is not empty do
        u, key = Q.pop_min() 
        if dist[u] = key then
            for each edge e that is adjacent to u do 
                if dist[v] > dist[u] + w(u,v) then 
                    dist[v] = dist[u] + w(u,v)
                    pred[v ] = u
                    Q.push(v , key = dist[v ])
    return dist[1..n], pred[1..n]

"""

if __name__ == "__main__":

    # # Example 1 OK Lol
    # # What is the significance of 0,3 repeat?
    # start = 0
    # end = 4
    # # The locations where there are potential passengers
    # passengers = [2, 1]
    # # The roads represented as a list of tuple
    # roads = [(0, 3, 5, 3),
    #          (3, 4, 35, 15),
    #          (3, 2, 2, 2),
    #          (4, 0, 15, 10),
    #          (2, 4, 30, 25),
    #          (2, 0, 2, 2),
    #          (0, 1, 10, 10),
    #          (1, 4, 30, 20)]
    # #If you switch 0->3 and 0->1
    # # Goes from 0 -> 1 -> 3
    # # To 0 -> 3 -> 1
    # #roads = [(0, 1, 10, 10), (0, 3, 5, 3), (3, 4, 35, 15), (3, 2, 2, 2), (4, 0, 15, 10), (2, 4, 30, 25), (2, 0, 2, 2), (1, 4, 30, 20)]
    # # Your function should return the optimal route (which takes 27 minutes).
    # optimalRoute(start, end, passengers, roads)
    # #[0, 3, 2, 0, 3, 4]

    # # Example 2 PassCon FAIL
    # What is the significance of 2,0,7 repeat?
    # start = 2
    # end = 5
    # passengers = [3]
    # roads = [
    #     (6, 2, 22, 6),
    #     (3, 6, 4, 3),
    #     (0, 7, 8, 3),
    #     (5, 0, 9, 6),
    #     (5, 4, 6, 5),
    #     (4, 3, 24, 2),
    #     (1, 2, 26, 23),
    #     (7, 4, 26, 8),
    #     (7, 3, 12, 5),
    #     (4, 5, 10, 3),
    #     (2, 0, 14, 1),
    #     (5, 7, 6, 6)
    # ]
    # res_1 = [2, 0, 7, 3, 6, 2, 0, 7, 4, 5]  # Both results should yield 58 mins
    # res_2 = [2, 0, 7, 4, 5]
    # optimalRoute(start, end, passengers, roads)

    #OK
    # # Example 3 Non_Pass FAIL 4 has no edges out?
    # Check Edges
    # start = 6
    # end = 7
    # passengers = [4, 2, 9]
    # roads = [
    #     (9, 0, 7, 4),
    #     (7, 4, 3, 1),
    #     (8, 7, 6, 1),
    #     (3, 5, 1, 1),
    #     (2, 9, 6, 4),
    #     (6, 4, 5, 4),
    #     (2, 4, 6, 2),
    #     (7, 3, 8, 7),
    #     (0, 9, 1, 1),
    #     (2, 3, 5, 5),
    #     (5, 3, 6, 6),
    #     (1, 9, 6, 5),
    #     (0, 7, 5, 5),
    #     (1, 8, 2, 1),
    #     (6, 9, 6, 5),
    #     (2, 1, 2, 2)
    # ]
    # result = [6, 9, 0, 7]  # optimal route should take 15 mins
    # optimalRoute(start, end, passengers, roads)

    # # Example 4 PassCon FAIL
    # PasscCon No Repeat
    # start = 0
    # end = 5
    # passengers = [2, 1]
    # roads = [
    #     (4, 5, 200, 2),
    #     (0, 2, 2, 2),
    #     (1, 3, 10, 5),
    #     (3, 5, 50, 50),
    #     (2, 4, 10, 10),
    #     (0, 1, 1, 1)
    # ]
    # result = [0, 2, 4, 5]
    # optimalRoute(start, end, passengers, roads)

    # # Example 5
    # # PassCon repeat of 0
    # start = 0
    # end = 4
    # passengers = [2, 1]
    # roads = [
    #     (0, 4, 30, 5),
    #     (0, 1, 5, 4),
    #     (1, 3, 3, 2),
    #     (3, 2, 2, 1),
    #     (2, 0, 1, 1)]
    # result = [0, 1, 3, 2, 0, 4]
    # optimalRoute(start, end, passengers, roads)


    # # Example 6
    # Sample IO given in the spec sheet
    # start = 0
    # end = 4
    # passengers = [2, 1]
    # roads = [
    #     (0, 3, 5, 3),
    #     (3, 4, 35, 15),
    #     (3, 2, 2, 2),
    #     (4, 0, 15, 10),
    #     (2, 4, 30, 25),
    #     (2, 0, 2, 2),
    #     (0, 1, 10, 10),
    #     (1, 4, 30, 20),
    # ]
    # expected = [0, 3, 2, 0, 3, 4]
    # optimalRoute(start, end, passengers, roads)

    #FAIL I thnk because it goes to the regular no passenger return
    # # Example 7 LONG ONE
    # # What is the significance of not having repeats? Number of nodes or because of the early access to 26? Or both?
    # start = 54
    # end = 62
    # passengers = [29, 63, 22, 18, 2, 23, 48, 41, 15, 31, 13, 4, 24, 16, 27, 17, 50, 67, 37, 58, 28, 64, 35, 10, 68, 38,
    #               59, 26, 69, 43, 44, 30, 46, 7]
    # roads = [
    #     (31, 45, 23, 12), (48, 3, 14, 7), (58, 50, 25, 10),
    #     (5, 3, 26, 23), (12, 32, 29, 3), (65, 4, 16, 16),
    #     (13, 46, 14, 13), (63, 29, 10, 2), (19, 56, 30, 19),
    #     (52, 47, 19, 12), (47, 52, 12, 8), (30, 42, 22, 19),
    #     (46, 60, 17, 17), (54, 22, 8, 7), (19, 8, 23, 10),
    #     (33, 51, 22, 5), (12, 17, 20, 5), (64, 62, 22, 18),
    #     (66, 25, 28, 10), (48, 19, 23, 8), (36, 13, 22, 19),
    #     (26, 48, 6, 3), (31, 30, 26, 9), (24, 29, 22, 11),
    #     (23, 36, 27, 11), (59, 37, 16, 10), (60, 44, 12, 8),
    #     (40, 7, 18, 1), (22, 3, 13, 12), (36, 35, 15, 15),
    #     (43, 2, 23, 6), (29, 27, 27, 6), (34, 0, 17, 4),
    #     (52, 50, 13, 4), (27, 23, 15, 1), (15, 10, 7, 6),
    #     (36, 65, 23, 1), (41, 64, 27, 8), (45, 34, 12, 1),
    #     (51, 24, 12, 10), (16, 12, 29, 7), (9, 67, 25, 24),
    #     (49, 38, 16, 4), (38, 7, 10, 1), (50, 13, 23, 16),
    #     (5, 33, 27, 10), (23, 42, 29, 15), (9, 2, 13, 7),
    #     (59, 52, 23, 17), (59, 54, 8, 6), (1, 8, 10, 8),
    #     (33, 30, 15, 2), (6, 26, 18, 6), (39, 57, 13, 12),
    #     (54, 26, 13, 9), (57, 41, 4, 4), (37, 66, 16, 12),
    #     (36, 9, 12, 5), (2, 68, 7, 3), (69, 28, 18, 2),
    #     (44, 1, 14, 3), (48, 9, 6, 4), (17, 38, 13, 1),
    #     (61, 49, 4, 4), (9, 10, 6, 3), (46, 37, 21, 8),
    #     (23, 53, 21, 8), (7, 24, 28, 26), (62, 20, 22, 7),
    #     (1, 18, 10, 1), (7, 41, 9, 1), (13, 18, 6, 4),
    #     (25, 21, 21, 3), (1, 61, 21, 16), (49, 40, 13, 5),
    #     (19, 25, 11, 10), (62, 50, 5, 5), (33, 46, 10, 9),
    #     (28, 25, 14, 6), (56, 51, 6, 4), (18, 19, 15, 1),
    #     (30, 9, 23, 13), (60, 21, 23, 7), (52, 37, 16, 6),
    #     (50, 42, 11, 4)
    # ]
    # # Optimal route is 198 mins
    # result = [54, 26, 48, 19, 56, 51, 24, 29, 27, 23, 36, 13, 46, 60, 44, 1, 61, 49, 38, 7, 41, 64, 62]
    # optimalRoute(start, end, passengers, roads)

    # OK
    # # Example 8 NO PASSENGER
    # start = 4
    # end = 0
    # passengers = []
    # roads = [
    #     (0, 1, 28, 22),
    #     (3, 2, 21, 10),
    #     (4, 1, 26, 20),
    #     (1, 3, 5, 3),
    #     (0, 4, 24, 13),
    #     (2, 1, 26, 15),
    #     (2, 0, 26, 26)
    # ]
    # result = [4, 1, 3, 2, 0]  # Optimal route is 78 mins
    # optimalRoute(start, end, passengers, roads)

    # OK
    # Example 9 NO PASSENGER
    # start = 1
    # end = 2
    # passengers = []
    # roads = [
    #     (3, 4, 24, 10),
    #     (4, 1, 16, 6),
    #     (0, 2, 28, 14),
    #     (1, 3, 27, 12),
    #     (4, 0, 5, 4),
    #     (2, 4, 15, 9)
    # ]
    # result = [1, 3, 4, 0, 2]  # Optimal route is 84 mins
    # optimalRoute(start, end, passengers, roads)

    # OK
    # Example 9.5 NO PASSENGER
    # start = 1
    # end = 2
    # passengers = []
    # roads = [
    #     (3, 4, 24, 10),
    #     (4, 1, 16, 6),
    #     (0, 2, 28, 14),
    #     (1, 3, 27, 12),
    #     (4, 0, 5, 4),
    #     (2, 4, 15, 9),
    #     (1, 5, 15, 9)
    # ]
    # result = [1, 3, 4, 0, 2]  # Optimal route is 84 mins
    # optimalRoute(start, end, passengers, roads)

    # # Example 10
    # start = 4
    # end = 9
    # passengers = [2, 6, 0]
    # roads = [
    #     (4, 6, 30, 18),
    #     (3, 1, 8, 1),
    #     (9, 1, 9, 5),
    #     (1, 9, 30, 2),
    #     (8, 5, 12, 12),
    #     (8, 9, 8, 6),
    #     (1, 8, 25, 2),
    #     (2, 4, 4, 2),
    #     (6, 0, 25, 5),
    #     (4, 3, 6, 6),
    #     (1, 2, 15, 7)
    # ]
    # result = [4, 3, 1, 2, 4, 3, 1, 9]
    # optimalRoute(start, end, passengers, roads)

    # # OK Works, but I believe I haven't solved all problems
    # # Example 11
    # start = 0
    # end = 5
    # passengers = [3, 4, 2]
    # roads = [
    #     (0, 1, 100, 95),
    #     (0, 2, 2, 2),
    #     (0, 3, 1, 1),
    #     (0, 4, 3, 3),
    #     (1, 5, 5, 3),
    #     (2, 5, 1000, 955),
    #     (3, 5, 1000, 955),
    #     (4, 5, 1000, 955),
    # ]
    # result = [0, 1, 5]  # Optimal route is 105 mins
    # optimalRoute(start, end, passengers, roads)

    # # OK Works, but I believe I haven't solved all problems
    # Example 12
    # start = 0
    # end = 3
    # passengers = [2]
    # roads = [(0, 1, 10, 10), (1, 3, 1, 1), (0, 2, 2, 2)]
    # result = [0, 1, 3]  # Optimal route is 11 minutes
    # optimalRoute(start, end, passengers, roads)

    # FAIL
    # Example 13
    start = 0
    end = 3
    passengers = [2, 1]
    roads = [(0, 1, 10, 10), (1, 3, 100, 1), (0, 2, 2, 2), (2, 3, 60, 60)]
    result = [0, 1, 3] # Optimal route is 11 minutes
    optimalRoute(start, end, passengers, roads)

    # FAIL
    # # Example 14
    # start = 0
    # end = 3
    # passengers = [2, 1]
    # roads = [(0, 1, 10, 10), (1, 3, 100, 1), (0, 2, 2, 2), (2, 3, 60, 60), (2, 1, 6, 3)]
    # result = [0, 2, 1, 3] # Optimal route is 6 minutes
    # optimalRoute(start, end, passengers, roads)
