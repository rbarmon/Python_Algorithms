
"""
1 Should I give a ride? (10 marks)
"""

def optimalRoute(start, end, passengers, roads):
    """ NOT DONE
    	Function description: This function returns an output array containing integers that represent the optimal
    	route to take to from start to end that has the minimum total travel time through the use of a modified
    	Dijkstra's Algorithm to accommodate for the case of when a passenger is picked up and the weights of the graph edges
    	change.

    	Approach description:

            Algorithm for solving the single source, all targets shortest path problem on graphs with non-negative weights

            Major problem is that the distances need to be reset once a passenger is pick up.

            Create two layers of djikstra

            base layer: no passenger is picked up therefore it runs normally.

            second layer: once a passenger is picked up must use that passenger reset dikstra with the current information so that a shorter path can be found.


    	Since the titles of the books are integers, we can sort this using Merge Sort. However during the merging process of Merge Sort, if we are ever doing a comparison between two equal integers when choosing which element to place into the merged array first, then we can simply discard one of these integers and place the other in the merged array (and updating pointers appropriately). This means that this modified Merge Sort will not only output a sorted array, but that sorted array will contain only the unique integers contained in the input. This output array is then returned.

        Time Complexity Breakdown:

            Given an input with |L| key locations and |R| roads:

            Pre-processing:

                Directed Weighted Adjacency List construction

            Modified Dijkstra section costs O(|R|log|L|), there are at most two rounds of Dijkstra running
                First without passengers
                Second if passenger is found

            Final processing:

            Total Time Complexity: + O(|R|log|L|) + = O(|R|log|L|)



        Aux Space Complexity Breakdown:

            Pre-processing:

            Directed Weighted Adjacency List Graph O(|L| + |R|)

            Priority Queue O(|R|)

            Final-processing:

            Total Aux Space Complexity = + O(|L| + |R|) + O(|R|) + = O(|L| + |R|)



    	Input:
    	    start: index for the start location of the drive
    	    end: index for the end location of the drive
    	    passengers: a list of integers that contains the indices where passengers are located
    	    roads: a List of tuples in which each tuple is a road represented in the form of:
    	    (road start location, road end location, time taken alone, time take with passenger)

    	Output:
    	    optimal_route: a list of integers that contains the optimal route to take from start to end.

    	Time complexity: O(|R|log|L|), given an input with |L| key locations and |R| roads

    	Aux space complexity: O(|L| + |R|), given an input with |L| key locations and |R| roads

    """

    """
    First need to set up Directed Weighted Adjacency List based on the roads input
        Find the number of vertices in roads
        instantiate adjacency list for total number of location |L|-1
        Add every road to the adjacency list as an directed weighted edge. Check CarpoolGraph for further information.
    Call CarpoolDjikstra with input as carpoolgraph, start, end, and passengers, in order to run modified Dijkstra
    """

    #Need to set up adjacency list
    no_of_vertices = find_no_of_vertices(roads)
    # print(no_of_vertices)

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

    # carpoolgraph.print_graph()

    CarpoolDjikstra(carpoolgraph, start, end, passengers)

def find_no_of_vertices(roads):
    """NOT DONE
    Function description: This function an integer that is the total number of vertices in the roads list of tuples by
    finding the maximum value of all locations appearing in roads as the assignment specification specifies that
    location will be a value from 0,1,2....|L|-1.

    Input:
    	roads: a List of tuples in which each tuple is a road represented in the form of:
    	(road start location, road end location, time taken alone, time take with passenger)

    Output:
        An integer that is the total number of vertices in the roads list of tuples.

    Time complexity: O(|R|), where R is the number of roads in the roads list of tuples
    Aux space complexity: O(1)

    """
    max = float('-inf')

    for i in range(len(roads)):
        if roads[i][0] >= max:
            max = roads[i][0]
        if roads[i][1] >= max:
            max = roads[i][1]

    return max + 1


class AdjacencyNode:
    """NOT DONE
    Class description: Class used to store the values of the roads where vertexNo is used to track the integer value of
    the end vertex, next tracks the other edges connected to the start vertex, single stores the weight for when there
    is no passengers and double stores the weight for when there is a passenger riding the car. No functions for this
    class besides the constructor.
    """

    def __init__(self, value):
        """ NOT DONE
        Function description: Constructor for a AdjacencyNode for Directed Weighted Adjacency List.

        Input:
            value: index value of the end vertex of a edge in a adajacency list
        """
        self.vertexNo = value
        self.next = None
        # not sure maybe store cost in node?
        self.single = None
        self.double = None

