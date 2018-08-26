import unittest
from Path import path


class Test_path(unittest.TestCase):

    def test1(self):
        answer1 = ([1.0, 3.0, 2.0, 5.0], 6.0)
        assert path.find_shortest_path("g11.txt", 1, 5) == answer1

    def test2(self):
        answer2 = [[4, 1, 2, 3, 4],
                   [1, 2, 3, 4, 1],
                   [2, 3, 4, 1, 2],
                   [3, 4, 1, 2, 3]]
        assert path.find_negative_cycles("g5.txt") in answer2

    def test3(self):
        answer3 = ([], float("inf"))
        assert path.find_shortest_path("g12.txt", 1, 3) == answer3

    def test4(self):
        answer4 = []
        assert path.find_negative_cycles("g6.txt") == answer4

    def test5(self):
        answer5 = []
        assert path.find_negative_cycles("g7.txt") == answer5
