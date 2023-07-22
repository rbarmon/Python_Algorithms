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



def maxThroughput(connections, maxIn, maxOut, origin, targets):

    # connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000),
    #                (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]
    # maxIn = [5000, 3000, 3000, 3000, 2000]
    # maxOut = [5000, 3000, 3000, 2500, 1500]
    # origin = 0
    # targets = [4, 2]
    # 4500

    # connect source to origin maxIn node
    # s --(inf)--> 0
    # origin = 0

    #connect REGULAR target
    # 2 --(inf)--> t
    # 4 --(inf)--> t
    # targets = [4, 2]

    # create nodes with maxIn and maxOut
    # 5000 - 0 - 5000
    # 3000 - 1 - 3000
    # 3000 - 2 - 3000
    # 3000 - 3 - 2500
    # 2000 - 4 - 1500
    # maxIn = [5000, 3000, 3000, 3000, 2000]
    # maxOut = [5000, 3000, 3000, 2500, 1500]

    #connect the nodes from respective maxOut node to maxIn node for connections
    # connections
    # connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000),
    #                (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]

    #adjListGraph(1)

    # 5 + 2 + 10 nodes in total
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5     s ->
    # 6     t ->
    # 7     5000 - 0
    # 8     0 - 5000
    # 9     3000 - 1
    # 10    1 - 3000
    # 11    3000 - 2
    # 12    2 - 3000
    # 13    3000 - 3
    # 14    3 - 2500
    # 15    2000 - 4
    # 16    4 - 1500

    no_upUntillTarget = len(maxIn) + 2
    source_index = no_upUntillTarget - 2
    target_index = no_upUntillTarget - 1
    fromTarget = len(maxIn) + 3
    total_nodes = 3 * len(maxIn) + 2
    graph = AdjacencyListGraph(total_nodes)
    #[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]

    for i in range(len(maxIn)):
        # graph.add_directed_edge(i, )
        graph.add_directed_edge(no_upUntillTarget + i*2, i, maxIn[i], 0, maxIn[i])
        graph.add_directed_edge(i, no_upUntillTarget + (i*2) + 1, maxOut[i], 0, maxOut[i])

    #---------up untill here is indexed correctly ---------

    # graph.print_graph()

    # origin = 0 connect source to origin IN node
    # graph.add_directed_edge(no_upUntillTarget - 2 , no_upUntillTarget + origin * 2, float("inf"), 0, float("inf"))
    graph.add_directed_edge(no_upUntillTarget - 2 , origin, float("inf"), 0, float("inf"))
    # graph.add_directed_edge(no_upUntillTarget - 2 , origin, float("inf"), 0)
    #---------up untill here is indexed correctly ---------

    # graph.print_graph()
    #
    # print(target_index)
    # targets = [4, 2] connect target nodes to TARGET
    for i in range(len(targets)):
        graph.add_directed_edge(targets[i], no_upUntillTarget - 1, float("inf"), 0, float("inf"))
    #---------up untill here is indexed correctly ---------
    # graph.print_graph()


    # connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000),
    #                (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]

    for i in range(len(connections)): #node out -> in
        graph.add_directed_edge(no_upUntillTarget + (connections[i][0] * 2) + 1, no_upUntillTarget + connections[i][1] * 2, connections[i][2], 0, connections[i][2])
    #---------up untill here is indexed correctly ---------
    graph.print_graph()

    #run fordfulkerson

    # BFS(graph, source_index, target_index)

    # print(MAX_FLOW(graph, source_index, target_index))
    return MAX_FLOW(graph, source_index, target_index)

    #get sum of maxthroughput in target nodes
    #return sum

























def BFS(graph, visited, source, target, bottleneck):
    if source == target:
        return bottleneck
    # d3:      if s = t then return bottleneck // We hit the sink, so we have an augmenting path

    # visited = [False] * graph.NoOfVertices
    # 2:      visited[1..n] = false
    visited[source] = True
    # 3:      visited[s] = true
    queue = []
    # 4:      queue = Queue()

    # order_visited = []
    # order_visited.append(source)

    queue.append(source)
    print(queue)
    # 5:      queue.push(s)
    while queue:
    # 6:      while queue is not empty do
        u_index = queue.pop(0)
    # 7:          u = queue.pop()
        u_adj_edge = graph.adjgraph[u_index]
        while u_adj_edge:
    # 8.          for each vertex v adjacent to u do

            residual = u_adj_edge.capacity - u_adj_edge.reversible_backward_edge
    # d6:          residual = e.capacity - e.flow

            # u_adj_edge.residual_forward_edge = forward
            # u_adj_edge.reversible_backward_edge = backward
            # u_adj_edge.capacity = capacity

            if residual > 0 and visited[u_adj_edge.index] is False:
    # 9:              if not visited[v] then
    # d7:          if residual > 0 and not visited[v] then

                augment = BFS(graph, visited, u_adj_edge.index, target, min(bottleneck, residual))
    # d8:              augment = DFS(v , t , min(bottleneck, residual))
                if augment > 0:
    # d9:              if augment > 0 then // We found an augmenting path - add the flow
                    u_adj_edge.reversible_backward_edge += augment
    # d10:                 e.flow += augment
                    u_adj_edge.residual_forward_edge -= augment
    # d11:                 e.reverse.flow -= augment
                    return augment
    # d12:                 return augment
                visited[u_adj_edge.index] = True
    # 10:                 visited[v] = true
                queue.append(u_adj_edge.index)
    # 11:                 queue.push(v)
    # #           order_visited.append(u_adj_edge.index)
            u_adj_edge = u_adj_edge.next

    # print(order_visited)
    return 0

def MAX_FLOW(graph, source, target):
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

    max_flow = 0

    # 17:     do
    visited = [False] * graph.NoOfVertices #[False, False, False, False, False, False..., False]
    # 18:         visited[1..n] = false
    augment = BFS(graph, visited, source, target, float('Inf'))
    # 19:         augment = DFS(s,t ,∞)
    print("augment")
    print(augment)
    max_flow += augment

    # 21:     loop while augment > 0
    print("max_flow")
    print(max_flow)
    print("----------------------------------------------------")
    while augment > 0:
        visited = [False] * graph.NoOfVertices #[False, False, False, False, False, False..., False]
        # 18:         visited[1..n] = false
        augment = BFS(graph, visited, source, target, float('Inf'))
        # 19:         augment = DFS(s,t ,∞)
        max_flow += augment
        print("augment")
        print(augment)
        print("----------------------------------------------------")
    # 20:         flow += augment
    # print(max_flow)
    # print(graph.adjgraph[3].reversible_backward_edge)

    # print("hey")
    return max_flow
    # 22:     return flow





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

    connections = [(0, 1, 16), (1, 2, 12), (2, 3, 20), (4, 1, 4), (5, 2, 7), (0, 4, 13), (4, 5, 14), (5, 3, 4),
                   (5, 1, 9)]
    # maxIn = [100] * len(connections)
    maxIn = [100] * 6
    # maxOut = [100] * len(connections)
    maxOut = [100] * 6
    origin = 0
    targets = [3]
    #23

    maxThroughput(connections, maxIn, maxOut, origin, targets)


