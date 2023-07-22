"""
DUMP
    #Q.push(s, key=0)
    #list(range(0, 5))

    #Q is now Q = [0,inf,inf, inf, .., inf]
    #Q should be Q = [0]

     I dont need to do this
    for i in list(range(0, graph.NoOfVertices)):
        if i == start:
            continue
        else:
            Queue.push(i, float('inf'))

    #set up queue

"""


"""
function DIJKSTRA(G=(V,E),s) 
    dist[1..n] = ∞
    pred[1..n] = 0
    dist[s]=0
    Q = priority_queue() 
    Q.push(s , key = 0) 
    while Q is not empty do
        u, key = Q.pop_min() 
        if dist[u] = key then
            for each edge e that is adjacent to u do 
                if dist[v] > dist[u] + w(u,v) then 
                    dist[v] = dist[u] + w(u,v)
                    pred[v ] = u
                    Q.push(v , key = dist[v ])
    return dist[1..n], pred[1..n]

"""

"""
Adjacency list of vertex 0
 head -> Vertex No: 7.single(5).double(5) -> Vertex No: 9.single(1).double(1) 

Adjacency list of vertex 1
 head -> Vertex No: 8.single(2).double(1) -> Vertex No: 9.single(6).double(5) 

Adjacency list of vertex 2
 head -> Vertex No: 1.single(2).double(2) -> Vertex No: 3.single(5).double(5) -> Vertex No: 4.single(6).double(2) -> Vertex No: 9.single(6).double(4) 

Adjacency list of vertex 3
 head -> Vertex No: 5.single(1).double(1) 

Adjacency list of vertex 4
 head 

Adjacency list of vertex 5
 head -> Vertex No: 3.single(6).double(6) 

Adjacency list of vertex 6
 head -> Vertex No: 9.single(6).double(5) -> Vertex No: 4.single(5).double(4) 

Adjacency list of vertex 7
 head -> Vertex No: 3.single(8).double(7) -> Vertex No: 4.single(3).double(1) 

Adjacency list of vertex 8
 head -> Vertex No: 7.single(6).double(1) 

Adjacency list of vertex 9
 head -> Vertex No: 0.single(7).double(4) 

"""

# 0 -> Vertex No: 1 .single(10).double(10) -> Vertex No: 3 .single(5).double(3)
# 1 -> Vertex No: 4 .single(30).double(20)
# 2 -> Vertex No: 0 .single(2).double(2) -> Vertex No: 4 .single(30).do uble(25)
# 3 -> Vertex No: 2 .single(2).double(2) -> Vertex No: 4 .single(35).double(15)
# 4 -> Vertex No: 0 .single(15).double(10)

# start = 0
# end = 4
# passengers = [2, 1]
# dist = [0, inf, inf, inf, inf]
# pred = [None, None, None, None, None]
# Q should be Q = [0]
# return val = [0, 3, 2, 0, 3, 4]

"""
def generateGraph(roads):

    #start = 0
    #end = 4

    # The locations where there are potential passengers
    #passengers = [2, 1]

    # The roads represented as a list of tuple
    #roads = [(0, 3, 5, 3), (3, 4, 35, 15), (3, 2, 2, 2), (4, 0, 15, 10), (2, 4, 30, 25), (2, 0, 2, 2), (0, 1, 10, 10), (1, 4, 30, 20)]
    # Your function should return the optimal route (which takes 27 minutes).

    #optimalRoute(start, end, passengers, roads)
    # [0, 3, 2, 0, 3, 4]

    #for i in range(len(roads)):
        #get max using merge sort


    carpoolgraph = CarpoolGraph(5) #change later

    for i in range(len(roads)):
        #add edges
        carpoolgraph.add_directed_edge(roads[i][0],roads[i][1],roads[i][2],roads[i][3])

    return carpoolgraph

"""

# carpoolgraph = adjacency list with single double weight
# 0 -> 1 -> 3
# 1 -> 4
# 2 -> 0 -> 4
# 3 -> 2 -> 4
# 4 -> 0
# start = 0
# end = 4
# passengers = [2, 1]

# carpoolgraph = adjacency list with single double weight
# This means 0 can go to 1 and 3
# 0 -> Vertex No: 1 .single(10).double(10) -> Vertex No: 3 .single(5).double(3)
# 1 -> Vertex No: 4 .single(30).double(20)
# 2 -> Vertex No: 0 .single(2).double(2) -> Vertex No: 4 .single(30).double(25)
# 3 -> Vertex No: 2 .single(2).double(2) -> Vertex No: 4 .single(35).double(15)
# 4 -> Vertex No: 0 .single(15).double(10)
# start = 0
# end = 4
# passengers = [2, 1]


# return val = [0, 3, 2, 0, 3, 4]

# add_directed_edge(start, end, single, double)
# roads = [(0, 3, 5, 3),
# (3, 4, 35, 15),
# (3, 2, 2, 2),
# (4, 0, 15, 10),
# (2, 4, 30, 25),
# (2, 0, 2, 2),
# (0, 1, 10, 10),
# (1, 4, 30, 20)]

# carpoolgraph = adjacency list with single double weight
# This means 0 can go to 1 and 3
# 0 -> Vertex No: 1 .single(10).double(10) -> Vertex No: 3 .single(5).double(3)
# 1 -> Vertex No: 4 .single(30).double(20)
# 2 -> Vertex No: 0 .single(2).double(2) -> Vertex No: 4 .single(30).do uble(25)
# 3 -> Vertex No: 2 .single(2).double(2) -> Vertex No: 4 .single(35).double(15)
# 4 -> Vertex No: 0 .single(15).double(10)
# start = 0
# end = 4
# passengers = [2, 1]
# return val = [0, 3, 2, 0, 3, 4]

# pred = list(range(0, graph.NoOfVertices)) why did i do this? [0, 1, 2, 3, 4]

"""
    	function DIJKSTRA(G=(V,E),s)
        dist[1..n] = ∞
        pred[1..n] = 0
        dist[s]=0
        Q = priority_queue()
        Q.push(s , key = 0)
        while Q is not empty do
            u, key = Q.pop_min()
            if dist[u] = key then
                for each edge e that is adjacent to u do
                    if dist[v] > dist[u] + w(u,v) then
                        dist[v] = dist[u] + w(u,v)
                        pred[v ] = u
                        Q.push(v , key = dist[v ])
        return dist[1..n], pred[1..n]
"""