class CarpoolGraph:
    """
    Class description: Class to create a Directed Weighted Adjacency List Graph for storing the roads details. Function
    for this class is add_directed_edge which creates a new adjacency list node to represent an edge.
    """

    def __init__(self, vertices):
        """NOT DONE
        Function description: Constructor for Carpool Graph

        Input:
        	vertices: a integer value for the total number of vertices the adjacency list will have.
        """
        self.NoOfVertices = vertices
        #[None, None, None, None, None]
        self.adjgraph = [None] * self.NoOfVertices

    def add_directed_edge(self, start, end, single, double):
        """NOT DONE
        Function description: This function creates an AdjacencyNode for the end vertex that is connected to the start
        index and maintains a reference of all the vertices connected to start by using next.

        Input:
        	start: an index of the start location of the road
        	end: an index of the end location of the road
        	single: the edge weight of using the road with no passengers
        	double: the edge weight of using the road with passengers

        Time complexity: O(1), for each road.
        """
        adjnode = AdjacencyNode(end)
        adjnode.next = self.adjgraph[start]
        adjnode.single = single
        adjnode.double = double
        self.adjgraph[start] = adjnode

    # def print_graph(self):
    #     for i in range(self.NoOfVertices):
    #         print("Adjacency list of vertex {}\n head".format(i), end="")
    #         temp = self.adjgraph[i]
    #         while temp:
    #             print(" -> Vertex No: {}".format(temp.vertexNo), end="")
    #             print(".single({}".format(temp.single), end=")")
    #             print(".double({}".format(temp.double), end=")")
    #             temp = temp.next
    #         print(" \n")

class MinHeapNode:
    """ NOT DONE
    Class description: MinHeapNode which represents the priority queue value that is necessary to perform Dijkstra's
    Algorithm. Slightly modified to track whether the node can have a passenger riding the car. No other functions
    besides the constructor.
    """

    def __init__(self, index, key, is_passenger_node):
        """NOT DONE
        Function description: Constructor for MinHeapNode.

        Input:
        	index: an integer value that is the index value for the vertex.
        	key: an integer value that is the key for the u value in Dijkstra.
        	is_passenger_node: a boolean value, which if False, then no passenger can be riding the car, if True, then
        	a passenger can be riding the car.
        """
        self.index = index
        self.key = key
        self.is_passenger_node = is_passenger_node


