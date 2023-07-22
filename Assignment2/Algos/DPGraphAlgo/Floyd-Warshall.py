"""
Algorithm 56 Floyd-Warshall
1: function FLOYD_WARSHALL(G = (V, E))
2:      dist[1..n][1..n] = ∞
3:      dist[v ][v] = 0 for all vertices v
4:      dist[u][v] = w(u, v ) for all edges e = (u, v ) in E
5:      for each vertex k = 1 to n do
6:          for each vertex u = 1 to n do
7:              for each vertex v = 1 to n do
8:                  dist[u][v ] = min(dist[u][v ], dist[u][k] + dist[k][v ])
9:      return dist[1..n][1..n]

"""

"""

Algorithm 57 Warshall’s transitive closure algorithm
1: function TRANSITIVE_CLOSURE(G = (V, E))
2:      connected[1..n][1..n] = false // Store using a bitvector
3:      connected[v ][v ] = true for all vertices v
4:      connected[u][v ] = true for all edges e = (u, v ) in E
5:      for each vertex k = 1 to n do
6:          for each vertex u = 1 to n do
7:              for each vertex v = 1 to n do
8:                  connected[u][v ] = connected[u][v ] or (connected[u][k] and connected[k][v ])
9:      return connected[1..n][1..n
"""


if __name__ == '__main__':
    pass