"""
1 Fast Backups (10 marks)
"""

class Node:
    def __init__(self, index):
        self.index = index
        self.next = None
        # track using edge or node?: go with node for now
        #self.flow = 0
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

# Function to print the graph
#     def print_graph(self):
#         for i in range(self.):
#             print("Adjacency list of vertex {}\n head".format(i), end="")
#             temp = self.graph[i]
#             while temp:
#                 print(" -> {}".format(temp.vertex), end="")
#                 temp = temp.next
#             print(" \n")

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

class AdjacencyMatrix:
    def __init__(self, NoOfVertices, flow_graph, capacity_graph):
        self.NoOfVertices = NoOfVertices
        self.flow_graph = flow_graph
        self.capacity_graph = capacity_graph


def maxThroughput(connections, maxIn, maxOut, origin, targets):
    no_upUntillTarget = len(maxIn) + 2
    source_index = no_upUntillTarget - 2
    target_index = no_upUntillTarget - 1
    fromTarget = len(maxIn) + 3
    total_nodes = 3 * len(maxIn) + 2


    #AjacencyMatrix-----------------------------------------------------
    AdjacencyMatrixGraphFlow = [[0 for y in range(total_nodes)] for x in range(total_nodes)]
    AdjacencyMatrixGraphCapacity = []
    print("Flow")
    print(AdjacencyMatrixGraphFlow)

    #[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

    #Martix Out Capacity 0->V
    for i in range(len(maxIn)):
        temp = [0]*total_nodes
        temp[no_upUntillTarget + (i*2) + 1] = maxOut[i]
        AdjacencyMatrixGraphCapacity.append(temp)

    #Matrix Add Source to Origin Node
    temp = [0]*total_nodes
    temp[origin] = float("inf")
    AdjacencyMatrixGraphCapacity.append(temp)

    #Matrix Add Target Node
    AdjacencyMatrixGraphCapacity.append([0]*total_nodes)

    #Matrix Add targets to Target
    for i in range(len(targets)):
        AdjacencyMatrixGraphCapacity[targets[i]][no_upUntillTarget - 1] = float("inf")

    #Matrix Add In -> 0 node     # maxIn = [5000, 3000, 3000, 3000, 2000]
    for i in range(len(maxIn)):
        tempIn = [0]*total_nodes
        tempOut = [0]*total_nodes
        tempIn[i] = maxIn[i]
        AdjacencyMatrixGraphCapacity.append(tempIn)
        AdjacencyMatrixGraphCapacity.append(tempOut)

    # print(AdjacencyMatrixGraphCapacity)
    #Matrix Add Out -> In capacity # connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000), (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]
    for i in range(len(connections)):  # node out -> in
        # print(no_upUntillTarget + (connections[i][0] * 2) + 1)
        # print(no_upUntillTarget + connections[i][1] * 2)
        AdjacencyMatrixGraphCapacity[no_upUntillTarget + (connections[i][0] * 2) + 1][no_upUntillTarget + connections[i][1] * 2] = connections[i][2]
        # graph.add_directed_edge(no_upUntillTarget + (connections[i][0] * 2) + 1,no_upUntillTarget + connections[i][1] * 2, connections[i][2], 0, connections[i][2])
    # print(len(AdjacencyMatrixGraphCapacity))
    print("Capacity")
    print(AdjacencyMatrixGraphCapacity)

    AdjacencyMatrixGraph = AdjacencyMatrix(total_nodes, AdjacencyMatrixGraphFlow, AdjacencyMatrixGraphCapacity)

    #AdjacencyList------------------------------------------------------


    graph = AdjacencyListGraph(total_nodes)
    # Add capacity nodes for IN and OUT for nodes 0-|V|
    for i in range(len(maxIn)):
        graph.add_directed_edge(no_upUntillTarget + i*2, i, maxIn[i], 0, maxIn[i])
        graph.add_directed_edge(i, no_upUntillTarget + (i*2) + 1, maxOut[i], 0, maxOut[i])
    # graph.print_graph()

    # Add nodes from to connect source to origin node DIRECTLY
        # graph.add_directed_edge(no_upUntillTarget - 2 , no_upUntillTarget + origin * 2, float("inf"), 0, float("inf"))
        # graph.add_directed_edge(no_upUntillTarget - 2 , origin, float("inf"), 0)
    graph.add_directed_edge(no_upUntillTarget - 2, origin, float("inf"), 0, float("inf"))
    #---------up untill here is indexed correctly ---------
    # graph.print_graph()
    # print(target_index)

    # targets = [4, 2] connect target nodes to TARGET Node
    for i in range(len(targets)):
        graph.add_directed_edge(targets[i], no_upUntillTarget - 1, float("inf"), 0, float("inf"))
    #---------up untill here is indexed correctly ---------
    # graph.print_graph()


    # connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000),
    #                (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]

    for i in range(len(connections)): #node out -> in
        graph.add_directed_edge(no_upUntillTarget + (connections[i][0] * 2) + 1, no_upUntillTarget + connections[i][1] * 2, connections[i][2], 0, connections[i][2])
    #---------up untill here is indexed correctly ---------

    # print("Next using Array List")
    # graph.print_graph()

    #run fordfulkerson

    # BFS(graph, source_index, target_index)

    # print(MAX_FLOW(graph, source_index, target_index))
    return MAX_FLOW(graph, AdjacencyMatrixGraph, source_index, target_index)
    # return MAX_FLOW(graph, source_index, target_index)

    #get sum of maxthroughput in target nodes
    #return sum


























