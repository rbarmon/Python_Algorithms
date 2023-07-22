__author__ = "31165176"

"""
1 Fast Backups (10 marks)
"""
from collections import deque
class Node:
    """
    Class description: Node class that represents a Node in the Adjacency List Graph
    """
    def __init__(self, index):
        """
        Function description: Constructor for the Node Class
        """
        self.index = index
        self.next = None #next is used to chain the adjacent nodes together
        self.residual_forward_edge = None  #residual capacity is forward edge
        self.reversible_backward_edge = None #reversible flow is backward edge
        self.capacity = None #Predefined Capacity
class AdjacencyListGraph:
    """
    Class description: Adjacency List that is used for iterating through the adjacent edges of the specific Node
    """
    def __init__(self, vertices):
        """
        Function description: Constructor for the AdjacencyListGraph Class
        """
        self.NoOfVertices = vertices
        self.adjgraph = [None] * self.NoOfVertices

    def add_directed_edge(self, start, end, forward, backward, capacity):
        """
        Function description: Function that is used to add a directed edge between start and end node.
        """
        node = Node(end)
        node.next = self.adjgraph[start]
        node.residual_forward_edge = forward
        node.reversible_backward_edge = backward
        node.capacity = capacity
        self.adjgraph[start] = node

class AdjacencyMatrix:
    """
    Class description: AdjacencyMatrix is the main graph class that is used to track the flow and capacity necessary to
    run the Edmonds Karp Algorithm. It has 2 matrices, flow_graph representing the flow between vertices and capacity_graph
    representing the predefined capacity between vertices.
    """
    def __init__(self, NoOfVertices, flow_graph, capacity_graph):
        self.NoOfVertices = NoOfVertices
        self.flow_graph = flow_graph
        self.capacity_graph = capacity_graph


