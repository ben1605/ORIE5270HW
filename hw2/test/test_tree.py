import unittest
from tree.orie5270_tree import Tree, Node


class Test_tree(unittest.TestCase):
    def test1(self):
        node1 = Node(1, None, None)
        tree1 = Tree(node1)
        answer1 = [["1"]]
        assert tree1.print_tree() == answer1

    def test2(self):
        node1 = Node(1, None, None)
        node2 = Node(2, None, None)
        node3 = Node(3, None, None)
        node4 = Node(4, None, None)
        node5 = Node(5, None, None)
        node6 = Node(6, None, None)
        node7 = Node(7, None, None)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7
        tree2 = Tree(node1)
        answer2 = [['|', '|', '|', '1', '|', '|', '|'], ['|', '2', '|', '|', '|', '3', '|'],
                   ['4', '|', '5', '|', '6', '|', '7']]
        assert tree2.print_tree() == answer2

    def test3(self):
        node1 = Node(1, None, None)
        node2 = Node(2, None, None)
        node3 = Node(3, None, None)
        node4 = Node(4, None, None)
        node1.left = node2
        node2.left = node3
        node3.left = node4
        tree3 = Tree(node1)
        answer3 = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                   ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                   ['|', '3', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
                   ['4', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|']]
        assert tree3.print_tree() == answer3

    def test4(self):
        node1 = Node(1, None, None)
        node2 = Node(2, None, None)
        node3 = Node(3, None, None)
        node4 = Node(4, None, None)
        node5 = Node(5, None, None)
        node6 = Node(6, None, None)
        node1.left = node2
        node1.right = node3
        node2.right = node4
        node3.left = node5
        node5.right = node6
        tree4 = Tree(node1)
        answer4 = [['|', '|', '|', '|', '|', '|', '|', '1', '|', '|', '|', '|', '|', '|', '|'],
                   ['|', '|', '|', '2', '|', '|', '|', '|', '|', '|', '|', '3', '|', '|', '|'],
                   ['|', '|', '|', '|', '|', '4', '|', '|', '|', '5', '|', '|', '|', '|', '|'],
                   ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '6', '|', '|', '|', '|']]
        assert tree4.print_tree() == answer4
