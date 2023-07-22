"""
Algorithm 58 Bottom-up longest path in a DAG
1: function CRITICAL_PATH(G = (V,E ))
2:      longest[1..n] = 0
3:      order = reverse(TOPOLOGICAL_SORT(G ))
4:      for each vertex u in order do
5:          for each edge (u, v ) adjacent to u do
6:              longest[u] = max(longest[u], w(u, v ) + longest[v ])
7:      return longest[1..n]
"""

"""
Algorithm 59 Recursive longest path in a DAG
1: function CRITICAL_PATH(u)
2:      if longest[u] = null then // longest[1..n] contains memoised subproblems
3:          longest[u] = 0
4:          for each edge (u, v ) adjacent to u do
5:              longest[u] = max(longest[u], w(u, v ) + CRITICAL_PATH(v ))
6:      return longest[u]

"""

if __name__ == '__main__':
    pass