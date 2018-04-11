from unittest import TestCase

from src.main.python.structures.quadtree import Node

class TestNode(TestCase):

    def setUp(self):
        self.node = Node(0.0, 0.25, 0.25, 0.5, 'NW')

    def test_sum(self):
        level = self.node.getLevel()
        self.assertEqual(level, 2)