def BFS(adjlistgraph, graph, queue, visited, source, target, bottleneck, pred, max_flow_finder):
    """
    3: if u = t then return bottleneck // We hit the sink, so we have an augmenting path
    4:      visited[u] = true
    5:      for each edge e = (u, v ) adjacent to u do
    6:          residual = e .capacity - e .flow
    7:          if residual > 0 and not visited[v] then
    8:              augment = DFS(v , t , min(bottleneck, residual))
    9:              if augment > 0 then // We found an augmenting path - add the flow
    10:                 e .flow += augment
    11:                 e .reverse.flow -= augment
    12:                 return augment
    13:     return 0 // We could not find an augmenting path"""


    # if source == target:
    #     return bottleneck
    # d3:      if s = t then return bottleneck // We hit the sink, so we have an augmenting path

    # visited = [False] * graph.NoOfVertices
    # 2:      visited[1..n] = false
    visited[source] = True
    # 3:      visited[s] = true
    # 4:      queue = Queue()

    # order_visited = []
    # order_visited.append(source)

    # queue.append(source)
    # print(queue)
    # 5:      queue.push(s)
    while queue:
    # 6:      while queue is not empty do
        u_index = queue.pop(0)
    # 7:          u = queue.pop()
        u_adj_edge = adjlistgraph.adjgraph[u_index]
        while u_adj_edge:
    # 8.          for each vertex v adjacent to u do
            residual = graph.capacity_graph[u_index][u_adj_edge.index] - graph.flow_graph[u_index][u_adj_edge.index]
            # residual = u_adj_edge.capacity - u_adj_edge.reversible_backward_edge
    # d6:          residual = e.capacity - e.flow

            # u_adj_edge.residual_forward_edge = forward
            # u_adj_edge.reversible_backward_edge = backward
            # u_adj_edge.capacity = capacity
            if residual > 0 and visited[u_adj_edge.index] is False:
    # 9:              if not visited[v] then
    # d7:          if residual > 0 and not visited[v] then
                pred[u_adj_edge.index] = u_index
                visited[u_adj_edge.index] = True
                max_flow_finder[u_adj_edge.index] = min(max_flow_finder[u_index], residual)
                if u_adj_edge.index != target:
                    queue.append(u_adj_edge.index)
                else:
                    return max_flow_finder[target], pred
            u_adj_edge = u_adj_edge.next

    return 0, pred
    #             augment = BFS(graph, queue, visited, u_adj_edge.index, target, min(bottleneck, residual))
    # # d8:              augment = DFS(v , t , min(bottleneck, residual))
    #             if augment > 0:
    # # d9:              if augment > 0 then // We found an augmenting path - add the flow
    #                 u_adj_edge.reversible_backward_edge += augment
    # # d10:                 e.flow += augment
    #                 u_adj_edge.residual_forward_edge -= augment
    # # d11:                 e.reverse.flow -= augment
    #                 return augment
    # # d12:                 return augment
    #             visited[u_adj_edge.index] = True
    # # 10:                 visited[v] = true
    #             queue.append(u_adj_edge.index)
    # # 11:                 queue.push(v)
    # # #           order_visited.append(u_adj_edge.index)
    #         u_adj_edge = u_adj_edge.next
    #
    # # print(order_visited)
    #     return 0

    # E = [[1, 2], [2, 3], [3], []]
    # C = [[0, 1000000, 1000000, 0], [0, 0, 1, 1000000], [0, 0, 0, 1000000], [0, 0, 0, 0]]
    # s = 0
    # t = 3
    # n = len(C) #4 vertices
    # P = [-2,-1,-1,-1]
    # M = [inf, 0, 0, 0]
    #Q = [s]
    # def BFSEK(E, C, s, t, F, P, M, BFSq):
    # while (len(BFSq) > 0):
    #     u = BFSq.pop(0)
    #     for v in E[u]:
    #         if C[u][v] - F[u][v] > 0 and P[v] == -1:
    #             P[v] = u
    #             M[v] = min(M[u], C[u][v] - F[u][v])
    #             if v != t:
    #                 BFSq.append(v)
    #             else:
    #                 return M[t], P
    # return 0, P


