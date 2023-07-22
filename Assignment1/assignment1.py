__author__ = "31165176"


"""
1 Should I give a ride? (10 marks)
"""
def optimalRoute(start, end, passengers, roads):
    """
        Function description: This function returns an output array containing integers that represent the optimal route
        to take from start to end which has the minimum total travel time through the use of a modified Dijkstra's
        Algorithm to accommodate for the case of when a passenger is picked up and the weights of the graph edges change.

    	Approach description: The main conditions in this problem was to accomodate for the changing edge weights after
    	a passenger is riding the car and how to find the shortest path from start to end when there are additional
    	difficulties arising from the updated edge weights. The solution implments Dijkstra's Algorithm from the course
    	notes but modifies it to take into account the change in how we track the predecessor and distance once we pick
    	up a passenger. There are primarily two cases for this where:
    	    1. if the relaxed node is a node that is not accessible with a passenger in the car then the nodes are
    	    values are updated in the arrays of the first frame of Dijkstra which are pred and dist. If no passengers are
    	    ever in the car through out the journey it would run like regular Dijkstra.
    	    2. if the relaxed node is a node that is accessible with a passenger in the car then the node's values are updated
    	    in a new dist and new pred array that take the distances and pred information from when a passenger can first be picked up.
    	    This second case functions as another frame of dijkstra in the sense that at most Dijkstra's algorithm runs
    	    twice in order to pop all the values in the priority queue.
    	Once all values are popped from the priority queue all that remains is to traverse the pred list
    	or pred list and new pred list, and return the final path.

        Time Complexity Breakdown:

            Given an input with |L| key locations and |R| roads,

            Pre-processing:

                Finding number of total vertices in roads Cost O(|R|)

                Directed Weighted Adjacency List construction Cost O(|R|)

            Modified Dijkstra section costs O(|R|log|L|), there are at most two rounds of Dijkstra running
                First without passengers, Second if passenger is found.

            Final processing:

                Traverse predecessor lists to find path Costs at most O(|R|)

            Total Time Complexity: O(|R|) + O(|R|) + O(|R|log|L|) + O(|R|) = O(|R|log|L|)

        Aux Space Complexity Breakdown:

            Given an input with |L| key locations and |R| roads,

            Directed Weighted Adjacency List Graph: O(|L| + |R|)

            Priority Queue: O(|R|)

            Dijkstra arrays: O(|L|)

            Final-processing: O(|R|)

            Total Aux Space Complexity = O(|L| + |R|) + O(|R|) + O(|L|) + O(|R|) = O(|L| + |R|)

    	Input:
    	    start: index for the start location of the drive
    	    end: index for the end location of the drive
    	    passengers: a list of integers that contains the indices where passengers are located
    	    roads: a List of tuples in which each tuple is a road represented in the form of:
    	    (road start location, road end location, time taken alone, time taken with passenger)

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

    # Need to set up adjacency list
    no_of_vertices = find_no_of_vertices(roads)

    carpoolgraph = CarpoolGraph(no_of_vertices)

    for i in range(len(roads)):
        # add edges: add_directed_edge(start, end, single, double)
        carpoolgraph.add_directed_edge(roads[i][0], roads[i][1], roads[i][2], roads[i][3])
    CarpoolDjikstra(carpoolgraph, start, end, passengers)


def find_no_of_vertices(roads):
    """
    Function description: This function returns an integer that is the total number of vertices in the roads list of tuples by
    finding the maximum value of all locations appearing in roads as the assignment specification specifies that
    location will be a value from 0,1,2....|L|-1.

    Input:
    	roads: a List of tuples in which each tuple is a road represented in the form of:
    	(road start location, road end location, time taken alone, time take with passenger)

    Output:
        An integer that is the total number of vertices in the roads list of tuples.
    """
    max = float('-inf')

    for i in range(len(roads)):
        if roads[i][0] >= max:
            max = roads[i][0]
        if roads[i][1] >= max:
            max = roads[i][1]
    return max + 1


class AdjacencyNode:
    """
    Class description: Class used to store the values of the roads where vertexNo is used to track the integer value of
    the end vertex, next tracks the other edges connected to the start vertex, single stores the weight for when there
    is no passengers and double stores the weight for when there is a passenger riding the car. No functions for this
    class besides the constructor.
    """

    def __init__(self, value):
        """
        Function description: Constructor for a AdjacencyNode for Directed Weighted Adjacency List.

        Input:
            value: index value of the end vertex of a edge in a adajacency list
        """
        self.vertexNo = value
        self.next = None
        self.single = None
        self.double = None

class CarpoolGraph:
    """
    Class description: Class to create a Directed Weighted Adjacency List Graph for storing the roads details. Function
    for this class is add_directed_edge which creates a new adjacency list node to represent an edge.
    """

    def __init__(self, vertices):
        """
        Function description: Constructor for CarpoolGraph. Adjacency list stored using a list and AdjacencyNodes.

        Input:
        	vertices: a integer value for the total number of vertices the adjacency list will have.
        """
        self.NoOfVertices = vertices
        self.adjgraph = [None] * self.NoOfVertices

    def add_directed_edge(self, start, end, single, double):
        """
        Function description: This function creates an AdjacencyNode for the end vertex that is connected to the start
        index and maintains a reference of all the vertices connected to start by using next.

        Input:
        	start: an index of the start location of the road
        	end: an index of the end location of the road
        	single: the edge weight of using the road with no passengers
        	double: the edge weight of using the road with passengers

        """
        adjnode = AdjacencyNode(end)
        adjnode.next = self.adjgraph[start]
        adjnode.single = single
        adjnode.double = double
        self.adjgraph[start] = adjnode

class MinHeapNode:
    """
    Class description: Class used to store the priority queue value that is necessary to perform Dijkstra's
    Algorithm. Instead of using just values in the priority queue the nodes allow us to track whether the node can be
    accessed when the driver has a passenger riding the car. No other functions besides the constructor.
    """

    def __init__(self, index, key, is_passenger_node):
        """
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
    """
    Class description: Priority Queue using Min Heap, that is based off of the Max Heap in course notes "Binary Heap
    Operations" section page 25 and FIT1008 Max Heap Data Structure Code. Generic Priority Queue is Slightly modified so
    that it can track whether the node is accessible when having a passenger riding the car, and if true this is boolean
    value is used to change which weight value we access from the Adjacency List from single to doyble. As a MinHeap
    based priority queue, the operations that were necessary for the priority queue were:
        push: push new MinHeapNode called by Dijkstra's Algorithm
        min_rise: move the element up the heap until it satisfies the heap property for min-heap.
        swap: swap to the positions of two values in the Priority Queue array
        pop_min: pop minimum value in the priority queue called by Dijkstra's Algorithm
        fall: move an element down the heap until it satisfies the heap property of minheap
        smallest_child: helper function to find the index of i's child with the smallest value


    """

    def __init__(self):
        """
        Function description: Constructor for Min_Heap_Priority_Queue. Starts with array with None value as a placer for
        indexes to align with course notes pseudocode. The binary heap is represented through a flat array [1..n].
        """
        self.array = [None]
        self.n = 0

    # Keep
    def push(self, x):
        """
        Function description: Function to Insert an element into the heap. This is the Insert function Algorithm 11 from
        the same section in the course notes.
        Input:
        	x: a minheap node
        """
        self.array.append(x)
        self.n += 1
        self.min_rise(self.n)

    def min_rise(self, i):
        """
        Function description: Function to move the element up the heap until it satisfies the heap property for min-heap.
        Based on Algorithm 13 Heap: rise and FTI1008 Head DS but modified for min-heap. The parent node is at the index i // 2.
        Input:
        	i: index of element to move up.
        """
        while i > 1 and self.array[i].key < self.array[i // 2].key:
            self.swap(i, i // 2)
            i //= 2

    def swap(self, x, y):
        """
        Function description: Function to swap the position between two indices in the array. From non-implemented
        function that was used in the pseudocode of Algorithm 13 Heap: Rise.

        Input:
        	x: index of first position
        	y: index of second position
        """
        self.array[x], self.array[y] = self.array[y], self.array[x]

    # Keep
    def pop_min(self):
        """
        Function description: Function to remove the minimum value from the heap. Based on algorithm 12 Heap delete.
        """
        self.swap(1, self.n)
        minimum = self.array.pop(self.n)
        self.n = self.n - 1
        self.fall(1)
        # print("Pop [{},{}]".format(min.index, min.key))
        return minimum

    def fall(self, i):
        """
        Function description: Function to move an element down the heap until it satisfies the heap property of minheap.
        Based on Algorithm 14 Heap:Fall and FIT1008 Max Heap Data Structure Sink Function.

        Input:
            i: index of element to move.
        """

        while 2 * i <= self.n:
            child = self.smallest_child(i)
            if self.array[i].key <= self.array[child].key:
                break
            self.swap(i, child)
            i = child

    def smallest_child(self, i):
        """
        Function description: Function to find the index of i's child with the smallest value. Based on FIT1008 Max-Heap
        DS. For each node array[i], its children if they exist are the Left child node is array[2i] and the right child
        node is array[2i + 1].
        Input:
            i: index of element to move.
        """
        if 2 * i == self.n or self.array[2 * i].key < self.array[2 * i + 1].key:
            return 2 * i
        else:
            return 2 * i + 1

def CarpoolDjikstra(graph, start, end, passengers):
    """
        Function description: This function returns the optimal path from the start vertex to end vertex that minimizes
        the total time travelled. Runs two frames of Dijkstra if necessary: First if no passenger is yet to be picked up
        and it operates as a regular Dijkstra's Algorithm, Second if a passenger is picked up then it operates on an updated
        dist, and pred list in order to be able to reassign the values for faster now available paths.

    	Input:
    		graph: a Directed Weighted Adjacency List Graph for storing the roads details
    		start: index for the start location of the drive
    	    end: index for the end location of the drive
    	    passengers: a list of integers that contains the indices where passengers are located

    	Output:
    	    optimal_route: a list of integers that contains the optimal route to take from start to end.
    """

    """
        Set up first part of Dijkstra's Algorithm
            Set up dist list with positive inf values and assign start vertex value as 0
            Set up pred list with None values
            Set up priority queue and push start vertex with key of 0 and is_passenger_node as False because no 
            passengers will be present at start node according to the assignment brief.
    """
    dist = [float('inf')] * graph.NoOfVertices
    # dist[1..n] = ∞
    dist[start] = 0
    # dist[s] = 0

    pred = [None] * graph.NoOfVertices
    # pred[1..n] = 0

    # Use priority queue
    Queue = Min_Heap_Priority_Queue()
    # Q = priority_queue()
    Queue.push(MinHeapNode(start, 0, False))

    """
        Passenger_condition is a new modified feature that is used to begin the initialization for the second frame of 
        dijkstra once a passenger can be picked up. 
        Completed is used to aid in updating the pred and dist list for the second frame of dijkstra. 
        potential_start_indices is used to track which node is the node where the driver begins their ride with a passenger.
    """
    passenger_condition = False
    completed = []
    potential_start_indices = []

    """
    2 Frames of Djikstra
    Frame 1: No passenger on the Car Yet 
        run as regular dijkstra 
    Frame 2: Once passenger is available as a path then: 
        create an updated dist called new_dist and pred called new_pred which updates the dist and pred for when a 
        passenger can be picked up.
        Nodes in the Queue track in boolean whether they have been reached after traversing a passenger_node
        this conditions changes which lists to update (pred and dist or new_pred and new_dist)
    Most Simplest Problem: No Passenger road the Car throughout the Trip
    """
    while Queue.array[1:]:
        # while Q is not empty do
        u = Queue.pop_min()
        if passenger_condition == False and u.is_passenger_node:
            passenger_condition = True
            new_dist = dist[:]  # [:] prevents it from being a reference to dist
            new_pred = pred[:]
            new_completed = []
            for i in completed:
                new_dist[i] = float('inf')
        """IF ITS JUST BELOW THEN NO PASSENGERS
        THIS IS THE BASE CASE"""
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
                    # Q.push(v, key=dist[v])
                    if temp.vertexNo in passengers:
                        potential_start_indices.append(temp.vertexNo)
                temp = temp.next
            completed.append(u.index)
            """For condition BELOW it updates distance and pred for after having a passenger in the car."""
        elif u.is_passenger_node and new_dist[u.index] == u.key:  # 7 == 7
            # if dist[u] = key then
            temp = graph.adjgraph[u.index]
            while temp:  # halts on None for adj node
                if new_dist[temp.vertexNo] >= new_dist[u.index] + temp.double:
                    new_dist[temp.vertexNo] = new_dist[u.index] + temp.double
                    new_pred[temp.vertexNo] = u.index
                    Queue.push(MinHeapNode(temp.vertexNo, new_dist[temp.vertexNo],
                                           temp.vertexNo in passengers or u.is_passenger_node))
                    if temp.vertexNo in potential_start_indices:
                        potential_start_indices.remove(temp.vertexNo)
                temp = temp.next
            new_completed.append(u.index)
    index = end
    optimal_route = []
    optimal_route.append(end)

    """
    Use pred to traverse bath the path from end to start node
    """
    #    If passenger is never found or dist to get end without passenger was faster
    if passenger_condition is False or dist[end] <= new_dist[end]:
        while index is not start:
            optimal_route.append(pred[index])
            index = pred[index]
    else:
        # If having a passenger on the car helped reach the end faster
        if dist[end] is float('inf') or dist[end] > new_dist[end]:
            #Potential start indices stores locations where the passenger could have been first picked up
            #Used to initate the switch of traversal from new_pred to pred.
            while index not in potential_start_indices:
                optimal_route.append(new_pred[index])
                index = new_pred[index]
            while index is not start:
                optimal_route.append(pred[index])
                index = pred[index]
    optimal_route.reverse()
    # print(optimal_route)
    return optimal_route



"""
2 Repurposing Underused Workspace (Dynamic Programming) (10 marks)
"""

class MatrixPathNode:
    """
        Class description: A class that represents a node for each section in the decision array. Helps track the
        minimum total occupancy probability for that node and the also keeps track of its predecessor node to help find
        the final optimal section locations. No functionalities besides storing and tracking in the nodes itself.
    """

    def __init__(self, probability_total, pred_node_index, pred_node):
        """
        Function description: Constructor for a MatrixPathNode.

        Input:
            probability_total: current minimum total occupancy probability for that section

            pred_node_index: the index (i,j) for the optimal predecessor node/ section.

            pred_node: reference to optimal predecessor node in the decision array
        """
        self.probability_total = probability_total
        self.pred_node_index = pred_node_index
        self.pred_node = pred_node


def select_sections(occupancy_probability):
    """
        Function description: This function returns a list of two items, an integer which is the total
        occupancy for the selected n sections to be removed, and a list of n tuples in the form of (i,j), in which each
        tuple represents one section selected for removal. The return values are selected through the use of Dynamic
        Programming.

    	Approach description: Considering the 3 selection conditions and the fact that each aisle has n rows where n > m,
    	we can find the n sections from top to down that has the total minimum occupancy rate using Dynamic Programming.
        The solution implements the Dynamic Programming Strategy in which each row is a sub-problem, and its solutions
        are used to build upon to find the final row's solution. Bottom-Up Dynamic programming is implemented using the
        memoization stored in the decision_array. Finding the optimal path slightly differs depending on the value of m
        which is explained below but to put it simply it slightly alters the method of solving when checking same and
        adjacent columns. Each current section picks the available section with the minimum occupancy probability from
        the previous row and the decision array is built upon these optimal choices. Once we have found the optimal
        total minimum occupancy rate for each section (n*m) in the decision array, the decision array is used to find
        the minimum in the final row and that node is used to trace back along the path to find the optimal section
        locations.

    	Time Complexity Breakdown:

            Given n is the number of aisles/columns in the office and, m is the number of rows in the office

            Preprocessing to construct the decision array costs O(n) and setting up the first row of the decision array
            cost O(m)

            The Dynamic Programming deicison array constructing using the for loops costs O(nm) in the worst case for
            all 3 cases.

            Final Processing to get the output costs O(m) to ge the minimum Node for the last row and getting the
            sections_locations costs O(n).

            Total Complexity = O(n) + O(m) + O(nm) + O(m) + O(n) = O(nm)

        Space Complexity Breakdown:
            • given input occupancy_probability list of lists of O(nm) space.

            • decision_array for dynamic programming with O(nm) aux space.

            decision_array beats out other pre/final-processing space complexity so total is O(nm) space and O(nm) aux
            space.

    	Input: occupancy_probability: a list of lists, where each position in a row and a column represents the
    	occupancy probability of that location.

    	Output: A list of two items:
            • an integer value which is the total occupancy for the selected n section to be removed. In other words,
            the total occupancy of the n sections with the minimum total occupancy.
            • a list of n tuples in which each tuple represents the section removed from each row.

    	Time complexity: O(nm) time, where n is the number of rows, and m is the number of columns/aisles.

    	Space complexity: O(nm) space, where n is the number of rows, and m is the number of columns/aisles.
    """

    # m represents the number of columns in the office
    m = len(occupancy_probability[0])

    # n represents the number of rows in the office
    n = len(occupancy_probability)

    """ Decision_array for dynamic programming with O(nm) space. It is a n*m list of lists initialized with None.
    It will be used to store the optimal path and minimum total occupancy for each column up until its respective row.
    """
    decision_array = [[None for x in range(m)] for y in range(n)]

    """To find the best occupancy probability for each column in the first row is unnecessary as it will be optimal as 
    is. Therefore, simply replace each value of the first row of the decision array with each value set as 
    MatrixPathNode(occupancy_probability[0][i], None, None). 

    To summarize: a MatrixPathNode mainly serves to track the minimum occupancy probability total which is the optimal 
    sections up until that section that is available to that section, and also to track the index (i,j) of the 
    predecessor node which is the predecessor section that was optimal for the current section.

    So the first row for decision array in each column will have:
     MatrixPathNode("initial first row value", None because no predecessor, None because no predecessor).
    """
    first_row = []
    for i in range(m):
        first_row.append(MatrixPathNode(occupancy_probability[0][i], None, None))
    decision_array[0] = first_row

    """
    There are three cases that change how the problem is solved:
    If m == 1:
        The office would be one column straight down thus there is no need for solving further and take the path 
        straight down and that would be the optimal and only sections to remove.
    Else if m == 2:
        When deciding optimal:
            The current row, first column, can pick the minimum occupancy probability from:
                previous row, first column
                previous row, second column
            The current row, m column, can pick the minimum occupancy probability from:
                previous row, "m-1" column
                previous row, "m" column
    Else when m >= 3:
        When deciding optimal:
            The current row, first column, can pick the minimum occupancy probability from:
                previous row, first column
                previous row, second column
            The current row second to m-1 column, can pick the minimum occupancy probability from:
                previous row, current column - 1 
                previous row, current column 
                previous row, current column + 1
            The current row, "m" column, can pick the minimum occupancy probability from:
                previous row, m-1 column
                previous row, m column
    """
    if m == 1:  # Just take the straight path down.
        minimum_total_occupancy = 0
        sections_location = []
        for i in range(0, n):
            minimum_total_occupancy += occupancy_probability[i][0]
            sections_location.append((i, 0))
        # print([minimum_total_occupancy, sections_location])
        return [minimum_total_occupancy, sections_location]
    elif m == 2:
        for i in range(1, n):
            for j in range(0, m):
                if j == 0:
                    if decision_array[i - 1][0].probability_total <= decision_array[i - 1][1].probability_total:
                        pred_node_index = (i - 1, 0)
                        pred_node = decision_array[i - 1][0]
                        minimum_val = decision_array[i - 1][0].probability_total
                    else:
                        pred_node_index = (i - 1, 1)
                        pred_node = decision_array[i - 1][1]
                        minimum_val = decision_array[i - 1][1].probability_total
                    decision_array[i][0] = MatrixPathNode(occupancy_probability[i][0] + minimum_val, pred_node_index,
                                                          pred_node)
                else:  # if j == m - 1:
                    if decision_array[i - 1][m - 2].probability_total <= decision_array[i - 1][m - 1].probability_total:
                        pred_node_index = (i - 1, m - 2)
                        pred_node = decision_array[i - 1][m - 2]
                        minimum_val = decision_array[i - 1][m - 2].probability_total
                    else:
                        pred_node_index = (i - 1, m - 1)
                        pred_node = decision_array[i - 1][m - 1]
                        minimum_val = decision_array[i - 1][m - 1].probability_total

                    decision_array[i][m - 1] = MatrixPathNode(occupancy_probability[i][m - 1] + minimum_val,
                                                              pred_node_index, pred_node)
    else:
        for i in range(1, n):
            for j in range(0, m):
                if j == 0:
                    if decision_array[i - 1][0].probability_total <= decision_array[i - 1][1].probability_total:
                        pred_node_index = (i - 1, 0)
                        pred_node = decision_array[i - 1][0]
                        minimum_val = decision_array[i - 1][0].probability_total
                    else:
                        pred_node_index = (i - 1, 1)
                        pred_node = decision_array[i - 1][1]
                        minimum_val = decision_array[i - 1][1].probability_total
                    decision_array[i][0] = MatrixPathNode(occupancy_probability[i][0] + minimum_val, pred_node_index,
                                                          pred_node)
                elif j == m - 1:
                    if decision_array[i - 1][m - 2].probability_total <= decision_array[i - 1][m - 1].probability_total:
                        pred_node_index = (i - 1, m - 2)
                        pred_node = decision_array[i - 1][m - 2]
                        minimum_val = decision_array[i - 1][m - 2].probability_total
                    else:
                        pred_node_index = (i - 1, m - 1)
                        pred_node = decision_array[i - 1][m - 1]
                        minimum_val = decision_array[i - 1][m - 1].probability_total

                    decision_array[i][m - 1] = MatrixPathNode(occupancy_probability[i][m - 1] + minimum_val,
                                                              pred_node_index, pred_node)
                else:
                    if decision_array[i - 1][j - 1].probability_total < decision_array[i - 1][j].probability_total and decision_array[i - 1][j - 1].probability_total < decision_array[i - 1][j + 1].probability_total:
                        pred_node_index = (i - 1, j - 1)
                        pred_node = decision_array[i - 1][j - 1]
                        minimum_val = decision_array[i - 1][j - 1].probability_total
                    elif decision_array[i - 1][j].probability_total < decision_array[i - 1][j + 1].probability_total:
                        pred_node_index = (i - 1, j)
                        pred_node = decision_array[i - 1][j]
                        minimum_val = decision_array[i - 1][j].probability_total
                    else:
                        pred_node_index = (i - 1, j + 1)
                        pred_node = decision_array[i - 1][j + 1]
                        minimum_val = decision_array[i - 1][j + 1].probability_total
                    decision_array[i][j] = MatrixPathNode(occupancy_probability[i][j] + minimum_val, pred_node_index,
                                                          pred_node)

    """
    Find node with minimum total occupancy in the final row. Must check every element in the final row.
    """
    min_node = decision_array[n - 1][0]
    min_pos = (n - 1, 0)
    for j in range(1, m):
        if min_node.probability_total > decision_array[n - 1][j].probability_total:
            min_node = decision_array[n - 1][j]
            min_pos = (n - 1, j)

    """
    Get the list of of section locations using deque to popleft as we track backwards. 
    In the while loop below once the path_search_node becomes None that means there are no more predecessors and 
    the optimal section_locations has been found.
    """

    sections_location = []
    sections_location.append(min_pos)
    sections_location.append(min_node.pred_node_index)

    path_search_node = min_node.pred_node
    # print(path_search_node.pred_node_index)

    while path_search_node:  # while not None
        if path_search_node.pred_node_index:
            sections_location.append(path_search_node.pred_node_index)
        path_search_node = path_search_node.pred_node

    sections_location.reverse()

    minimum_total_occupancy = min_node.probability_total

    # print([minimum_total_occupancy, sections_location])

    return [minimum_total_occupancy, sections_location]