def maxThroughput(connections, maxIn, maxOut, origin, targets):
    """
        Function description: This function returns an output integer that represents the maximum possible data
        throughput from the origin data centre to the data centres specified in the target list.

        Approach description: The main point of this problem was identifying how and what kind of graph structure is
        necessary to perform network flow.

        • There are |D| data centres and each data centre has a limit on how much data they can receive and send thus requiring
        nodes and edges that limit the capacity in the form of maxOut node and maxIn node.
        • There needs to be a necessary source node that connects to the origin to run Max_Flow.
        • There needs to be a necessary target node that is on the receiving end of an edge from the data centres in the
         targets list.
        • Make the connection from the maxOut node to the maxIn node for the connections in the connections list.

        These points established that the problem is a straightforward max flow problem but the next problem is the
        complexity constraints requiring that the algorithm must be completed in O(|D| · |C|^2).

            To explain the complexity O(|D| · |C|^2):
                |D| = len(maxOut) =  Basically number of Vertices |V|
                |C| =  len(connections) = Basically number of Edges |E|

        In otherwords O(|D| · |C|^2) is  O(|V ||E |^2 ) which would be the time complexity for the Edmonds Karp
        Algorithm implementation of the max flow problem. Edmonds Karp Algorithm is faster than the Ford Fulkerson
        method that uses DFS in the worst case because it selects the shortest augmenting path.

        So certain adjustments needed to be implemented so that BFS can be used instead of using Algorithm 61
        Ford-Fulkerson implemented using depth-first search, written in the course notes.
        Once the graph is set up the rest is a max flow problem, so it's about running the Edmonds Karp algorithm.

        Based on the Algorithm 61 Ford-Fulkerson implemented using depth-first search, Algorithm 28 Generic
        breadth-first search, Wikipedia Edmonds-Karp Algorithm
        https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm.

        Time Complexity Breakdown:

            Pre-Processing: Graph Construction takes O(total_nodes), where total_nodes is all the nodes necessary to run
            the max_flow algorithm includes datacentre nodes + source + target + maxIn and maxOut nodes(|D|*2) = O(|D|)

            Edmonds Karp Algorithm: O(|D| · |C|^2)

            Total Time Complexity: O(|D|) + O(|D| · |C|^2) = O(|D| · |C|^2)

        Aux Space Complexity Breakdown:

            Adjacency Matrix: O(total_nodes^2)

            Adjacency List: O(VE)

            Total Aux Space Complexity = O(VE) +  O(total_nodes^2) = O(total_nodes^2)

        Input:
            connections: a list of tuples,
            maxIn: a list of integers representing the limits on the amount of incoming data a data centre can receive
            maxOut: a list of integers representing the limits on the amount of outgoing data a data centre can send
            origin: integer, that represents the data centre where the backup request begins
            target: a list

     	Output:
            the maximum possible data throughput from the data centre origin to the data centres specified in targets.

     	Time complexity: O(|D| · |C|^2), where |D| is the number of data centres and |C| is the number of communication
     	channels

     	Aux space complexity: O(total_nodes^2)
    """

    # Necessary Node Position Tracking Variables:
    # Number of Nodes until 0->T
    no_upUntillTarget = len(maxIn) + 2
    # Position of the Source Node
    source_index = no_upUntillTarget - 2
    # Position of the Target Node
    target_index = no_upUntillTarget - 1
    # Next Position from the Target Node
    fromTarget = len(maxIn) + 3
    # Total Number of Nodes
    total_nodes = 3 * len(maxIn) + 2

    """
    Note (this explains the indexing of where each necessary node is in the graph):
        • Data Centre Nodes in the problem from 0...|D|-1 are in the Position 0...|D|-1 in the list of list 
        a.k.a 0...len(maxIn).
        • Source Node is in the position after the last data centre node so |D| a.k.a. source_index.
        • Target Node is in the position after the source node so |D| + 1 a.k.a. target_index.
        • MaxIn and MaxOut Nodes for each Data Centre Nodes in the problem from 0...|D|-1 are in the positions next to 
        each other for each node 0...|D|-1 beginning from the target node position until every last MaxIn and MaxOut 
        Nodes for each data centre node has been added. So from |D| + 2 ... total_nodes a.k.a. fromTarget...total_nodes
        • Each connection (maxOut node, maxIn node, capacity) is processed in this manner where the maxOut node makes a 
        connection to the respective maxIn node with a specified capacity. 

    Steps taken to create graph:
        connect source to origin maxIn node
        connect target nodes to REGULAR target
        create nodes with maxIn and maxOut
        connect the nodes from respective maxOut node to maxIn node for connections
    """

    # Create Matrix for the size of total_nodes with all values set as zero as the Flow Graph
    AdjacencyMatrixGraphFlow = [[0 for y in range(total_nodes)] for x in range(total_nodes)]
    AdjacencyMatrixGraphCapacity = []
    #Initialize AdjacencyList
    graph = AdjacencyListGraph(total_nodes)


    # Matrix: Add the edges from the Data Centre Nodes to its Respective maxOut Node with the capacity defined in maxOut
    for i in range(len(maxIn)):
        # Just capacity
        temp = [0] * total_nodes
        temp[no_upUntillTarget + (i * 2) + 1] = maxOut[i]
        AdjacencyMatrixGraphCapacity.append(temp)

        # Using the Next Method
        graph.add_directed_edge(no_upUntillTarget + i * 2, i, maxIn[i], 0, maxIn[i])
        graph.add_directed_edge(i, no_upUntillTarget + (i * 2) + 1, maxOut[i], 0, maxOut[i])


    # AdjacencyList: Add nodes from to connect source to origin node DIRECTLY
    graph.add_directed_edge(no_upUntillTarget - 2, origin, float("inf"), 0, float("inf"))

    # Matrix: Add Source Node to Origin Node with a Capacity of Infinity
    # Just capacity
    temp = [0] * total_nodes
    temp[origin] = float("inf")
    AdjacencyMatrixGraphCapacity.append(temp)


    # Matrix: Add Target Node which doesn't have directed edge towards anything so all zero capacity
    # Just capacity
    AdjacencyMatrixGraphCapacity.append([0] * total_nodes)


    # Matrix: Connect target node in targets list to Target Node with a directed edge with capacity of Infinity
    for i in range(len(targets)):
        # Just capacity
        AdjacencyMatrixGraphCapacity[targets[i]][no_upUntillTarget - 1] = float("inf")

        # AdjacencyList: Connect target nodes to TARGET Node
        graph.add_directed_edge(targets[i], no_upUntillTarget - 1, float("inf"), 0, float("inf"))


    # Matrix: Add both maxIn and maxNode for each data centre node. Connect maxIn node to its respective data centre node
    for i in range(len(maxIn)):
        # Just capacity
        tempIn = [0] * total_nodes
        tempOut = [0] * total_nodes
        tempIn[i] = maxIn[i]
        AdjacencyMatrixGraphCapacity.append(tempIn)
        AdjacencyMatrixGraphCapacity.append(tempOut)


    # Matrix: Set Out -> In capacity
    for i in range(len(connections)):
        # Just capacity
        AdjacencyMatrixGraphCapacity[no_upUntillTarget + (connections[i][0] * 2) + 1][
            no_upUntillTarget + connections[i][1] * 2] = connections[i][2]

        # AdjacencyList: Connect the data centres from its respective Out to the In node of the other node.
        graph.add_directed_edge(no_upUntillTarget + (connections[i][0] * 2) + 1,
                                no_upUntillTarget + connections[i][1] * 2, connections[i][2], 0, connections[i][2])

    """Now Call the Max Flow method to get the maxthroughput from the source to target node and return this maxthroughput
    """
    AdjacencyMatrixGraph = AdjacencyMatrix(total_nodes, AdjacencyMatrixGraphFlow, AdjacencyMatrixGraphCapacity)

    return MAX_FLOW(graph, AdjacencyMatrixGraph, source_index, target_index)

