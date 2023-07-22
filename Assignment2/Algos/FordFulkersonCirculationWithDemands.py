# Week 8 & 9



"""
Algorithm 61 Ford-Fulkerson implemented using depth-first search
1: // DFS returns the capacity of the augmenting path found (or 0 if there are none left)
2: function DFS(u, t , bottleneck)
3:      if u = t then return bottleneck // We hit the sink, so we have an augmenting path
4:      visited[u] = true
5:      for each edge e = (u, v ) adjacent to u do
6:          residual = e .capacity - e .flow
7:          if residual > 0 and not visited[v] then
8:              augment = DFS(v , t , min(bottleneck, residual))
9:              if augment > 0 then // We found an augmenting path - add the flow
10:                 e .flow += augment
11:                 e .reverse.flow -= augment
12:                 return augment
13:     return 0 // We could not find an augmenting path
14:
15: function MAX_FLOW(G = (V,E ),s,t )
16:     flow = 0
17:     do
18:         visited[1..n] = false
19:         augment = DFS(s,t ,∞)
20:         flow += augment
21:     loop while augment > 0
22:     return flow

Algorithm 60 The Ford-Fulkerson method
1: function MAX_FLOW(G = (V,E ),s,t )
2:      Set initial flow f to 0 on all edges
3:      while there exists an augmenting path p in the residual network Gf do
4:          Augment the flow f along the augmenting path p as much as possible
5:      return f


"""


"""

Algorithm 62 The method to solve the circulation with demands problem
1: function CIRCULATION(G = (V,E ), {du })
2:      If Pu∈V,du >0du 6=Pu∈V,du <0 −du , return unfeasible.
3:      Create the supergraph G0from G .
4:      Solve the max-flow problem in G0 using Ford-Fulkerson to obtain f0ma x .
5:      If |f0ma x | 6=Pu∈V,du >0du , return unfeasible.
6:      Given f0ma x , delete all outgoing edges of s and all incoming edges of t to obtain f .
7:      return f

"""


if __name__ == '__main__':
    pass