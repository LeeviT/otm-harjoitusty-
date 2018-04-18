from unittest import TestCase
from main.python.structures.quadtree import Node
import main.python.io.inputFileReader
#import main.python.tmpMain.tmpmain

class TestNode(TestCase):

    def test_level(self):
        node = Node(0.0, 0.25, 0.25, 0.5, 'NW')
        level = node.get_level()
        self.assertEqual(level, 2)

#if __name__ == '__main__':
#    unittest.main()