def MAX_FLOW(adjlistgraph, graph, source, target):
    """
    # 15: function MAX_FLOW(G = (V,E ),s,t )
    # 16:     flow = 0
    # 17:     do
    # 18:         visited[1..n] = false
    # 19:         augment = DFS(s,t ,∞)
    # 20:         flow += augment
    # 21:     loop while augment > 0
    # 22:     return flow
    """
    # Algorithm 61 Ford-Fulkerson implemented using depth-first search
    # Ford-Fulkerson implemented using breadth-first search

    # graph.print_graph()

    flow = 0
    # 16:     flow = 0
    # 17:     do

    pred = [-1] * graph.NoOfVertices
    pred[source] = -2

    #Think about M max
    max_flow_finder = [0] * graph.NoOfVertices
    max_flow_finder[source] = float('inf')

    queue = []
    queue.append(source)
    visited = [False] * graph.NoOfVertices #[False, False, False, False, False, False..., False]
    # 18:         visited[1..n] = false


    augment, pred = BFS(adjlistgraph, graph, queue, visited, source, target, float('Inf'), pred, max_flow_finder)
    flow += augment
    v = target
    while v != source:
        u = pred[v]
        graph.flow_graph[u][v] = graph.flow_graph[u][v] + augment
        graph.flow_graph[v][u] = graph.flow_graph[v][u] - augment
        v = u
    # 19:         augment = DFS(s,t ,∞)
    print("augment")
    print(augment)

    # 21:     loop while augment > 0
    print("flow")
    print(flow)
    print("----------------------------------------------------")
    while augment > 0:
        pred = [-1] * graph.NoOfVertices
        pred[source] = -2
        max_flow_finder = [0] * graph.NoOfVertices
        max_flow_finder[source] = float('inf')
        queue = []
        queue.append(source)

        visited = [False] * graph.NoOfVertices #[False, False, False, False, False, False..., False]
        # 18:         visited[1..n] = false

        augment, pred = BFS(adjlistgraph, graph, queue, visited, source, target, float('Inf'), pred, max_flow_finder)
        # 19:         augment = DFS(s,t ,∞)
        if augment == 0:
            break
        flow += augment
        v = target
        while v != source:
            u = pred[v]
            graph.flow_graph[u][v] = graph.flow_graph[u][v] + augment
            graph.flow_graph[v][u] = graph.flow_graph[v][u] - augment
            v = u
        print("augment")
        print(augment)
        print("flow")
        print(flow)
        print("----------------------------------------------------")
    # 20:         flow += augment
    # print(max_flow)
    # print(graph.adjgraph[3].reversible_backward_edge)

    # print("hey")
    print("FLOW")
    print(flow)
    return flow
    # 22:     return flow

   # E = [[1, 2], [2, 3], [3], []]
    # C = [[0, 1000000, 1000000, 0], [0, 0, 1, 1000000], [0, 0, 0, 1000000], [0, 0, 0, 0]]
    # s = 0
    # t = 3
    # n = len(C) #4 vertices


    # flow = 0
    # # F = [[0 for y in range(n)] for x in range(n)] Already Done
    # # print(F)
    # while True:
    #     Path = [-1 for x in range(n)]
    #     Path[source] = -2
    #     print(Path)
    #     M = [0 for x in range(n)]
    #     print(M)
    #     M[s] = decimal.Decimal('Infinity')
    #     BFSq = []
    #     BFSq.append(s)
    #     print(BFSq)
    #     pathFlow, Path = BFSEK(E, C, s, t, F, P, M, BFSq)
    #     print(pathFlow)
    #     print(Path)
    #     if pathFlow == 0:
    #         break
    #     flow = flow + pathFlow
    #     v = t
    #     while v != s:
    #         u = Path[v]
    #         F[u][v] = F[u][v] + pathFlow
    #         F[v][u] = F[v][u] - pathFlow
    #         v = u
    # return flow

