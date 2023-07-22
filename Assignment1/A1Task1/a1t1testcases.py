"""
BASE CASE NO PASSENGERS
"""
# OK
# # Example 8 NO PASSENGER
# start = 4
# end = 0
# passengers = []
# roads = [
#     (0, 1, 28, 22),
#     (3, 2, 21, 10),
#     (4, 1, 26, 20),
#     (1, 3, 5, 3),
#     (0, 4, 24, 13),
#     (2, 1, 26, 15),
#     (2, 0, 26, 26)
# ]
# result = [4, 1, 3, 2, 0]  # Optimal route is 78 mins
# optimalRoute(start, end, passengers, roads)

# OK
# Example 9 NO PASSENGER
# start = 1
# end = 2
# passengers = []
# roads = [
#     (3, 4, 24, 10),
#     (4, 1, 16, 6),
#     (0, 2, 28, 14),
#     (1, 3, 27, 12),
#     (4, 0, 5, 4),
#     (2, 4, 15, 9)
# ]
# result = [1, 3, 4, 0, 2]  # Optimal route is 84 mins
# optimalRoute(start, end, passengers, roads)

# OK
# THIS WAS A PROBLEM WHEN I WAS LAZY AND USING COMPLETED AS FINAL
# Example 9.5 NO PASSENGER
# start = 1
# end = 2
# passengers = []
# roads = [
#     (3, 4, 24, 10),
#     (4, 1, 16, 6),
#     (0, 2, 28, 14),
#     (1, 3, 27, 12),
#     (4, 0, 5, 4),
#     (2, 4, 15, 9),
#     (1, 5, 15, 9)
# ]
# result = [1, 3, 4, 0, 2]  # Optimal route is 84 mins
# optimalRoute(start, end, passengers, roads)

"""
NON REPEATER
"""
# OK
# Example 13
# start = 0
# end = 3
# passengers = [2, 1]
# roads = [(0, 1, 10, 10), (1, 3, 100, 1), (0, 2, 2, 2), (2, 3, 60, 60)]
# result = [0, 1, 3] # Optimal route is 11 minutes
# optimalRoute(start, end, passengers, roads)

# OK
# # Example 14
start = 0
end = 3
passengers = [2, 1]
roads = [(0, 1, 10, 10), (1, 3, 100, 1), (0, 2, 2, 2), (2, 3, 60, 60), (2, 1, 6, 3)]
result = [0, 2, 1, 3] # Optimal route is 6 minutes
# optimalRoute(start, end, passengers, roads)

# OK
# # Example 16
# start = 0
# end = 4
# passengers = [1, 3]
# roads = [
#     (0, 1, 6, 5),
#     (0, 2, 5, 1),
#     (0, 4, 20, 18),
#     (1, 4, 4, 4),
#     (2, 3, 2, 2),
#     (3, 4, 20, 2)
# ]
# expected = [0, 2, 3, 4]

# OK Passcon but faster without passenger
# # Example 15
# start = 2
# end = 6
# passengers = [0, 3, 5]
# roads = [
#     (0, 1, 10, 8),
#     (2, 6, 5, 5),
#     (1, 2, 11, 9),
#     (2, 3, 12, 10),
#     (3, 4, 15, 12),
#     (4, 5, 18, 10),
#     (5, 6, 20, 13),
#     (6, 7, 30, 15)
# ]
# expected = [2, 6]

# OK
# # Example 3 Non_Pass FAIL 4 has no edges out?
# Check Edges
start = 6
end = 7
passengers = [4, 2, 9]
roads = [
    (9, 0, 7, 4),
    (7, 4, 3, 1),
    (8, 7, 6, 1),
    (3, 5, 1, 1),
    (2, 9, 6, 4),
    (6, 4, 5, 4),
    (2, 4, 6, 2),
    (7, 3, 8, 7),
    (0, 9, 1, 1),
    (2, 3, 5, 5),
    (5, 3, 6, 6),
    (1, 9, 6, 5),
    (0, 7, 5, 5),
    (1, 8, 2, 1),
    (6, 9, 6, 5),
    (2, 1, 2, 2)
]
# result = [6, 9, 0, 7]  # optimal route should take 15 mins
# optimalRoute(start, end, passengers, roads)

