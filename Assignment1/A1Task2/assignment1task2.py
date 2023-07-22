"""
2 Repurposing Underused Workspace (Dynamic Programming) (10 marks)
"""

class MatrixPathNode:
    """
        Class description: A class that represents a node for each section in the decision array. Helps track the
        minimum total occupancy probability for that node and the also keeps track of its predecessor node to help find
        the final optimal section locations. No functionalities besides storing and tracking in the nodes itself.
    """
    def __init__(self, probability_total, pred_node_index, pred_node):
        """
        Function description: Constructor for a MatrixPathNode.

        Input:
            probability_total: current minimum total occupancy probability for that section

            pred_node_index: the index (i,j) for the optimal predecessor node/ section.

            pred_node: reference to optimal predecessor node in the decision array
        """
        self.probability_total = probability_total
        self.pred_node_index = pred_node_index
        self.pred_node = pred_node

def select_sections(occupancy_probability):
    """
        Function description: This function returns a list of two items, an integer which is the total
        occupancy for the selected n sections to be removed, and a list of n tuples in the form of (i,j), in which each
        tuple represents one section selected for removal. The return values are selected through the use of Dynamic
        Programming.

    	Approach description: Considering the 3 selection conditions and the fact that each aisle has n rows where n > m,
    	we can find the n sections from top to down that has the total minimum occupancy rate using Dynamic Programming.
        The solution implements the Dynamic Programming Strategy in which each row is a sub-problem, and its solutions
        are used to build upon to find the final row's solution. Bottom-Up Dynamic programming is implemented using the
        memoization stored in the decision_array. Finding the optimal path slightly differs depending on the value of m
        which is explained below but to put it simply it slightly alters the method of solving when checking same and
        adjacent columns. Each section picks the available section with the minimum occupancy probability from the
        previous row and the decision array is built upon these optimal choices. Once we have found the optimal total
        minimum occupancy rate for each section (n*m) in the decision array, the decision array is used to find the
        minimum in the final row and that node is used to trace back along the path to find the optimal section
        locations.

    	Time Complexity Breakdown:

            Given n is the number of aisles/columns in the office and, m is the number of rows in the office

            Preprocessing to costruct the decision costs O(n) and setting up the first row of the decision array
            cost O(m)

            The Dynamic Programming deicison array constructing using the for loops costs O(nm) in the worst case for
            all 3 cases.

            Final Processing to get the output costs O(m) to ge the minimum Node for the last row and getting the
            sections_locations costs O(n).

            Total Complexity = O(n) + O(m) + O(nm) + O(m) + O(n) = O(nm)

        Space Complexity Breakdown:
            • given input occupancy_probability list of lists of O(nm) space.

            • decision_array for dynamic programming with O(nm) aux space.

            decision_array beats out other pre/final-processing space complexity so total is O(nm) space and O(nm) aux
            space.

    	Input: occupancy_probability: a list of lists, where each position in a row and a column represents the
    	occupancy probability of that location.

    	Output: A list of two items:
            • an integer value which is the total occupancy for the selected n section to be removed. In other words,
            the total occupancy of the n section with the minimum total occupancy.
            • a list of n tuples in which each tuple represents the section removed from each row.

    	Time complexity: O(nm) time, where n is the number of rows, and m is the number of columns/aisles.

    	Space complexity: O(nm) space, where n is the number of rows, and m is the number of columns/aisles.





    """

    #m represents the number of columns in the office
    m = len(occupancy_probability[0])

    # n represents the number of rows in the office
    n = len(occupancy_probability)

    """ Decision_array for dynamic programming with O(nm) space. It is a n*m list of lists initialized with None.
    It will be used to store the optimal path and minimum total occupancy for each column up until its respective row.
    """
    decision_array = [[None for x in range(m)] for y in range(n)]

    """To find the best occupancy probability for each column in the first row is unnecessary as it will be optimal as 
    is. Therefore, simply replace each value of the first row of the decision array with each value set as 
    MatrixPathNode(occupancy_probability[0][i], None, None). 
    
    To summarize: a MatrixPathNode mainly serves to track the minimum occupancy probability total which is the optimal 
    sections up until that section that is available to that section, and also to track the index (i,j) of the 
    predecessor node which is the predecessor section that was optimal for the current section.
    
    So the first row for decision array in each column will have:
     MatrixPathNode("initial first row value", None because no predecessor, None because no predecessor).
    """
    first_row = []
    for i in range(m):
        first_row.append(MatrixPathNode(occupancy_probability[0][i], None, None))
    decision_array[0] = first_row


    """
    There are three cases that change how the problem is solved:
    If m == 1:
        The office would be one column straight down thus there is no need for solving further and take the path 
        straight down and that would be the optimal and only sections to remove.
    Else if m == 2:
        When deciding optimal:
            The current row, first column, can pick the minimum occupancy probability from:
                previous row, first column
                previous row, second column
            The current row, m column, can pick the minimum occupancy probability from:
                previous row, "m-1" column
                previous row, "m" column
    Else when m >= 3:
        When deciding optimal:
            The current row, first column, can pick the minimum occupancy probability from:
                previous row, first column
                previous row, second column
            The current row second to m-1 column, can pick the minimum occupancy probability from:
                previous row, current column - 1 
                previous row, current column 
                previous row, current column + 1
            The current row, "m" column, can pick the minimum occupancy probability from:
                previous row, m-1 column
                previous row, m column
    """
    if m == 1: #Just take the straight path down.
        minimum_total_occupancy = 0
        sections_location = []
        for i in range(0, n):
            minimum_total_occupancy += occupancy_probability[i][0]
            sections_location.append((i,0))
        print([minimum_total_occupancy, sections_location])
        return [minimum_total_occupancy, sections_location]
    elif m == 2:
        for i in range(1, n):
            for j in range(0, m):
                if j == 0:
                    minimum_val = min(decision_array[i - 1][0].probability_total,
                                      decision_array[i - 1][1].probability_total)
                    if decision_array[i - 1][0].probability_total <= decision_array[i - 1][1].probability_total:
                        pred_node_index = (i - 1, 0)
                        pred_node = decision_array[i - 1][0]
                    else:
                        pred_node_index = (i - 1, 1)
                        pred_node = decision_array[i - 1][1]
                    decision_array[i][0] = MatrixPathNode(occupancy_probability[i][0] + minimum_val, pred_node_index,
                                                          pred_node)
                else: #if j == m - 1:
                    minimum_val = min(decision_array[i - 1][m - 2].probability_total,
                                      decision_array[i - 1][m - 1].probability_total)
                    if decision_array[i - 1][m - 2].probability_total <= decision_array[i - 1][m - 1].probability_total:
                        pred_node_index = (i - 1, m - 2)
                        pred_node = decision_array[i - 1][m - 2]
                    else:
                        pred_node_index = (i - 1, m - 1)
                        pred_node = decision_array[i - 1][m - 1]

                    decision_array[i][m - 1] = MatrixPathNode(occupancy_probability[i][m - 1] + minimum_val,
                                                              pred_node_index, pred_node)
                # print(decision_array)
    else:
        for i in range(1,n):
            for j in range(0,m):
                if j == 0:
                    minimum_val = min(decision_array[i-1][0].probability_total, decision_array[i-1][1].probability_total)
                    if decision_array[i-1][0].probability_total <= decision_array[i-1][1].probability_total:
                        pred_node_index = (i-1, 0)
                        pred_node = decision_array[i-1][0]
                    else:
                        pred_node_index = (i - 1, 1)
                        pred_node = decision_array[i-1][1]
                    decision_array[i][0] = MatrixPathNode(occupancy_probability[i][0] + minimum_val, pred_node_index, pred_node)
                elif j == m-1:
                    minimum_val = min(decision_array[i - 1][m-2].probability_total, decision_array[i - 1][m-1].probability_total)
                    if decision_array[i - 1][m-2].probability_total <= decision_array[i - 1][m-1].probability_total:
                        pred_node_index = (i-1, m-2)
                        pred_node = decision_array[i-1][m-2]
                    else:
                        pred_node_index = (i-1, m-1)
                        pred_node = decision_array[i-1][m-1]

                    decision_array[i][m-1] = MatrixPathNode(occupancy_probability[i][m-1] + minimum_val, pred_node_index, pred_node)
                else:
                    minimum_val = min(decision_array[i - 1][j-1].probability_total, decision_array[i - 1][j].probability_total, decision_array[i - 1][j+1].probability_total)
                    if decision_array[i - 1][j-1].probability_total < decision_array[i - 1][j].probability_total and  decision_array[i - 1][j-1].probability_total < decision_array[i - 1][j+1].probability_total:
                        pred_node_index = (i-1, j-1)
                        pred_node = decision_array[i-1][j-1]
                    elif decision_array[i - 1][j].probability_total < decision_array[i - 1][j+1].probability_total:
                        pred_node_index = (i-1, j)
                        pred_node = decision_array[i-1][j]
                    else:
                        pred_node_index = (i - 1, j+1)
                        pred_node = decision_array[i-1][j+1]
                    decision_array[i][j] = MatrixPathNode(occupancy_probability[i][j] + minimum_val, pred_node_index, pred_node)
                # print(decision_array)

    """
    Find node with minimum total occupancy in the final row. Must check every element in the final row.
    """
    min_node = decision_array[n-1][0]
    min_pos = (n-1,0)
    for j in range(1,m):
        if min_node.probability_total > decision_array[n-1][j].probability_total:
            min_node = decision_array[n-1][j]
            min_pos = (n-1, j)

    """
    Get the list of of section locations using deque to popleft as we track backwards. 
    In the while loop below once the path_search_node becomes None that means there are no more predecessors and 
    the optimal section_locations has been found.
    """
    # path = deque()
    # path.appendleft(min_pos)
    # path.appendleft(min_node.pred_node_index)

    sections_location = []
    sections_location.append(min_pos)
    sections_location.append(min_node.pred_node_index)

    # print(path)

    path_search_node = min_node.pred_node
    # print(path_search_node.pred_node_index)

    while path_search_node: #while not None
        if path_search_node.pred_node_index:
            # path.appendleft(path_search_node.pred_node_index)
            sections_location.append(path_search_node.pred_node_index)
        path_search_node = path_search_node.pred_node

    sections_location.reverse()

    """Reformat information into a list.
    """
    # sections_location = []
    # for item in path:
    #     sections_location.append(item)

    minimum_total_occupancy = min_node.probability_total

    print([minimum_total_occupancy, sections_location])

    return [minimum_total_occupancy, sections_location]