class Min_Heap_Priority_Queue:
    """NOT DONE
    Class description: Priority Queue using Min Heap, that is based off of the Max Heap in course notes "Binary Heap
    Operations" section page 25 and FIT1008 Heap Data Structure Code. Slightly modified so that the Priority Queue tracks whether the node is capable of
    having a passenger riding the car, and if true this is the used to change which weight value we access from the
    Adjacency List from single to doyble.

    The operations on a min heap, that were necessary for the priority queue were


    Input:
    	input_array: an array based list containing integers

    	Output: An array based list containing only the unique integers from the input array

    	Time complexity: O(n*log(n)), where n is the number of elements in the input array
    	Aux space complexity: O(n),  where n is the number of elements in the input array
    """

    def __init__(self):
        """
        Function description: Constructor for Min_Heap_Priority_Queue. Starts with array with None value.
        From the course notes: "Due to its structure, a binary heap can be represented as a flat array array[1..n]
        where the root node is array[1] and for each node array[i], its children (if they exist)
        are elements array[2i] and array[2i + 1]." So array[0] is set as None.

        """
        # self.array = [None]
        self.array = []
        self.n = -1

    # Keep
    def push(self, x):
        """NOT DONE
        Function description: Function to Insert an element into the heap. Append new minheap node to the array
        and increase n and then call min_rise.
        This is the Insert function Algorithm 11 from the same section in the course notes.

        Input:
        	x: minheap node
        """
        self.array.append(x)
        self.n += 1
        self.min_rise(self.n)

    def min_rise(self, i):
        """NOT DONE
        Function description: Function


        This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array

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
        # parent = [i // 2]
        # while i > 1 and self.array[i].key < self.array[i // 2].key:
        #     self.swap(i, i // 2)
        #     i //= 2
        # parent = [(i - 1) // 2]

        # while i > 1 and self.array[i].key < self.array[i // 2].key:
        #     self.array[i], self.array[i // 2] = self.array[i // 2], self.array[i]
        #     i = i // 2
        parent_index = (i-1) // 2
        while i > 0 and self.array[i].key < self.array[parent_index].key:
            self.swap(i,parent_index)
            i = parent_index

    def swap(self, i, j):
        """NOT DONE
        Function to swap.

        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array
        """
        self.array[i], self.array[j] = self.array[j], self.array[i]

    # Keep
    def pop_min(self):
        """NOT DONE
        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array

        3. REMOVE: Remove the min/max value from the heap.
        Algorithm 12 Heap: Delete
        1: function EXTRACT_MAX(array[1..n])
        2:      swap(array[1], array[n])
        3:      n = n - 1
        4:      FALL(array[1..n], 1)
        5:      return array.pop_back()
        """
        # self.swap(1, self.n)
        # min = self.array.pop(self.n)
        # self.n -= 1
        # self.sink(1)
        # print("Pop [{},{}]".format(min.index, min.key))
        # return min
        self.swap(0, self.n)
        minimum = self.array.pop(self.n)
        self.n -= 1
        self.sink(0)
        # print("Pop [{},{}]".format(min.index, min.key))
        return minimum

    def sink(self, i):
        """NOT DONE
        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array

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
        while (2*i)+1 <= self.n:
            child = self.smallestChild(i)
            if self.array[i].key <= self.array[child].key:
                break
            self.swap(child, i)
            i = child

        # while 2 * i <= self.n:
        #     child = self.smallestChild(i)
        #     if self.array[i].key <= self.array[child].key:
        #         break
        #     self.swap(child, i)
        #     i = child


    def smallestChild(self, i):
        """NOT DONE
        Function description: This function returns a sorted output array containing only the unique integers contained within the input array.

        Input:
        	input_array: an array based list containing integers

        	Output: An array based list containing only the unique integers from the input array

        	Time complexity: O(n*log(n)), where n is the number of elements in the input array
        	Aux space complexity: O(n),  where n is the number of elements in the input array
        """
        if (2 * i) + 1 == self.n or self.array[(2 * i) + 1].key < self.array[(2 * i) + 2].key:
            return (2 * i) + 1
        else:
            return (2 * i) + 2

    def printPQ(self):
        temp = []
        for node in self.array:
            temp.append([node.index, node.key, node.is_passenger_node])
        print("Priority Q: {}".format(temp))