# # OK Works, but I believe I haven't solved all problems
# # Example 11
start = 0
end = 5
passengers = [3, 4, 2]
roads = [
    (0, 1, 100, 95),
    (0, 2, 2, 2),
    (0, 3, 1, 1),
    (0, 4, 3, 3),
    (1, 5, 5, 3),
    (2, 5, 1000, 955),
    (3, 5, 1000, 955),
    (4, 5, 1000, 955),
]
# result = [0, 1, 5]  # Optimal route is 105 mins
# optimalRoute(start, end, passengers, roads)

# # OK Works, but I believe I haven't solved all problems
# Example 12
start = 0
end = 3
passengers = [2]
roads = [(0, 1, 10, 10), (1, 3, 1, 1), (0, 2, 2, 2)]
result = [0, 1, 3]  # Optimal route is 11 minutes
# optimalRoute(start, end, passengers, roads)

# OK
# # Example 4 PassCon FAIL
# PasscCon No Repeat
start = 0
end = 5
passengers = [2, 1]
roads = [
    (4, 5, 200, 2),
    (0, 2, 2, 2),
    (1, 3, 10, 5),
    (3, 5, 50, 50),
    (2, 4, 10, 10),
    (0, 1, 1, 1)
]
result = [0, 2, 4, 5]
# optimalRoute(start, end, passengers, roads)

# OK I thnk because it goes to the regular no passenger return
# # Example 7 LONG ONE
# # What is the significance of not having repeats? Number of nodes or because of the early access to 26? Or both?
start = 54
end = 62
passengers = [29, 63, 22, 18, 2, 23, 48, 41, 15, 31, 13, 4, 24, 16, 27, 17, 50, 67, 37, 58, 28, 64, 35, 10, 68, 38,
              59, 26, 69, 43, 44, 30, 46, 7]
roads = [
    (31, 45, 23, 12), (48, 3, 14, 7), (58, 50, 25, 10),
    (5, 3, 26, 23), (12, 32, 29, 3), (65, 4, 16, 16),
    (13, 46, 14, 13), (63, 29, 10, 2), (19, 56, 30, 19),
    (52, 47, 19, 12), (47, 52, 12, 8), (30, 42, 22, 19),
    (46, 60, 17, 17), (54, 22, 8, 7), (19, 8, 23, 10),
    (33, 51, 22, 5), (12, 17, 20, 5), (64, 62, 22, 18),
    (66, 25, 28, 10), (48, 19, 23, 8), (36, 13, 22, 19),
    (26, 48, 6, 3), (31, 30, 26, 9), (24, 29, 22, 11),
    (23, 36, 27, 11), (59, 37, 16, 10), (60, 44, 12, 8),
    (40, 7, 18, 1), (22, 3, 13, 12), (36, 35, 15, 15),
    (43, 2, 23, 6), (29, 27, 27, 6), (34, 0, 17, 4),
    (52, 50, 13, 4), (27, 23, 15, 1), (15, 10, 7, 6),
    (36, 65, 23, 1), (41, 64, 27, 8), (45, 34, 12, 1),
    (51, 24, 12, 10), (16, 12, 29, 7), (9, 67, 25, 24),
    (49, 38, 16, 4), (38, 7, 10, 1), (50, 13, 23, 16),
    (5, 33, 27, 10), (23, 42, 29, 15), (9, 2, 13, 7),
    (59, 52, 23, 17), (59, 54, 8, 6), (1, 8, 10, 8),
    (33, 30, 15, 2), (6, 26, 18, 6), (39, 57, 13, 12),
    (54, 26, 13, 9), (57, 41, 4, 4), (37, 66, 16, 12),
    (36, 9, 12, 5), (2, 68, 7, 3), (69, 28, 18, 2),
    (44, 1, 14, 3), (48, 9, 6, 4), (17, 38, 13, 1),
    (61, 49, 4, 4), (9, 10, 6, 3), (46, 37, 21, 8),
    (23, 53, 21, 8), (7, 24, 28, 26), (62, 20, 22, 7),
    (1, 18, 10, 1), (7, 41, 9, 1), (13, 18, 6, 4),
    (25, 21, 21, 3), (1, 61, 21, 16), (49, 40, 13, 5),
    (19, 25, 11, 10), (62, 50, 5, 5), (33, 46, 10, 9),
    (28, 25, 14, 6), (56, 51, 6, 4), (18, 19, 15, 1),
    (30, 9, 23, 13), (60, 21, 23, 7), (52, 37, 16, 6),
    (50, 42, 11, 4)
]

