# while Queue.array[1:]:  # slice for now
#     # while Q is not empty do
#     u = Queue.pop_min()
#     completed.append(u.index)
#     print("Completed: {}".format(completed))
#     # dist = [0, 10, 7, 5, 37]
#     # pred = [None, 0, 3, 0, 2]


    # if passenger_condition == False and u.index in passengers:
    #     passenger_condition = True
    #     print("passenger_condition is True")
    #     loop_start_index = u.index
    #     new_dist = dist[:]  # [:] prevents it from being a reference to dist
    #     new_pred = pred[:]
    #     new_completed = []
    #     # for i in completed[:len(completed)-1]:
    #     #     dist[i] = float('inf')
    #     # for i in completed[:len(completed)]:
    #     for i in completed:
    #         new_dist[i] = float('inf')
    #     # dist = [0, 10, 7, 5, 40]
    #     # new_dist = [inf, 10, inf, inf, 40]
    #     # pred = [None, 0, 3, 0, 2]
    #     print("Pred list: {}".format(pred))
    #     print("New Pred list: {}".format(new_pred))
    #     print("Dist list: {}".format(dist))
    #     print("New Dist list: {}".format(new_dist))
    #     # Queue.printPQ()
    #     # if u.index == loop_start_index: to skip if dist[u.index] == u.key:


        while Queue.array[1::]:
            print("----------------------------------------------------------------------------------")
            print("Dist list: {}".format(dist))
            print("New Dist list: {}".format(new_dist))
            Queue.printPQ()

            if u.index is loop_start_index:
                # if dist[u] = key then
                temp = graph.adjgraph[u.index]
                while temp:  # halts on None for adj node
                    # for each edge e that is adjacent to u do
                    if new_dist[temp.vertexNo] > dist[
                        u.index] + temp.double:  # think about the case for when it turns to double
                        # if dist[v] > dist[u] + w(u, v) then
                        new_dist[temp.vertexNo] = dist[u.index] + temp.double
                        # dist[v] = dist[u] + w(u, v)
                        new_pred[temp.vertexNo] = u.index
                        # pred[v] = u
                        Queue.push(MinHeapNode(temp.vertexNo, new_dist[temp.vertexNo], u.is_passenger_node))
                        # temp = temp.next
                        # Queue.printPQ()
                        # Q.push(v, key=dist[v])
                    # elif dist[temp.vertexNo] is float('inf'):
                    #     new_dist[temp.vertexNo] = dist[u.index] + temp.double
                    #     # dist[v] = dist[u] + w(u, v)
                    #     new_pred[temp.vertexNo] = u.index
                    #     # pred[v] = u
                    #     Queue.push(MinHeapNode(temp.vertexNo, new_dist[temp.vertexNo], u.is_passenger_node))
                    #     # temp = temp.next
                    #     # Queue.printPQ()
                    temp = temp.next
                    Queue.printPQ()
                print("Pred list: {}".format(pred))
                print("New Pred list: {}".format(new_pred))
                print("Dist list: {}".format(dist))
                print("New Dist list: {}".format(new_dist))
                print("hey")

                print("----------------------------------------------------------------------------------")
            # elif not u.is_passenger_node and dist[u.index] == u.key:
            #     # if dist[u] = key then
            #     temp = graph.adjgraph[u.index]
            #     while temp:  # halts on None for adj node
            #         # for each edge e that is adjacent to u do
            #         if dist[temp.vertexNo] > dist[
            #             u.index] + temp.single:  # think about the case for when it turns to double
            #             # if dist[v] > dist[u] + w(u, v) then
            #             dist[temp.vertexNo] = dist[u.index] + temp.single
            #             # dist[v] = dist[u] + w(u, v)
            #             pred[temp.vertexNo] = u.index
            #             # pred[v] = u
            #             Queue.push(MinHeapNode(temp.vertexNo, dist[temp.vertexNo], u.is_passenger_node))
            #             # temp = temp.next
            #             # Queue.printPQ()
            #             # Q.push(v, key=dist[v])
            #         temp = temp.next
            #         Queue.printPQ()
            #     print("Dist list: {}".format(dist))
            #     print("Pred list: {}".format(pred))
                print("----------------------------------------------------------------------------------")
            # if dist[u.index] == new_dist[u.index]:
            # to solve the 1 10 problem
            #   dist[u.index] != new_dist[u.index] and
            # elif new_dist[u.index] == u.key:  # 7 == 7
            #     # if dist[u] = key then
            #     temp = graph.adjgraph[u.index]
            #     while temp:  # halts on None for adj node
            #         # for each edge e that is adjacent to u do
            #         if new_dist[temp.vertexNo] > new_dist[
            #             u.index] + temp.double:  # think about the case for when it turns to double
            #             # if dist[v] > dist[u] + w(u, v) then
            #             new_dist[temp.vertexNo] = new_dist[u.index] + temp.double
            #             # dist[v] = dist[u] + w(u, v)
            #             new_pred[temp.vertexNo] = u.index
            #             # pred[v] = u
            #             Queue.push(MinHeapNode(temp.vertexNo, new_dist[temp.vertexNo], temp.vertexNo in passengers))
            #             # temp = temp.next
            #             # Queue.printPQ()
            #             # Q.push(v, key=dist[v])
            #         temp = temp.next
            #     Queue.printPQ()
            #     print("Dist list: {}".format(dist))
            #     print("Pred list: {}".format(pred))
            #     print("New Pred list: {}".format(new_pred))
            #     print("New Dist list: {}".format(new_dist))
            #     print("----------------------------------------------------------------------------------")
            # u = Queue.pop_min()
            # completed.append(u.index)
            # print("Completed: {}".format(completed))

            if u.index == loop_start_index:
                # break #something along the lines
                path = deque()
                index = end
                while index != loop_start_index:
                    path.appendleft(index)
                    index = new_pred[index]
                if index == loop_start_index:
                    while index is not start:
                        path.appendleft(index)
                        index = pred[index]
                print(index)
                if index is start:
                    path.appendleft(start)

                final_path = []
                for item in path:
                    final_path.append(item)

                print("New Dist list: {}".format(new_dist))
                print("Pred list: {}".format(pred))
                print("New Pred list: {}".format(new_pred))
                Queue.printPQ()
                print(path)
                print(final_path)

                return final_path
        # u, key = Q.pop_min()
        print("hello")
        print("Pred list: {}".format(pred))
        print("New Pred list: {}".format(new_pred))
        print("Dist list: {}".format(dist))
        print("New Dist list: {}".format(new_dist))
        print("Loop Start Index: {}".format(loop_start_index))
        Queue.printPQ()
        index = end
        path = deque()
        path.appendleft(end)

        # if dist[end] is float('inf') or dist[end] > new_dist[end]:
        #     while index is not loop_start_index or new_pred[index] is not None:
        #         path.appendleft(new_pred[index])
        #         index = new_pred[index]
        #     if index == loop_start_index:
        #         while index is not start:
        #             path.appendleft(pred[index])
        #             index = pred[index]
        #     final_path = []
        #     for item in path:
        #         final_path.append(item)
        #     print(path)
        #     print(final_path)
        #     return final_path

    # print(dist[u.index])
    # print(u.key)