def CarpoolDjikstra(graph, start, end, passengers):
    """ NOT DONE
        Function description: This function returns the optimal path from the start vertex to end vertex that minimizes
        the total time travelled. Runs two frames of Dijkstra if necessary: First if no passenger is yet to be picked up
        it operates as a regular Dijkstra's Algorithm, Second if a passenger is picked up then operates on an updated
        dist, and pred List in order to be able to reassign the values for faster now available paths.

    	Input:
    		graph: a Directed Weighted Adjacency List Graph for storing the roads details
    		start: index for the start location of the drive
    	    end: index for the end location of the drive
    	    passengers: a list of integers that contains the indices where passengers are located

    	Output:
    	    optimal_route: a list of integers that contains the optimal route to take from start to end.
    """

    """
        First part of Dijkstra's Algorithm
        Set up dist list with positive inf values and assign start vertex value as 0
        Set up pred list with None values
        Set up priority queue and push start vertex with key of 0 and is_passenger_node as False because no passengers
        will be present at start node according to the assignment brief.
    """
    dist = [float('inf')] * graph.NoOfVertices
    # dist[1..n] = ∞
    # [inf, inf, inf, inf, inf]
    dist[start] = 0
    # dist[s] = 0
    # print("Dist list: {}".format(dist))
    # [0, inf, inf, inf, inf]

    pred = [None] * graph.NoOfVertices
    # pred[1..n] = 0
    # print("Pred list: {}".format(pred))
    # [None, None, None, None, None]

    # use priority queue
    Queue = Min_Heap_Priority_Queue()
    # Q = priority_queue()
    Queue.push(MinHeapNode(start, 0, False))
    # Queue.printPQ()

    # print("----------------------------------------------------------------------------------")
    # print("Up until here works as expected.")
    # print("----------------------------------------------------------------------------------")

    """
        Passenger_condition is new modified feature that is used to begin the initialization for the second frame of 
        dijkstra once a passenger can be picked up. 
        Completed is used to aid in updating the pred and dist list for the second frame of dijkstra. 
        potential_start_indices is used to track which node is the node where the driver begins their ride with a passenger.
    """
    passenger_condition = False  # PASSENGER CONDITION BEGINNING OR END
    Queue.printPQ()
    completed = []
    potential_start_indices = []
    potential_start_index = None

    """
    2 Frames of Djikstra
    Frame 1: No passenger on the Car Yet 
        run as regular dijkstra 
    Frame 2: Once passenger is available as a path then create
        an updated dist called new_dist and pred called new_pred which updates the dist and pred for when a passenger can be picked up
        nodes in the Queue track in boolean whether they have been reached after traversing a passenger_node
        this conditions changes which lists to update (pred and dist or new_pred and new_dist)


    Most Simplest Problem: No Passenger road the Car throughout the Trip
    """

    while Queue.array:  # slice for now
        # while Q is not empty do
        u = Queue.pop_min()
        print(u.is_passenger_node)
        # --Significance of Completed-------------------------------------------------------
        # completed.append(u.index)
        # print("Completed: {}".format(completed))
        # ----------------------------------------------------------------------------------
        # dist = [0, 10, 7, 5, 37]
        # pred = [None, 0, 3, 0, 2]

        if passenger_condition == False and u.is_passenger_node:
            passenger_condition = True
            print("passenger_condition is True")
            # loop_start_index = u.index
            new_dist = dist[:]  # [:] prevents it from being a reference to dist
            new_pred = pred[:]
            new_completed = []

            # Erase if necessary
            # potential_start_indices = []

            # for i in completed[:len(completed)-1]:
            #     dist[i] = float('inf')
            # for i in completed[:len(completed)]:
            for i in completed:
                new_dist[i] = float('inf')
            # dist = [0, 10, 7, 5, 40]
            # new_dist = [inf, 10, inf, inf, 40]
            # pred = [None, 0, 3, 0, 2]
            print("Pred list: {}".format(pred))
            print("New Pred list: {}".format(new_pred))
            print("Dist list: {}".format(dist))
            print("New Dist list: {}".format(new_dist))
            # Queue.printPQ()
            # if u.index == loop_start_index: to skip if dist[u.index] == u.key:

        # IF ITS JUST BELOW THEN NO PASSENGERS
        # ----------------------------------------------------------------------------------
        # THIS IS THE BASE CASE
        if not u.is_passenger_node and dist[u.index] == u.key:
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
                    Queue.push(MinHeapNode(temp.vertexNo, dist[temp.vertexNo], temp.vertexNo in passengers))
                    # temp = temp.next
                    # Queue.printPQ()
                    # Q.push(v, key=dist[v])
                    if temp.vertexNo in passengers:
                        potential_start_indices.append(temp.vertexNo)
                    if temp.vertexNo in passengers and potential_start_index is None:
                        potential_start_index = temp.vertexNo
                temp = temp.next
            completed.append(u.index)
            print("Completed: {}".format(completed))
            print("Dist list: {}".format(dist))
            print("Pred list: {}".format(pred))
            Queue.printPQ()
            print("----------------------------------------------------------------------------------")
        # print(passenger_condition)
        elif u.is_passenger_node and new_dist[u.index] == u.key:  # 7 == 7
            # if dist[u] = key then
            temp = graph.adjgraph[u.index]
            while temp:  # halts on None for adj node
                # for each edge e that is adjacent to u do
                if new_dist[temp.vertexNo] >= new_dist[u.index] + temp.double:
                    # if new_dist[temp.vertexNo] > new_dist[u.index] + temp.double: cheap fix

                    # if dist[v] > dist[u] + w(u, v) then
                    new_dist[temp.vertexNo] = new_dist[u.index] + temp.double
                    # dist[v] = dist[u] + w(u, v)
                    new_pred[temp.vertexNo] = u.index
                    # pred[v] = u
                    Queue.push(MinHeapNode(temp.vertexNo, new_dist[temp.vertexNo],
                                           temp.vertexNo in passengers or u.is_passenger_node))
                    # temp = temp.next
                    # Queue.printPQ()
                    # Q.push(v, key=dist[v])

                    if temp.vertexNo in potential_start_indices:
                        potential_start_indices.remove(temp.vertexNo)

                temp = temp.next
            new_completed.append(u.index)
            Queue.printPQ()
            print("Completed: {}".format(completed))
            print("New Completed: {}".format(new_completed))
            print("Pred list: {}".format(pred))
            print("New Pred list: {}".format(new_pred))
            print("Dist list: {}".format(dist))
            print("New Dist list: {}".format(new_dist))
            print("----------------------------------------------------------------------------------")
    # [4, None, 0, 1, 3, 1]
    index = end
    # path = deque()
    # path.appendleft(end)

    optimal_route = []
    optimal_route.append(end)

    """
    Use pred to traverse bath the path from end to start node
    """
    if passenger_condition is False or dist[end] <= new_dist[end]:
        print("Dist list: {}".format(dist))
        print("Pred list: {}".format(pred))
        print("Completed list: {}".format(completed))
        while index is not start:
            # path.appendleft(pred[index])
            optimal_route.append(pred[index])
            index = pred[index]
        # final_path = []
        # for item in path:
        #     final_path.append(item)
    else:
        print("Completed: {}".format(completed))
        print("New Completed: {}".format(new_completed))
        print("Pred list: {}".format(pred))
        print("New Pred list: {}".format(new_pred))
        print("Dist list: {}".format(dist))
        print("New Dist list: {}".format(new_dist))
        if dist[end] is float('inf') or dist[end] > new_dist[end]:
            print(index)
            # print(path)
            print(potential_start_index)
            print(potential_start_indices)

            # while index is not start or new_pred[index] is not None:
            # # while index is not loop_start_index or new_pred[index] is not None:
            #     path.appendleft(new_pred[index])
            #     index = new_pred[index]
            #     # print(index)
            # the code below is retarded

            # if new_pred[start] is not None:
            #     while index is not potential_start_index:
            #         path.appendleft(new_pred[index])
            #         index = new_pred[index]

            # while index is not potential_start_index:

            while index not in potential_start_indices:
                # path.appendleft(new_pred[index])
                optimal_route.append(new_pred[index])
                index = new_pred[index]

            # while index is not start:

            # while index is not start or new_pred[index] is not None:
            # while index is not start and new_pred[index] not in passengers:

            while index is not start:  # new_pred[index] not in passengers:
                # path.appendleft(pred[index])
                optimal_route.append(pred[index])
                index = pred[index]

        # else: #case when there was a faster path without a passenger
        #     while index is not start:
        #         path.appendleft(pred[index])
        #         index = pred[index]
    # final_path = []
    # for item in path:
    #     final_path.append(item)

    optimal_route.reverse()

    print(potential_start_index)
    print(potential_start_indices)

    # print(path)
    # print(final_path)
    print(optimal_route)
    return optimal_route
    # return dist[1..n], pred[1..n]

    # return val = [0, 3, 2, 0, 3, 4]