# Pred list: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#        None, None, None, None, 54, None, None, None, 54, None, None, None, None, None, None, None, None, None, None,
#        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
#        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
# New Pred list: [None, 44, 9, 22, 65, None, None, 38, 19, 48, 9, None, None, 36, None, None, None, None, 13, 48, 62, 25, 54,
#        27, 51, 19, 54, 29, None, 24, None, None, None, None, None, 36, 23, 46, 49, None, 49, 7, 23, None, 60, None,
#        13, None, 26, 61, 62, 56, None, 23, None, None, 19, None, None, None, 46, 1, 64, None, 41, 36, 37, 9, 2,
#        None]
# # Optimal route is 198 mins
# result = [54, 26, 48, 19, 56, 51, 24, 29, 27, 23, 36, 13, 46, 60, 44, 1, 61, 49, 38, 7, 41, 64, 62]
# optimalRoute(start, end, passengers, roads)

# OK
# NON-REPEATER/ REPEATER
# # Example 2 PassCon FAIL
# What is the significance of 2,0,7 repeat?
start = 2
end = 5
passengers = [3]
roads = [
    (6, 2, 22, 6),
    (3, 6, 4, 3),
    (0, 7, 8, 3),
    (5, 0, 9, 6),
    (5, 4, 6, 5),
    (4, 3, 24, 2),
    (1, 2, 26, 23),
    (7, 4, 26, 8),
    (7, 3, 12, 5),
    (4, 5, 10, 3),
    (2, 0, 14, 1),
    (5, 7, 6, 6)
]
# res_1 = [2, 0, 7, 3, 6, 2, 0, 7, 4, 5]  # Both results should yield 58 mins
# res_2 = [2, 0, 7, 4, 5]
# optimalRoute(start, end, passengers, roads)

"""
PASSCON REPEAT
"""



# OK
# REPEATER
# # Example 5
# # PassCon repeat of 0
start = 0
end = 4
passengers = [2, 1]
roads = [
    (0, 4, 30, 5),
    (0, 1, 5, 4),
    (1, 3, 3, 2),
    (3, 2, 2, 1),
    (2, 0, 1, 1)]
result = [0, 1, 3, 2, 0, 4]
# optimalRoute(start, end, passengers, roads)

# elif start in new_completed:
#     while index != start:
#         path.appendleft(index)
#         index = new_pred[index]
#     if index == start:
#         while index is not start:
#             path.appendleft(index)
#             index = pred[index]
#     print(index)
#     if index is start:
#         path.appendleft(start)

# OK FINAL SORTING WITH START OR LOOP STARTER
# # Example 17
start = 0
end = 3
passengers = [1]
roads = [
    (0, 1, 1, 1),
    (0, 2, 2, 1),
    (1, 2, 1, 1),
    (2, 0, 2, 1),
    (0, 3, 1000, 500)
]
# result = [0, 1, 2, 0, 3]


# OK
# # Example 1 OK Lol
# # What is the significance of 0,3 repeat?
# start = 0
# end = 4
# # The locations where there are potential passengers
# passengers = [2, 1]
# # The roads represented as a list of tuple
# roads = [(0, 3, 5, 3),
#          (3, 4, 35, 15),
#          (3, 2, 2, 2),
#          (4, 0, 15, 10),
#          (2, 4, 30, 25),
#          (2, 0, 2, 2),
#          (0, 1, 10, 10),
#          (1, 4, 30, 20)]
# #If you switch 0->3 and 0->1
# # Goes from 0 -> 1 -> 3
# # To 0 -> 3 -> 1
# #roads = [(0, 1, 10, 10), (0, 3, 5, 3), (3, 4, 35, 15), (3, 2, 2, 2), (4, 0, 15, 10), (2, 4, 30, 25), (2, 0, 2, 2), (1, 4, 30, 20)]
# # Your function should return the optimal route (which takes 27 minutes).
# optimalRoute(start, end, passengers, roads)
# #[0, 3, 2, 0, 3, 4]

