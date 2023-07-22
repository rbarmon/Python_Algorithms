    """
            each data cenre has a in and out limit in otherwords capacity

        each data centre is given two nodes and edges with in capacity and out


        Your task is to determine the maximum possible data throughput from the data centre origin to the data centres specified in targets.
        You should implement a function maxThroughput(connections, maxIn, maxOut, origin, targets) that returns the maximum possible data throughput from the data centre origin to the data centres specified in targets.

        The problem has no lower bounds, no demands. What is required is to create each individual node and make sure that the specific in and out capacity are fulfilled.
        Just add nodes for each
        use maxIn and maxOut to create incoming and outgoing capacity
        create connections
        connect source and target and then run the ford fulkerson method

        Edmonds-Karp algorithm by using BFS instead of DFS.
        This allows the augmenting path to pick a path with minimum number of edges improving the time complexity compared to a
        DFS implementation.
"""

    """
    The problem has no lower bounds, no demands. What is required is to create each individual node and make sure that the specific in and out capacity are fulfilled. 
    Just add nodes for each
    use maxIn and maxOut to create incoming and outgoing capacity 
    create connections 
    connect source and target and then run the ford fulkerson method
    """