if __name__ == "__main__":
    # ------------------------------------------------------------------------------------------------------------------




    """
    BASE CASE NO PASSENGERS
    """
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
    # THIS WAS A PROBLEM WHEN I WAS LAZY AND USING COMPLETED AS FINAL
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

    """
    NON REPEATER
    """
    # OK
    # Example 13
    # start = 0
    # end = 3
    # passengers = [2, 1]
    # roads = [(0, 1, 10, 10), (1, 3, 100, 1), (0, 2, 2, 2), (2, 3, 60, 60)]
    # result = [0, 1, 3] # Optimal route is 11 minutes
    # optimalRoute(start, end, passengers, roads)

    # OK
    # # Example 14
    # start = 0
    # end = 3
    # passengers = [2, 1]
    # roads = [(0, 1, 10, 10), (1, 3, 100, 1), (0, 2, 2, 2), (2, 3, 60, 60), (2, 1, 6, 3)]
    # result = [0, 2, 1, 3]  # Optimal route is 6 minutes
    # optimalRoute(start, end, passengers, roads)

    # OK
    # # Example 16
    start = 0
    end = 4
    passengers = [1, 3]
    roads = [
        (0, 1, 6, 5),
        (0, 2, 5, 1),
        (0, 4, 20, 18),
        (1, 4, 4, 4),
        (2, 3, 2, 2),
        (3, 4, 20, 2)
    ]
    # expected = [0, 2, 3, 4]

    # OK Passcon but faster without passenger
    # # Example 15
    # start = 2
    # end = 6
    # passengers = [0, 3, 5]
    # roads = [
    #     (0, 1, 10, 8),
    #     (2, 6, 5, 5),
    #     (1, 2, 11, 9),
    #     (2, 3, 12, 10),
    #     (3, 4, 15, 12),
    #     (4, 5, 18, 10),
    #     (5, 6, 20, 13),
    #     (6, 7, 30, 15)
    # ]
    # expected = [2, 6]

    # OK
    # # Example 3 Non_Pass FAIL 4 has no edges out?
    # Check Edges
    start = 6
    end = 7
    passengers = [4, 2, 9]
    roads = [
        (9, 0, 7, 4),
        (7, 4, 3, 1),
        (8, 7, 6, 1),
        (3, 5, 1, 1),
        (2, 9, 6, 4),
        (6, 4, 5, 4),
        (2, 4, 6, 2),
        (7, 3, 8, 7),
        (0, 9, 1, 1),
        (2, 3, 5, 5),
        (5, 3, 6, 6),
        (1, 9, 6, 5),
        (0, 7, 5, 5),
        (1, 8, 2, 1),
        (6, 9, 6, 5),
        (2, 1, 2, 2)
    ]
    # result = [6, 9, 0, 7]  # optimal route should take 15 mins
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

    # OK
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

    # OK I thnk because it goes to the regular no passenger return
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

    # Pred list: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    #        None, None, None, None, 54, None, None, None, 54, None, None, None, None, None, None, None, None, None, None,
    #        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    #        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    # New Pred list: [None, 44, 9, 22, 65, None, None, 38, 19, 48, 9, None, None, 36, None, None, None, None, 13, 48, 62, 25, 54,
    #        27, 51, 19, 54, 29, None, 24, None, None, None, None, None, 36, 23, 46, 49, None, 49, 7, 23, None, 60, None,
    #        13, None, 26, 61, 62, 56, None, 23, None, None, 19, None, None, None, 46, 1, 64, None, 41, 36, 37, 9, 2,
    #        None]
    # # Optimal route is 198 mins
    # result = [54, 26, 48, 19, 56, 51, 24, 29, 27, 23, 36, 13, 46, 60, 44, 1, 61, 49, 38, 7, 41, 64, 62]
    # optimalRoute(start, end, passengers, roads)

    # OK
    # NON-REPEATER/ REPEATER
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

    """
    PASSCON REPEAT
    """

    # OK
    # REPEATER
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

    # OK
    # # Example 17
    # start = 0
    # end = 3
    # passengers = [1]
    # roads = [
    #     (0, 1, 1, 1),
    #     (0, 2, 2, 1),
    #     (1, 2, 1, 1),
    #     (2, 0, 2, 1),
    #     (0, 3, 1000, 500)
    # ]
    # result = [0, 1, 2, 0, 3]

    # OK
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

    # OK
    # REPEATER
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
    #     (1, 4, 30, 20)]
    # expected = [0, 3, 2, 0, 3, 4]
    # optimalRoute(start, end, passengers, roads)

    #  OK
    # REPEATER
    # # Example 10
    start = 4
    end = 9
    passengers = [2, 6, 0]
    roads = [
        (4, 6, 30, 18),
        (3, 1, 8, 1),
        (9, 1, 9, 5),
        (1, 9, 30, 2),
        (8, 5, 12, 12),
        (8, 9, 8, 6),
        (1, 8, 25, 2),
        (2, 4, 4, 2),
        (6, 0, 25, 5),
        (4, 3, 6, 6),
        (1, 2, 15, 7)
    ]
    # result = [4, 3, 1, 2, 4, 3, 1, 9]

    optimalRoute(start, end, passengers, roads)