# OK
# REPEATER
# # Example 6
# Sample IO given in the spec sheet
start = 0
end = 4
passengers = [2, 1]
roads = [
    (0, 3, 5, 3),
    (3, 4, 35, 15),
    (3, 2, 2, 2),
    (4, 0, 15, 10),
    (2, 4, 30, 25),
    (2, 0, 2, 2),
    (0, 1, 10, 10),
    (1, 4, 30, 20)]
# expected = [0, 3, 2, 0, 3, 4]
# optimalRoute(start, end, passengers, roads)

# OK
# REPEATER
# # Example 10
start = 4
end = 9
passengers = [2, 6, 0]
roads = [
    (4, 6, 30, 18),
    (3, 1, 8, 1),
    (9, 1, 9, 5),
    (1, 9, 30, 2),
    (8, 5, 12, 12),
    (8, 9, 8, 6),
    (1, 8, 25, 2),
    (2, 4, 4, 2),
    (6, 0, 25, 5),
    (4, 3, 6, 6),
    (1, 2, 15, 7)
]
result = [4, 3, 1, 2, 4, 3, 1, 9]
# optimalRoute(start, end, passengers, roads)

# Pred list: [None, 3, 1, 4, None, 8, 4, None, 1, 1]
# New Pred list: [6, 3, 1, 4, 2, None, 4, None, 1, 1]

"""
# start = 2
# end = 5
Pred list: [2, None, None, 7, 7, 4, None, 0]
New Pred list: [2, None, 6, 7, 7, None, 3, 0]
Dist list: [14, inf, 0, 34, 48, 58, inf, 22]
New Dist list: [44, inf, 43, 34, 48, inf, 37, 47]
# res_2 = [2, 0, 7, 4, 5]

start = 0
end = 3
Pred list: [None, 0, 0, 0]
New Pred list: [2, 0, 1, 0]
Dist list: [0, 1, 2, 1000]
New Dist list: [3, 1, 2, 503]
# result = [0, 1, 2, 0, 3]

Pred list: [None, 0, 3, 0, 3]
New Pred list: [2, 0, 3, 0, 3]

    start = 0
    end = 4
    passengers = [2, 1]
    roads = [
        (0, 3, 5, 3),
        (3, 4, 35, 15),
        (3, 2, 2, 2),
        (4, 0, 15, 10),
        (2, 4, 30, 25),
        (2, 0, 2, 2),
        (0, 1, 10, 10),
        (1, 4, 30, 20),
    ]
    # expected = [0, 3, 2, 0, 3, 4]

"""

if dist[end] is float('inf') or dist[end] > new_dist[end]:
    while index != start and new_pred[index] is not None:
        # while index is not loop_start_index or new_pred[index] is not None:
        path.appendleft(new_pred[index])
        index = new_pred[index]
    # the code below is retarded
    if index == start and new_pred[index] is not None:
        path.appendleft(new_pred[index])
        index = new_pred[index]
        while index is not start or index is not None:
            path.appendleft(new_pred[index])
            index = new_pred[index]


"""
            while index is not start or new_pred[index] is not None:

            # while index is not loop_start_index or new_pred[index] is not None:
                path.appendleft(new_pred[index])
                index = new_pred[index]

            #the code below is retarded
            if index == start:
                while index is not start:
                    path.appendleft(pred[index])
                    index = pred[index]
"""