if __name__ == '__main__':
    #ok
    # connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000),
    #                (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]
    # maxIn = [5000, 3000, 3000, 3000, 2000]
    # maxOut = [5000, 3000, 3000, 2500, 1500]
    # origin = 0
    # targets = [4, 2]
    # #4500

    # Your function should return the maximum possible data throughput from the
    # data centre origin to the data centres specified in targets.

    #ok
    # connections = [(0, 1, 10), (0, 2, 100), (1, 3, 50),
    #                (2, 3, 50)]
    # maxIn = [1, 60, 50, 7]
    # maxOut = [1, 60, 50, 7]
    # origin = 0
    # targets = [3]

    #ok
    # connections = [(0, 1, 10), (0, 2, 100), (1, 3, 50),
    #                (2, 3, 50)]
    # maxIn = [20, 60, 50, 7]
    # maxOut = [20, 60, 50, 7]
    # origin = 0
    # targets = [3]

    #failed
    # connections = [(0, 1, 10), (0, 2, 100), (1, 3, 50),
    #                (2, 3, 50)]
    # maxIn = [1, 60, 50, 7]
    # maxOut = [20, 60, 50, 7]
    # origin = 0
    # targets = [3]

    #ok
    # connections = [(0, 1, 20), (1, 2, 20)]
    # maxIn = [20, 5, 20]
    # maxOut = [20, 100, 20]
    # origin = 0
    # targets = [1]

    #ok
    # connections = [(0, 1, 50), (1, 2, 20), (1, 3, 35)]
    # maxIn = [60, 60, 10, 30]
    # maxOut = [60, 50, 30, 2]
    # origin = 0
    # targets = [2, 3]

    #Failed OK NOW
    # connections = [(0, 1, 16), (1, 2, 12), (2, 3, 20), (4, 1, 4), (5, 2, 7), (0, 4, 13), (4, 5, 14), (5, 3, 4),
    #                (5, 1, 9)]
    # # maxIn = [100] * len(connections)
    # maxIn = [100] * 6
    # # maxOut = [100] * len(connections)
    # maxOut = [100] * 6
    # origin = 0
    # targets = [3]
    #23

    maxThroughput(connections, maxIn, maxOut, origin, targets)


