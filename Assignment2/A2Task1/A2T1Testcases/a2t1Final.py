"""
1 Fast Backups (10 marks)
"""
from collections import deque


class Node:
    def __init__(self, index):
        self.index = index
        self.next = None
        #residual capacity is forward edge
        self.residual_forward_edge = None
        #reversible flow is backward edge
        self.reversible_backward_edge = None
        self.capacity = None
class AdjacencyListGraph:

    def __init__(self, vertices):
        self.NoOfVertices = vertices
        self.adjgraph = [None] * self.NoOfVertices

    def add_directed_edge(self, start, end, forward, backward, capacity):
        node = Node(end)
        node.next = self.adjgraph[start]
        node.residual_forward_edge = forward
        node.reversible_backward_edge = backward
        node.capacity = capacity
        self.adjgraph[start] = node

    def print_graph(self):
        for i in range(self.NoOfVertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.adjgraph[i]
            while temp:
                print(" -> Vertex No: {}".format(temp.index), end="")
                print(".forward({}".format(temp.residual_forward_edge), end=")")
                print(".backward({}".format(temp.reversible_backward_edge), end=")")
                print(".capacity({}".format(temp.capacity), end=")")
                temp = temp.next
            print(" \n")
class SimpleNode:
    def __init__(self, index, forward, backward, capacity):
        self.index = index
        #residual capacity is forward edge
        self.residual_forward_edge = forward
        #reversible flow is backward edge
        self.reversible_backward_edge = backward
        self.capacity = capacity

class SimpleAdjacencyList:

    def __init__(self, vertices):
        self.NoOfVertices = vertices
        self.adjgraph = [[]] * self.NoOfVertices

    def add_directed_edge(self, start, end, forward, backward, capacity):
        self.adjgraph[start].append(SimpleNode(end, forward, backward, capacity))
    def print_graph(self):
        print(self.adjgraph)

class MatrixNode:
    def __init__(self, flow, capacity):
        self.flow = flow
        self.capacity = capacity

class AdjacencyMatrix:
    def __init__(self, NoOfVertices, flow_graph, capacity_graph):
        self.NoOfVertices = NoOfVertices
        self.flow_graph = flow_graph
        self.capacity_graph = capacity_graph

class AdjacencyMatrixBoth:
    def __init__(self, NoOfVertices, graph):
        self.NoOfVertices = NoOfVertices
        self.graph = graph


def maxThroughput(connections, maxIn, maxOut, origin, targets):


    #Necessary Node Position Tracking Variables:
    #Number of Nodes until 0->T
    no_upUntillTarget = len(maxIn) + 2
    #Position of the Source Node
    source_index = no_upUntillTarget - 2
    #Position of the Target Node
    target_index = no_upUntillTarget - 1
    #Next Position from the Target Node
    fromTarget = len(maxIn) + 3
    #Total Number of Nodes
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
        connect REGULAR target
        create nodes with maxIn and maxOut
        connect the nodes from respective maxOut node to maxIn node for connections
    """
    #AjacencyMatrix-----------------------------------------------------------------------------------------------------

    # Create Matrix for the size of total_nodes with all values set as zero as the Flow Graph
    AdjacencyMatrixGraphFlow = [[0 for y in range(total_nodes)] for x in range(total_nodes)]

    AdjacencyMatrixGraphCapacity = []
    AdjacencyMatrixGraphBoth = []

    # Matrix: Add the edges from the Data Centre Nodes to its Respective maxOut Node with the capacity defined in maxOut
    for i in range(len(maxIn)):
        #Just capacity
        temp = [0] * total_nodes
        temp[no_upUntillTarget + (i * 2) + 1] = maxOut[i]
        AdjacencyMatrixGraphCapacity.append(temp)
        #Both
        temp = [MatrixNode(0, 0)] * total_nodes
        temp[no_upUntillTarget + (i * 2) + 1] = MatrixNode(0, maxOut[i])
        AdjacencyMatrixGraphBoth.append(temp)

    # Matrix: Add Source Node to Origin Node with a Capacity of Infinity
    # Just capacity
    temp = [0] * total_nodes
    temp[origin] = float("inf")
    AdjacencyMatrixGraphCapacity.append(temp)
    # Both
    temp = [MatrixNode(0, 0)] * total_nodes
    temp[origin] = MatrixNode(0, float("inf"))
    AdjacencyMatrixGraphBoth.append(temp)

    # Matrix: Add Target Node which doesn't have directed edge towards anything so all zero capacity
    # Just capacity
    AdjacencyMatrixGraphCapacity.append([0] * total_nodes)
    # Both
    AdjacencyMatrixGraphBoth.append([MatrixNode(0, 0)] * total_nodes)


    # Matrix: Connect target node in targets list to Target Node with a directed edge with capacity of Infinity
    for i in range(len(targets)):
        # Just capacity
        AdjacencyMatrixGraphCapacity[targets[i]][no_upUntillTarget - 1] = float("inf")
        # Both
        AdjacencyMatrixGraphBoth[targets[i]][no_upUntillTarget - 1].capacity = float("inf")


    # Matrix: Add both maxIn and maxNode for each data centre node. Connect maxIn node to its respective data centre node
    for i in range(len(maxIn)):
        # Just capacity
        tempIn = [0] * total_nodes
        tempOut = [0] * total_nodes
        tempIn[i] = maxIn[i]
        AdjacencyMatrixGraphCapacity.append(tempIn)
        AdjacencyMatrixGraphCapacity.append(tempOut)
        # Both
        tempIn = [MatrixNode(0, 0)] * total_nodes
        tempOut = [MatrixNode(0, 0)] * total_nodes
        tempIn[i] = MatrixNode(0, maxIn[i])
        AdjacencyMatrixGraphBoth.append(tempIn)
        AdjacencyMatrixGraphBoth.append(tempOut)

    # Matrix: Set Out -> In capacity
    for i in range(len(connections)):
        # Just capacity
        AdjacencyMatrixGraphCapacity[no_upUntillTarget + (connections[i][0] * 2) + 1][
            no_upUntillTarget + connections[i][1] * 2] = connections[i][2]
        # Both
        AdjacencyMatrixGraphBoth[no_upUntillTarget + (connections[i][0] * 2) + 1][
            no_upUntillTarget + connections[i][1] * 2] = MatrixNode(0, connections[i][2])


    #AdjacencyList------------------------------------------------------------------------------------------------------
    """
    Steps taken to create graph:
        
    """
    graph = AdjacencyListGraph(total_nodes)
    simple_al_graph = SimpleAdjacencyList(total_nodes)

    # AdjacencyList: For nodes 0-|D| created edges from maxIn to Data Centre Node, and Data Centre to maxOut nodes
    for i in range(len(maxIn)):
        #Using the Next Method
        graph.add_directed_edge(no_upUntillTarget + i*2, i, maxIn[i], 0, maxIn[i])
        graph.add_directed_edge(i, no_upUntillTarget + (i*2) + 1, maxOut[i], 0, maxOut[i])
        #Simpler Way
        simple_al_graph.add_directed_edge(no_upUntillTarget + i*2, i, maxIn[i], 0, maxIn[i])
        simple_al_graph.add_directed_edge(i, no_upUntillTarget + (i*2) + 1, maxOut[i], 0, maxOut[i])

    # AdjacencyList: Add nodes from to connect source to origin node DIRECTLY
    graph.add_directed_edge(no_upUntillTarget - 2, origin, float("inf"), 0, float("inf"))
    simple_al_graph.add_directed_edge(no_upUntillTarget - 2, origin, float("inf"), 0, float("inf"))

    # AdjacencyList: Connect target nodes to TARGET Node
    for i in range(len(targets)):
        graph.add_directed_edge(targets[i], no_upUntillTarget - 1, float("inf"), 0, float("inf"))
        simple_al_graph.add_directed_edge(targets[i], no_upUntillTarget - 1, float("inf"), 0, float("inf"))

    # AdjacencyList: Connect the data centres from its respective Out to the In node of the other node.
    for i in range(len(connections)): #node out -> in
        graph.add_directed_edge(no_upUntillTarget + (connections[i][0] * 2) + 1, no_upUntillTarget + connections[i][1] * 2, connections[i][2], 0, connections[i][2])
        simple_al_graph.add_directed_edge(no_upUntillTarget + (connections[i][0] * 2) + 1, no_upUntillTarget + connections[i][1] * 2, connections[i][2], 0, connections[i][2])

    """Now Call the Max Flow method to get the maxthroughput from the source to target node and return this maxthroughput
    """

    AdjacencyMatrixGraph = AdjacencyMatrix(total_nodes, AdjacencyMatrixGraphFlow, AdjacencyMatrixGraphCapacity)
    AdjacencyMatrixBothGraph = AdjacencyMatrixBoth(total_nodes, AdjacencyMatrixGraphBoth)

    print("Capacity")
    print(AdjacencyMatrixGraphCapacity)
    print("Both")
    print(AdjacencyMatrixGraphBoth)
    graph.print_graph()
    simple_al_graph.print_graph()


    # print(MAX_FLOW(graph, AdjacencyMatrixGraph, source_index, target_index))
    return MAX_FLOW(graph, AdjacencyMatrixGraph, source_index, target_index)
    # return MAX_FLOW(graph, AdjacencyMatrixGraph, source_index, target_index)
    # return MAX_FLOW(graph, source_index, target_index)


def BFS(adjlistgraph, graph, source, target, pred, max_flow_finder):

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
        # for i in range(len(adjlistgraph[u_index])):
        u_adj_edge = adjlistgraph.adjgraph[u_index]
        while u_adj_edge:
            # d6:          residual = e.capacity - e.flow
            residual = graph.capacity_graph[u_index][u_adj_edge.index] - graph.flow_graph[u_index][u_adj_edge.index]
            # residual = graph[u_index][adjlistgraph[u_index][i].index].capacity - graph[u_index][adjlistgraph[u_index][i].index].flow
            # d7:          if residual > 0 and not visited[v] then
            if residual > 0 and visited[u_adj_edge.index] is False:
            # if residual > 0 and visited[adjlistgraph[u_index][i].index] is False:
            #     pred[adjlistgraph[u_index][i].index] = u_index
            #     visited[adjlistgraph[u_index][i].index] = True
            #     queue.append(adjlistgraph[u_index][i].index)
            #     max_flow_finder[adjlistgraph[u_index][i].index] = min(max_flow_finder[u_index], residual)
                pred[u_adj_edge.index] = u_index
                visited[u_adj_edge.index] = True
                max_flow_finder[u_adj_edge.index] = min(max_flow_finder[u_index], residual)
                queue.append(u_adj_edge.index)
            # if adjlistgraph[u_index][i].index == target:
                if u_adj_edge.index == target:
                        return max_flow_finder[target], pred
            u_adj_edge = u_adj_edge.next
    return 0, pred



def MAX_FLOW(adjlistgraph, graph, source, target):
    # 16:     flow = 0
    flow = 0
    #List to track the predecessor node for nodes in a path
    pred = [-1] * graph.NoOfVertices
    # pred[source] = -2
    max_flow_finder = [0] * graph.NoOfVertices
    max_flow_finder[source] = float('inf')

    augment, pred = BFS(adjlistgraph, graph, source, target, pred, max_flow_finder)
    flow += augment
    v = target
    while v != source and augment != 0:
        u = pred[v]
        # graph.graph[u][v_index].flow = graph.graph[u][v_index].flow + augment
        # graph.graph[v][v_index].flow = graph.graph[v][v_index].flow - augment
        graph.flow_graph[u][v] = graph.flow_graph[u][v] + augment
        graph.flow_graph[v][u] = graph.flow_graph[v][u] - augment
        v = u
    while augment > 0:
        # List to track the predecessor node for nodes in a path
        pred = [-1] * graph.NoOfVertices
        # pred[source] = -2
        max_flow_finder = [0] * graph.NoOfVertices
        max_flow_finder[source] = float('inf')

        augment, pred = BFS(adjlistgraph, graph, source, target, pred, max_flow_finder)
        if augment == 0:
            break
        flow += augment
        v = target
        while v != source:
            u = pred[v]
            # graph.graph[u][v_index].flow = graph.graph[u][v_index].flow + augment
            # graph.graph[v][v_index].flow = graph.graph[v][v_index].flow - augment
            graph.flow_graph[u][v] = graph.flow_graph[u][v] + augment
            graph.flow_graph[v][u] = graph.flow_graph[v][u] - augment
            v = u
    return flow





if __name__ == '__main__':
    connections = [(0, 1, 16), (1, 2, 12), (2, 3, 20), (4, 1, 4), (5, 2, 7), (0, 4, 13), (4, 5, 14), (5, 3, 4),
                   (5, 1, 9)]
    # maxIn = [100] * len(connections)
    maxIn = [100] * 6
    # maxOut = [100] * len(connections)
    maxOut = [100] * 6
    origin = 0
    targets = [3]
    maxThroughput(connections, maxIn, maxOut, origin, targets)


