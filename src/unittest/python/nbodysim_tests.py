from unittest import TestCase
from main.python.structures.quadtree import Node

class TestNode(TestCase):

    def test_boolean(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_level(self):
        node = Node(0.0, 0.25, 0.25, 0.5, 'NW')
        level = node.getLevel()
        self.assertEqual(level, 2)

if __name__ == '__main__':
    unittest.main()