if __name__ == "__main__":
    # Example OK
    # occupancy_probability = [[31, 54, 94, 34, 12],[26, 25, 24, 16, 87],[39, 74, 50, 13, 82],[42, 20, 81, 21, 52],[30, 43, 19,  5, 47],[37, 59, 70, 28, 15],[ 2, 16, 14, 57, 49],[22, 38,  9, 19, 99]]
    # [118, [(0, 4), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 2), (7, 2)]]

    # Two optimal solutions OK m>=3
    # occupancy_probability = [[32, 86, 95, 15,  68, 90],[91, 88, 96, 51, 64, 66], [17, 70, 13, 9, 90, 17], [17, 15, 38, 12, 53, 17],[29, 6, 18, 27, 66, 48],[74, 43, 76, 44, 3, 1],[89, 1, 8, 24, 45, 62],[3, 98, 99, 89, 6, 66]]
    # expected_1 = [147, [(0, 3), (1, 3), (2, 2), (3, 1), (4, 1), (5, 1), (6, 1), (7, 0)]]
    # expected_2 = [147, [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 4), (6, 3), (7, 4)]]

    # Gives me Errors. OK NOW  m = 1
    # n > m, n = 2, m = 1
    # occupancy_probability = [[66], [66]]
    # expected = [132, [(0, 0), (1, 0)]]

    # Should give me Error OK I GUESS m = 2
    # n > m, n = 3, m = 2
    # occupancy_probability = [[68, 90], [70, 13], [17, 15]]
    # expected = [96, [(0, 0), (1, 1), (2,1)]]

    # Gives me Errors OK NOW
    # m = 1
    # occupancy_probability = [[15], [84], [82], [79], [77], [55], [69], [13], [21], [33], [85], [100], [67], [93], [3],  [26], [29], [89], [36], [100], [68], [34], [87], [55], [47], [44], [64], [84], [41], [97]]
    # expected = [1777, [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0),(12, 0), (13, 0), (14, 0), (15, 0), (16, 0), (17, 0), (18, 0), (19, 0), (20, 0), (21, 0),(22, 0), (23, 0), (24, 0), (25, 0), (26, 0), (27, 0), (28, 0), (29, 0)]]

    # OK
    occupancy_probability = [[57, 11, 14, 19, 63, 50, 61, 50, 40, 0, 46],
                             [2, 42, 98, 84, 56, 5, 33, 87, 60, 19, 91],
                             [84, 23, 37, 36, 38, 89, 72, 13, 48, 88, 46],
                             [36, 91, 11, 1, 5, 3, 38, 58, 37, 24, 39],
                             [52, 74, 67, 41, 76, 29, 38, 61, 74, 42, 10],
                             [46, 25, 38, 16, 50, 7, 99, 34, 79, 83, 19],
                             [76, 68, 74, 48, 38, 11, 46, 25, 31, 10, 73],
                             [99, 4, 65, 22, 12, 47, 18, 45, 63, 85, 17],
                             [35, 86, 91, 69, 50, 20, 72, 34, 24, 69, 100],
                             [20, 7, 63, 92, 33, 81, 22, 79, 85, 39, 21],
                             [98, 22, 37, 54, 28, 89, 50, 95, 59, 17, 88],
                             [13, 86, 98, 26, 30, 3, 93, 97, 59, 1, 23],
                             [39, 62, 48, 37, 35, 84, 87, 91, 63, 66, 21]]

    # expected = [273, [(0, 1), (1, 0), (2, 1), (3, 2), (4, 3), (5, 3), (6, 4), (7, 4), (8, 5), (9, 4), (10, 4), (11, 5),(12, 4)]]

    # OK
    occupancy_probability = [
                        [57, 76, 38, 22],
                        [56, 94, 54, 68],
                        [71, 86, 86, 99],
                        [81,  0,  0, 60],
                        [36, 22, 43, 93]
                        ]
    # expec_res_1 = [184, [(0, 3), (1, 2), (2, 1), (3, 1), (4, 1)]]
    # expec_res_2 = [184, [(0, 3), (1, 2), (2, 2), (3, 2), (4, 1)]]

    # OK
    # occupancy_probability = [
    #     [19, 76, 38, 22],
    #     [56, 20, 54, 68],
    #     [71, 86, 15, 99],
    #     [81, 82, 82, 22],
    #     [36, 22, 22, 93]
    # ]
    # expected = [98, [(0, 0), (1, 1), (2, 2), (3, 3), (4, 2)]]
    # expected = [98, [(0, 0), (1, 1), (2, 2), (3, 3), (4, 1)]]

    # OK
    # occupancy_probability = [
    #     [19, 76, 38, 22, 0],
    #     [56, 20, 54, 0, 34],
    #     [71, 86, 0, 99, 89],
    #     [81, 0, 82, 22, 45],
    #     [0, 22, 22, 93, 23]
    # ]
    # expected = [0, [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]]

    # OK
    # occupancy_probability = [
    #     [19, 76, 38, 22, 0],
    #     [56, 20, 54, 0, 34],
    #     [71, 86, 0, 99, 89],
    #     [81, 34, 82, 0, 45],
    #     [62, 22, 22, 93, 0]
    # ]
    # expected = [0, [(0, 4), (1, 3), (2, 2), (3, 3), (4, 4)]]

    # occupancy_probability = [
    #     [0, 76, 38, 2],
    #     [1, 94, 54, 1],
    #     [2, 86, 86, 99],
    #     [3, 0, 0, 0],
    #     [99, 99, 99, 0]
    # ]
    # expec_res_1 = [87, [(0, 0), (1, 0), (2, 1), (3, 2), (4, 3)]]

    select_sections(occupancy_probability)