def BFS(adjlistgraph, graph, source, target, pred, min_flow_finder):
    """
    Function description: Function to run BFS that is necessary for Edmonds Karp algorithm. It returns the possible
    augment value that is possible for the found path and return the pred list that can be used to augment the flow for
    the specific path, doing this instead of using BFS that returns a boolean value for finding a path makes it more
    efficient because it doesn't require calling it multiple times.

    Based on the Algorithm 61 Ford-Fulkerson implemented using depth-first search, Algorithm 28 Generic
    breadth-first search, Wikipedia Edmonds-Karp Algorithm
    https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm.

    Input:
    adjlistgraph: AdjacencyListGraph
    graph: AdjacencyMatrix
    source: source index
    target: target index
    pred: list to store the predecessor vertex for the path
    min_flow_finder: list to find the smallest flow value that is possible to augment

    Output:
    the max augment which will be the augment used to update the flow.
    the pred list for tracking the predecessor nodes.
    """

    # 2:      visited[1..n] = false
    visited = [False] * graph.NoOfVertices
    # 3:      visited[s] = true
    visited[source] = True
    # 4:      queue = Queue()
    queue = deque()
    # 5:      queue.push(s)
    queue.append(source)
    # 6:      while queue is not empty do
    while queue:
        # 7:          u = queue.pop()
        u_index = queue.popleft()
        # 8.          for each vertex v adjacent to u do
        u_adj_edge = adjlistgraph.adjgraph[u_index]
        while u_adj_edge:
            # d6:          residual = e.capacity - e.flow
            residual = graph.capacity_graph[u_index][u_adj_edge.index] - graph.flow_graph[u_index][u_adj_edge.index]
            # d7:          if residual > 0 and not visited[v] then
            if residual > 0 and visited[u_adj_edge.index] is False:
                pred[u_adj_edge.index] = u_index # Update pred
                visited[u_adj_edge.index] = True
                min_flow_finder[u_adj_edge.index] = min(min_flow_finder[u_index], residual) #Compare to find smallest augment
                queue.append(u_adj_edge.index)
                if u_adj_edge.index == target: #Ends with target
                        return min_flow_finder[target], pred
            u_adj_edge = u_adj_edge.next
    return 0, pred