start = 54
    end = 62
    passengers = [29, 63, 22, 18, 2, 23, 48, 41, 15, 31, 13, 4, 24, 16, 27, 17, 50, 67, 37, 58, 28, 64, 35, 10, 68, 38,
                  59, 26, 69, 43, 44, 30, 46, 7]
    roads = [
        (31, 45, 23, 12), (48, 3, 14, 7), (58, 50, 25, 10),
        (5, 3, 26, 23), (12, 32, 29, 3), (65, 4, 16, 16),
        (13, 46, 14, 13), (63, 29, 10, 2), (19, 56, 30, 19),
        (52, 47, 19, 12), (47, 52, 12, 8), (30, 42, 22, 19),
        (46, 60, 17, 17), (54, 22, 8, 7), (19, 8, 23, 10),
        (33, 51, 22, 5), (12, 17, 20, 5), (64, 62, 22, 18),
        (66, 25, 28, 10), (48, 19, 23, 8), (36, 13, 22, 19),
        (26, 48, 6, 3), (31, 30, 26, 9), (24, 29, 22, 11),
        (23, 36, 27, 11), (59, 37, 16, 10), (60, 44, 12, 8),
        (40, 7, 18, 1), (22, 3, 13, 12), (36, 35, 15, 15),
        (43, 2, 23, 6), (29, 27, 27, 6), (34, 0, 17, 4),
        (52, 50, 13, 4), (27, 23, 15, 1), (15, 10, 7, 6),
        (36, 65, 23, 1), (41, 64, 27, 8), (45, 34, 12, 1),
        (51, 24, 12, 10), (16, 12, 29, 7), (9, 67, 25, 24),
        (49, 38, 16, 4), (38, 7, 10, 1), (50, 13, 23, 16),
        (5, 33, 27, 10), (23, 42, 29, 15), (9, 2, 13, 7),
        (59, 52, 23, 17), (59, 54, 8, 6), (1, 8, 10, 8),
        (33, 30, 15, 2), (6, 26, 18, 6), (39, 57, 13, 12),
        (54, 26, 13, 9), (57, 41, 4, 4), (37, 66, 16, 12),
        (36, 9, 12, 5), (2, 68, 7, 3), (69, 28, 18, 2),
        (44, 1, 14, 3), (48, 9, 6, 4), (17, 38, 13, 1),
        (61, 49, 4, 4), (9, 10, 6, 3), (46, 37, 21, 8),
        (23, 53, 21, 8), (7, 24, 28, 26), (62, 20, 22, 7),
        (1, 18, 10, 1), (7, 41, 9, 1), (13, 18, 6, 4),
        (25, 21, 21, 3), (1, 61, 21, 16), (49, 40, 13, 5),
        (19, 25, 11, 10), (62, 50, 5, 5), (33, 46, 10, 9),
        (28, 25, 14, 6), (56, 51, 6, 4), (18, 19, 15, 1),
        (30, 9, 23, 13), (60, 21, 23, 7), (52, 37, 16, 6),
        (50, 42, 11, 4)]

    # Pred list: [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    #        None, None, None, None, 54, None, None, None, 54, None, None, None, None, None, None, None, None, None, None,
    #        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
    #        None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    # New Pred list: [None, 44, 9, 22, 65, None, None, 38, 19, 48, 9, None, None, 36, None, None, None, None, 13, 48, 62, 25, 54,
    #        27, 51, 19, 54, 29, None, 24, None, None, None, None, None, 36, 23, 46, 49, None, 49, 7, 23, None, 60, None,
    #        13, None, 26, 61, 62, 56, None, 23, None, None, 19, None, None, None, 46, 1, 64, None, 41, 36, 37, 9, 2,
    #        None]

    # 22 or 26
    #
    # start = 0
    # end = 5
    # passengers = [2, 1]
    # roads = [
    #     (4, 5, 200, 2),
    #     (0, 2, 2, 2),
    #     (1, 3, 10, 5),
    #     (3, 5, 50, 50),
    #     (2, 4, 10, 10),
    #     (0, 1, 1, 1)
    # ]
    # result = [0, 2, 4, 5]
    # Pred list: [None, 0, 0, None, None, None]
    # New Pred list: [None, 0, 0, 1, 2, 4]

    # start = 0
    # end = 4
    # passengers = [2, 1]
    # roads = [
    #     (0, 4, 30, 5),
    #     (0, 1, 5, 4),
    #     (1, 3, 3, 2),
    #     (3, 2, 2, 1),
    #     (2, 0, 1, 1)]
    # result = [0, 1, 3, 2, 0, 4]

    # start = 0
    # end = 3
    # passengers = [2, 1]
    # roads = [(0, 1, 10, 10), (1, 3, 100, 1), (0, 2, 2, 2), (2, 3, 60, 60), (2, 1, 6, 3)]
    # result = [0, 2, 1, 3]  # Optimal route is 6 minutes