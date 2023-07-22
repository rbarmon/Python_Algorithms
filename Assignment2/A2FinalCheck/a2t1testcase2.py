
import unittest

__author__ = "TAL"

# from a2t1 import maxThroughput
# from a2t1rethink import maxThroughput
# from a2t1Final import maxThroughput
from Assignments.Assignment2.assignment2 import maxThroughput


class Q1Test(unittest.TestCase):


    #2 Fails with Errors
    # passes as long as float('inf')
    def test1(self):
        connections = [(0, 1, 10), (1, 2, 5), (1, 3, 7), (3, 4, 10)]
        # maxIn = [inf, 10, 5, 7, inf]
        maxIn = [float('inf'), 10, 5, 7, float('inf')]
        # maxOut = [inf, 10, 5, 10, inf]
        maxOut = [float('inf'), 10, 5, 10, float('inf')]
        origin = 0
        targets = [2, 4]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 10)

    def test(self):
        connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000),
                       (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]
        maxIn = [5000, 3000, 3000, 2000, 2000]
        maxOut = [5000, 3000, 3000, 2000, 1500]
        origin = 0
        targets = [4, 2]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 4000)

    def test2(self):
        connections = [(0, 1, 20), (1, 3, 30), (1, 4, 5), (0, 2, 10), (2, 4, 15)]
        # maxIn = [inf, inf, inf, inf, inf]
        maxIn = [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
        # maxOut = [inf, inf, inf, inf, inf]
        maxOut = [float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]
        origin = 0
        targets = [3, 4]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 30)


    def test3(self):
        connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000),
                       (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]
        maxIn = [5000, 3000, 3000, 3000, 2000]
        maxOut = [5000, 3000, 3000, 2500, 1500]
        origin = 3
        targets = [4, 2]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 2500)


    def test4(self):
        connections = [(0, 1, 30), (1, 3, 30), (1, 4, 30), (0, 2, 30), (2, 4, 30)]
        maxIn = [5, 5, 5, 5, 5]
        maxOut = [1000, 1000, 1000, 1000, 1000]
        origin = 0
        targets = [3, 4]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 10)


    def test5(self):
        connections = [(0, 1, 30), (1, 3, 30), (1, 4, 30), (0, 2, 30), (2, 4, 30)]
        maxIn = [1000, 1000, 1000, 1000, 1000]
        maxOut = [100, 5, 5, 5, 5]
        origin = 0
        targets = [3, 4]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 10)


    def test6(self):
        connections = [(0, 1, 30), (1, 3, 30), (1, 4, 30), (0, 2, 30), (2, 4, 30)]
        maxIn = [1000, 1000, 1000, 1000, 1000]
        maxOut = [1, 1000, 1000, 1000, 1000]
        origin = 0
        targets = [3, 4]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 1)


    def test7(self):
        connections = [(0, 1, 30), (1, 3, 30), (1, 4, 30), (0, 2, 30), (2, 4, 30)]
        maxIn = [1000, 1000, 1000, 1000, 1000]
        maxOut = [1000, 1000, 1000, 1000, 1000]
        origin = 0
        targets = [1, 2, 3, 4]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 60)


    def test9(self):
        connections = [(0, 1, 3000), (0, 2, 2000)]
        maxIn = [5000, 0, 0]
        maxOut = [5000, 0, 0]
        origin = 0
        targets = [1, 2]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 0)


    def test10(self):
        connections = [(0, 1, 1000), (0, 2, 2000), (2, 1, 3000)]
        maxIn = [5000, 4000, 3000]
        maxOut = [5000, 4000, 3000]
        origin = 0
        targets = [1]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 3000)


    def test11(self):
        connections = [(0, 1, 1000), (0, 2, 2000), (0, 3, 3000)]
        maxIn = [5000, 1000, 2000, 3000]
        maxOut = [10000, 1000, 2000, 3000]
        origin = 0
        targets = [1, 2, 3]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 6000)


    def test12(self):
        connections = [(0, 1, 3000), (0, 2, 2000)]
        maxIn = [0, 5000, 5000]
        maxOut = [0, 5000, 5000]
        origin = 0
        targets = [1, 2]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 0)


    def test14(self):
        connections = [(0, 1, 2000), (0, 2, 2000)]
        maxIn = [5000, 2000, 2000]
        maxOut = [5000, 2000, 2000]
        origin = 0
        targets = [1, 2]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 4000)


    def test15(self):
        connections = [(0, 1, 3000)]
        maxIn = [5000, 3000]
        maxOut = [5000, 3000]
        origin = 0
        targets = [1]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 3000)


    def test16(self):
        connections = [(0, 1, 0), (0, 2, 0)]
        maxIn = [5000, 5000, 5000]
        maxOut = [5000, 5000, 5000]
        origin = 0
        targets = [1, 2]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 0)


    def test17(self):
        connections = [(0, 1, 1000), (0, 2, 1000), (0, 3, 1000)]
        maxIn = [5000, 1000, 1000, 1000]
        maxOut = [5000, 1000, 1000, 1000]
        origin = 0
        targets = [1, 2, 3]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 3000)


    # ------------------------SOME OTHER DUDE------------------------------------------------------------------------------------

    def edge_case(self):
        connections = [(0, 1, 3000), (1, 2, 2000), (1, 3, 1000), (0, 3, 2000), (3, 4, 2000), (3, 2, 1000)]
        maxIn = [5000, 3000, 3000, 3000, 2000]
        maxOut = [5000, 3000, 3000, 2500, 2000]
        origin = 0
        targets = [4, 2]
        self.assertEqual(maxThroughput(connections, maxIn, maxOut, origin, targets), 4500)

if __name__ == "__main__":
    unittest.main()