def MAX_FLOW(adjlistgraph, graph, source, target):
    """
    Function description: Function to run the Edmonds Karp Algorithm for the max flow problem. Uses a pred list and
    min_flow_finder to update the flow values once a possible path has been found using BFS.

    Based on the Algorithm 61 Ford-Fulkerson implemented using depth-first search, Algorithm 28 Generic
    breadth-first search, Wikipedia Edmonds-Karp Algorithm
    https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm.

    Input:
    adjlistgraph: AdjacencyListGraph
    graph: AdjacencyMatrix
    source: source index
    target: target index

    Output:
    the maximum possible data throughput from the data centre origin to the data centres specified in targets.
    """
    # 16:     flow = 0
    flow = 0
    #17:      do
    # List to track the predecessor node for nodes in a path
    pred = [-1] * graph.NoOfVertices
    min_flow_finder = [0] * graph.NoOfVertices
    min_flow_finder[source] = float('inf') #set source as Infinity

    augment, pred = BFS(adjlistgraph, graph, source, target, pred, min_flow_finder)
    flow += augment
    y = target
    #Update the flow
    while y != source and augment != 0:
        x = pred[y]
        graph.flow_graph[x][y] = graph.flow_graph[x][y] + augment
        graph.flow_graph[y][x] = graph.flow_graph[y][x] - augment
        y = x
    #Call while augment > 0
    while augment > 0:
        # List to track the predecessor node for nodes in a path
        pred = [-1] * graph.NoOfVertices
        min_flow_finder = [0] * graph.NoOfVertices
        min_flow_finder[source] = float('inf')

        augment, pred = BFS(adjlistgraph, graph, source, target, pred, min_flow_finder)
        if augment == 0:
            break
        flow += augment
        y = target
        while y != source:
            x = pred[y]
            graph.flow_graph[x][y] = graph.flow_graph[x][y] + augment
            graph.flow_graph[y][x] = graph.flow_graph[y][x] - augment
            y = x
    return flow

"""
2 catGPT (10 marks)
"""

class CharacterNode:
    """
    Class description: Node Class structure used to store additional information necessary to construct the CatsTrie.
    Has max_sentence_frequency that is used to track the frequency of the sentence that is the most frequent that is
    reachable from that node.
    """

    def __init__(self, character):
        """
        Function description: Constructor for the CharacterNode.
        """
        self.connected_nodes = [None] * 26
        # self.connected_adj_list = ConnectedAdjacencyList(character, self.connected_nodes)
        self.character = character  # The string character
        self.frequency = 1  # The number of times the character occurs in the trie for that specific position
        self.max_sentence_frequency = 0
        self.parent = None
        self.sentence_counter = 0  # If the node is a end of sentence node represents the number of times the sentence is in sentences[]
        self.is_end = False  # Boolean that will be True if the node is the end of a sentence>
        self.sentence = None  # If the node is the end of sentence, will be the sentence in string form.

    def updateFrequency(self):
        """
        Function description: Function used to update the frequency count of the node by 1.
        """
        self.frequency += 1

    def last_letter(self):
        """
        Function description: Function used to change the is_end boolean to True
        """
        self.is_end = True

    def store_sentence_in_last_letter(self, sentence):
        """
        Function description: Function used to store the sentence in the node.

        sentence: string cat sentence
        """
        self.sentence = sentence

