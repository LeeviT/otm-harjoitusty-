from unittest import TestCase
from main.python.quadtree.node import Node
from main.python.quadtree.body import Body
from enum import Enum
from main.python.quadtree.node_storage import NodeStorage
from main.python.quadtree.node_direction import NodeDirection
from main.python.math.center_of_mass import calculate_com
from main.python.io.inputFileReader import read_data_to_body_list, read_number_of_bodies


class TestInputFileReader(TestCase):

    def test_read_number_of_bodies(self):
        nob = read_number_of_bodies("src/main/resources/randominput.dat")
        self.assertEqual(nob, 100)


class TestNodeDirection(TestCase, Enum):

    def test_init(self):
        NodeDirection(Enum)


class TestCenterOfMass(TestCase):

    def test_calculate_com(self):
        body_list = []
        body1 = Body(1, 1.0, 0.25, 0.5, 0.1, 0.1)
        body2 = Body(2, 1.0, 0.75, 0.5, 0.1, 0.1)
        body_list.append(body1)
        body_list.append(body2)
        node = Node(0.0, 1.0, 0.0, 1.0, 'ROOT')
        node_storage = NodeStorage()
        node_storage.add_node_to_storage(node, body1.get_id())
        node_storage.add_node_to_storage(node, body2.get_id())
        com = calculate_com(node_storage, body_list, 0)
        self.assertEqual(com, (0.5, 0.5))


class TestNode(TestCase):

    def test_level(self):
        node = Node(0.0, 0.25, 0.25, 0.5, 'NW')
        level = node.get_level()
        self.assertEqual(level, 2)


class TestBody(TestCase):

    def test_get_id(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        body_id = body.get_id()
        self.assertEqual(body_id, 1)

    def test_get_mass(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        mass = body.get_mass()
        self.assertEqual(mass, 12.0)

    def test_get_x(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        x = body.get_x()
        self.assertEqual(x, 0.3)

    def test_get_y(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        y = body.get_y()
        self.assertEqual(y, 0.6)

    def test_get_vx(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        vx = body.get_vx()
        self.assertEqual(vx, 0.1)

    def test_get_vy(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        vy = body.get_vy()
        self.assertEqual(vy, 0.2)

    def test_get_visualize(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        visualize = body.get_visualize()
        self.assertEqual(visualize, (12.0, 0.3, 0.6))
