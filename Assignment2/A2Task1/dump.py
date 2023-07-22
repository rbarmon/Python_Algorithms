# 0
# 1
# 2
# 3
# 4
# s ->
# 6 t ->
#
#
# 0 1 2 3 4
#
# 7   0  0 * 2
# 8   1  0 * 2 + 1
# 9   2  1 * 2
# 10  3  1 * 2 + 1
# 11  4  2 * 2
# 12  5  2 * 2 + 1
# 13  6
# 14  7
# 15  8
# 16  9
# 17  10
#
#
# 4 + 0
# 4 +
# 4 +

# Algorithm 60 The Ford-Fulkerson method
# 1: function MAX_FLOW(G = (V,E ),s,t )
# 2:      Set initial flow f to 0 on all edges
# 3:      while there exists an augmenting path p in the residual network Gf do
# 4:          Augment the flow f along the augmenting path p as much as possible
# 5:      return f

# 15: function MAX_FLOW(G = (V,E ),s,t )
# 16:     flow = 0
# 17:     do
# 18:         visited[1..n] = false
# 19:         augment = DFS(s,t ,∞)
# 20:         flow += augment
# 21:     loop while augment > 0
# 22:     return flow


# 1: // DFS returns the capacity of the augmenting path found (or 0 if there are none left)
# 2: function DFS(u, t , bottleneck)
# 3:      if u = t then return bottleneck // We hit the sink, so we have an augmenting path
# 4:      visited[u] = true
# 5:      for each edge e = (u, v ) adjacent to u do
# 6:          residual = e .capacity - e .flow
# 7:          if residual > 0 and not visited[v] then
# 8:              augment = DFS(v , t , min(bottleneck, residual))
# 9:              if augment > 0 then // We found an augmenting path - add the flow
# 10:                 e .flow += augment
# 11:                 e .reverse.flow -= augment
# 12:                 return augment
# 13:     return 0 // We could not find an augmenting path

# Algorithm 28 Generic breadth - first search
# 1: function BFS(G=(V, E), s)
# 2:      visited[1..n] = false
# 3:      visited[s] = true
# 4:      queue = Queue()
# 5:      queue.push(s)
# 6:      while queue is not empty do
# 7:          u = queue.pop()
# 8.          for each vertex v adjacent to u do
# 9:              if not visited[v] then
# 10:                 visited[v] = true
# 11:                 queue.push(v)


# --------------------------------------------------------------------------------------------------

# visited[source] = true
# # 3:      visited[s] = true
# temp = graph[source]
# while temp:
#     # 5:      for each edge e = (u, v ) adjacent to u do
#     residual = temp.
#     temp = temp.next

# 2: function DFS(s, t , bottleneck)
# d3:      if s = t then return bottleneck // We hit the sink, so we have an augmenting path
# d4:      visited[s] = true
# d5:      for each edge e = (s, v ) adjacent to s do
# d6:          residual = e.capacity - e.flow
# d7:          if residual > 0 and not visited[v] then
# d8:              augment = DFS(v , t , min(bottleneck, residual))
# d9:              if augment > 0 then // We found an augmenting path - add the flow
# d10:                 e.flow += augment
# d11:                 e.reverse.flow -= augment
# d12:                 return augment
# d13:     return 0 // We could not find an augmenting path

# Algorithm 28 Generic breadth - first search
# 1: function BFS(G=(V, E), s)
# 1: // BFS returns the capacity of the augmenting path found (or 0 if there are none left)
# 2:      visited[1..n] = false
# 3:      visited[s] = true
# 4:      queue = Queue()
# 5:      queue.push(s)
# 6:      while queue is not empty do
# 7:          u = queue.pop()
# 8.          for each vertex v adjacent to u do
# 9:              if not visited[v] then
# 10:                 visited[v] = true
# 11:                 queue.push(v)


# --------------------------------------------------------------------------------------------------
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

# connect REGULAR target
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

# connect the nodes from respective maxOut node to maxIn node for connections
# connections
# connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000),
#                (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]

# adjListGraph(1)

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