class CatsTrie:
    """
    Class description: Class structure to encapsulate all the cat sentences in the form of a Trie. Creates a multilayer
    tries using CharacterNode.
    """

    def __init__(self, sentences):
        """
        Function description: Constructor for CatsTrie class. Receives as input a list of strings and then generates a
        Trie branch for each string.

        Approach Description: Trie was generated using the generateTrie function which is explained below.
        Based on FIT2004 Lecture slide Week 11

        Time Complexity Breakdown:

            generateTrie = O(NM), for each character in the sentence in sentences puts it and updates the correct
            position based on the position index that is determined based on the ord() which was considered O(1)

            Total Time Complexity: O(NM) = O(NM)

        Aux Space Complexity Breakdown:

            generateTrie =  O(26 * NM), for each character in the sentence there is a list of size 26 to construct the trie

            Total Aux Space Complexity =  O(26 * NM) = O(NM)

        Input:
            sentences: a list of strings, where each string represents a cat sentence which is a string consisting of
            lower case characters from a to z.

        Time complexity:

        O(NM), where N is the number of sentence in sentences and M is the number of characters in the
            longest sentence.

        Aux space complexity:

        O(NM), where N is the number of sentence in sentences and M is the number of characters in the
            longest sentence.
        """
        self.N = len(sentences) # Number of sentences, where N is a positive integer.

        self.trie = CharacterNode(' ') #starting node of the CatsTrie

        self.generateTrie(sentences)  #call to generate trie based on sentences
        # You can assume that there is only a maximum of 26 unique cat words in total, represented as lower case characters from a to z.

    def generateTrie(self, sentences):
        """
        Function description: Function used to fill the Trie with the list of string sentences in the sentences list.
        General idea was that it starts at the top node of the trie and then expands to the bottom by creating more nodes.
        For characters that represent the end of a sentence a node that tracks the sentence frequency and sentence string
        is created.
        For every character that represents the end of a sentence code will traverse from the top of the trie to update
        the max_sentence_frequency used to determine which node has a higher frequency in autocomplete.

        Input:
            sentences: a list of strings, where each string represents a cat sentence which is a string consisting of
            lower case characters from a to z.

        Output: a full trie with all the sentences from the sentences list encapsulated into it.
        """


        for i in range(len(sentences)):
            for j in range(len(sentences[i])):
                # Add to trie directly for the first level of the trie
                if j == 0:
                    # If the position for the character is None meaning no character yet then create a New Node
                    if self.trie.connected_nodes[ord(sentences[i][j]) - 97] is None:
                        # If the letter is the last letter of the sentence. Create a node to indicate a word ends there
                        # give sentence counter = 1
                        if j == len(sentences[i]) - 1:
                            node = CharacterNode(sentences[i][j])
                            node.last_letter()
                            node.store_sentence_in_last_letter(sentences[i])
                            node.sentence_counter += 1
                            node.max_sentence_frequency += 1
                            node.parent = self.trie

                            if node.sentence_counter > self.trie.max_sentence_frequency:
                                val = node.sentence_counter
                                self.trie.max_sentence_frequency = val

                            self.trie.connected_nodes[ord(sentences[i][j]) - 97] = node
                            temp = self.trie.connected_nodes[ord(sentences[i][j]) - 97]
                        else:
                            # if not last letter then just create a node
                            node = CharacterNode(sentences[i][j])
                            node.parent = self.trie
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97] = node
                            temp = self.trie.connected_nodes[ord(sentences[i][j]) - 97]
                    # If the position for the character is not None then update the details of that node.
                    else:
                        # if the character is the last letter of the sentence update its details give the sentence_counter += 1
                        if j == len(sentences[i]) - 1:
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97].last_letter()
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97].store_sentence_in_last_letter(
                                sentences[i])
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97].updateFrequency()
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter += 1
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97].max_sentence_frequency += 1


                            if self.trie.connected_nodes[
                                ord(sentences[i][j]) - 97].sentence_counter > self.trie.max_sentence_frequency:
                                val = self.trie.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter
                                self.trie.max_sentence_frequency = val

                            temp = self.trie.connected_nodes[ord(sentences[i][j]) - 97]
                        # otherwise just update frequency
                        else:
                            self.trie.connected_nodes[ord(sentences[i][j]) - 97].updateFrequency()
                            temp = self.trie.connected_nodes[ord(sentences[i][j]) - 97]

                # If current character of the sentence is the last character of the sentence and its not on the first layer of the trie

                elif j == len(sentences[i]) - 1:

                    # If the position to enter the node is None that means its empty so add a Node that knows its the end
                    if temp.connected_nodes[ord(sentences[i][j]) - 97] is None:
                        node = CharacterNode(sentences[i][j])
                        node.last_letter()
                        node.store_sentence_in_last_letter(sentences[i])
                        node.sentence_counter += 1
                        node.max_sentence_frequency += 1
                        temp.connected_nodes[ord(sentences[i][j]) - 97] = node

                        for k in range(len(sentences[i])):
                            if k == 0:
                                if temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter > \
                                        self.trie.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency:
                                    val = temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter
                                    self.trie.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency = val

                                max_sentence_temp = self.trie.connected_nodes[ord(sentences[i][k]) - 97]
                            else:
                                if temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter > \
                                        max_sentence_temp.connected_nodes[
                                            ord(sentences[i][k]) - 97].max_sentence_frequency:

                                    val = temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter
                                    max_sentence_temp.connected_nodes[
                                        ord(sentences[i][k]) - 97].max_sentence_frequency = val

                                max_sentence_temp = max_sentence_temp.connected_nodes[ord(sentences[i][k]) - 97]

                        temp = temp.connected_nodes[ord(sentences[i][j]) - 97]


                    # Otherwise update node
                    else:
                        temp.connected_nodes[ord(sentences[i][j]) - 97].updateFrequency()
                        temp.connected_nodes[ord(sentences[i][j]) - 97].last_letter()
                        temp.connected_nodes[ord(sentences[i][j]) - 97].store_sentence_in_last_letter(sentences[i])
                        temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter += 1
                        temp.connected_nodes[ord(sentences[i][j]) - 97].max_sentence_frequency += 1

                        for k in range(len(sentences[i])):
                            if k == 0:
                                if temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter > \
                                        self.trie.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency:
                                    val = temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter
                                    self.trie.connected_nodes[ord(sentences[i][k]) - 97].max_sentence_frequency = val
                                max_sentence_temp = self.trie.connected_nodes[ord(sentences[i][k]) - 97]
                            elif k == len(sentences[i]) - 1:
                                break
                            else:
                                if temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter > \
                                        max_sentence_temp.connected_nodes[
                                            ord(sentences[i][k]) - 97].max_sentence_frequency:
                                    val = temp.connected_nodes[ord(sentences[i][j]) - 97].sentence_counter
                                    max_sentence_temp.connected_nodes[
                                        ord(sentences[i][k]) - 97].max_sentence_frequency = val
                                max_sentence_temp = max_sentence_temp.connected_nodes[ord(sentences[i][k]) - 97]

                        temp = temp.connected_nodes[ord(sentences[i][j]) - 97]

                # If the node isn't an end node then just apply the same conditions as above to either create or update a node
                else:
                    if temp.connected_nodes[ord(sentences[i][j]) - 97] is None:
                        # node = CharacterNode(sentences[i][j])
                        temp.connected_nodes[ord(sentences[i][j]) - 97] = CharacterNode(sentences[i][j])
                        temp = temp.connected_nodes[ord(sentences[i][j]) - 97]
                    else:
                        temp.connected_nodes[ord(sentences[i][j]) - 97].updateFrequency()
                        temp = temp.connected_nodes[ord(sentences[i][j]) - 97]

    def findSentence(self, temp):
        """
        Function description: Function used to find the sentence that would complete what the cat is saying. Handles the
        cases for finding the highest frequency and determening the lexicographically smaller string.

        Input:
            temp: a node at a specific point in the trie which is used to continue traversing the Trie to find the
            sentence that would complete the original prompt.

        Output:
            a complete sentence, that completes what the original prompt was saying for CatGPT.
        """
        while temp:
            max_freq = None
            # Find the node with the highest frequency in general
            for i in range(26):
                if temp.connected_nodes[i] is None:
                    continue
                # Max_freq for this node has not yet been found then just set
                elif max_freq == None:
                    max_freq = temp.connected_nodes[i]
                else:
                    if temp.connected_nodes[i].max_sentence_frequency > max_freq.max_sentence_frequency:
                        max_freq = temp.connected_nodes[i]
                    elif temp.connected_nodes[i].max_sentence_frequency < max_freq.max_sentence_frequency:
                        continue
                    elif temp.connected_nodes[i].max_sentence_frequency == max_freq.max_sentence_frequency:
                        # tiebreaker

                        if ord(temp.connected_nodes[i].character) < ord(max_freq.character):
                            max_freq = temp.connected_nodes[i]
                        else:
                            continue

            if max_freq == None:
                return temp.sentence
            else:
                if temp.is_end == True:
                    return self.branch_decider(temp)

                temp = max_freq

    def branch_decider(self, temp):
        """
        Function description: Function to help the findSentence function determine the sentence with the highest
        frequency for a specific branch of the trie that is necessary as a requirement for CatGPT

        Input:
            temp: a node at a specific point in the trie which is used to continue traversing the Trie.

        Output:
            a complete sentence, that completes what the original prompt was saying for CatGPT.
        """
        max_freq = None
        for i in range(26):
            if temp.connected_nodes[i] is None:
                continue
            # Max_freq for this node has not yet been found then just set
            elif max_freq == None:
                max_freq = temp.connected_nodes[i]

            else:
                if temp.connected_nodes[i].max_sentence_frequency > max_freq.max_sentence_frequency:
                    max_freq = temp.connected_nodes[i]
                elif temp.connected_nodes[i].max_sentence_frequency < max_freq.max_sentence_frequency:

                    continue
                elif temp.connected_nodes[i].max_sentence_frequency == max_freq.max_sentence_frequency:
                    # tiebreaker
                    if ord(temp.connected_nodes[i].character) < ord(max_freq.character):
                        max_freq = temp.connected_nodes[i]
                    else:
                        continue
        # if all_node in connected_nodes of temp is have a lower max_sentence_frequency than temp.sentence_count
        #     then return temp.sentence
        if max_freq == None:
            return temp.sentence
        elif temp.sentence_counter > max_freq.max_sentence_frequency:
            return temp.sentence
        # if equal do ord check just return because its the branch so will always be higher lexicographically
        elif temp.sentence_counter == max_freq.max_sentence_frequency:
            return temp.sentence
        # if there is a node with a higher freq call findSentence again:
        elif temp.sentence_counter < max_freq.max_sentence_frequency:

            #Recall findSentence if max_freq has a sentence with a higher frequency
            # temp = max_freq
            return self.findSentence(max_freq)

    def autoComplete(self, prompt):
        """
            Function description: Function used to complete and return the completed sentence of the prompt if
            applicable.

            Approach description: The function has three conditions it has to fulfill in order to function correctly.
            For every prompt the function should return:
                • If such a sentence does not exist, return None
                • If such a sentence exist, return the completed sentence with the highest frequency in the cat
                sentences list.
                • If there are multiple possible auto-complete sentences with the same highest frequency, then you would
                 return the lexicographically smaller string.

            Therefore, the function handles these conditions in the order of:
                1. Check if the sentence exists in the Trie, if not return None
                2. Call findSentence to find the sentence completes the prompt.
                3. Use both findSentence and branch_decider to fulfill the last 2 conditions for highest frequency and
                the lexicographically smaller string in this order.

            Time Complexity Breakdown:
                first part to traverse the trie using the prompt: O(X)

                calling findSentence: O(Y), in the worst case for checking all other branches

                Total Time Complexity: O(X) + O(Y) = O(X + Y)

            Aux Space Complexity Breakdown:

                O(Y) for the traversing of the temp pointers in the trie.

                Total Aux Space Complexity: O(Y) = O(Y)

            Input:
                prompt: is a string with characters in the set of [a...z] that represents the incomplete sentence that
                needs to be completed using the sentences in the Trie.

            Output:
                a string that represents the completed sentence from the prompt that fulfills the three conditions
                stated in the Approach description.

         	Time complexity:
         	O(X + Y): where X is the length of the prompt and Y is the length of the most frequent sentence in sentences
         	 that begins with the prompt.
         	O(X): where X is the length of the prompt, and if no such sentence exists to complete.

         	Aux space complexity:
         	O(Y): where Y is the length of the most frequent sentence in sentences that begins with the prompt.
        """
        temp = self.trie

        for i in range(len(prompt)):
            if temp.connected_nodes[ord(prompt[i]) - 97]:
                temp = temp.connected_nodes[ord(prompt[i]) - 97]
            else:
                # If prompt goes beyond the possible sentences in the trie then return None
                return None

        # Call findSentence for cases that handle determining #1. highest sentence frequency and 2. If same Frequency pick smaller lexico string
        return self.findSentence(temp)




