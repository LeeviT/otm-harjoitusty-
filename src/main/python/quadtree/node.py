import math
from main.python.quadtree.node_direction import NodeDirection


class Node:

    id = 0

    def __init__(self, x0, xh, y0, yh, direction):
        self.x0 = x0
        self.x1 = xh
        self.y0 = y0
        self.y1 = yh
        self.direction = direction
        self.isEmpty = True
        self.hasChildren = False

    def is_body_in_node(self, body):
        if (body.get_x() > self.x0) & (body.get_x() < self.x1) & (body.get_y() > self.y0) & (body.get_y() < self.y1):
            return True
        else:
            return False

    def add_body_to_node(self, body, node_storage):
        self.isEmpty = False
        node_storage.get_storage_element_using_id(self.id)[2] = body.get_id()

    def divide_node(self, node_storage, body_list):
        node_storage.get_node_using_id(self.id).hasChildren = True
        sw_node = Node(self.x0, (self.x0 + self.x1) / 2.0, self.y0, (self.y0 + self.y1) / 2.0, NodeDirection.SW.name)
        nw_node = Node(self.x0, (self.x0 + self.x1) / 2.0, (self.y0 + self.y1) / 2.0, self.y1, NodeDirection.NW.name)
        ne_node = Node((self.x0 + self.x1) / 2.0, self.x1, (self.y0 + self.y1) / 2.0, self.y1, NodeDirection.NE.name)
        se_node = Node((self.x0 + self.x1) / 2.0, self.x1, self.y0, (self.y0 + self.y1) / 2.0, NodeDirection.SE.name)
        sw_node.id = sw_node.generate_node_id(self.id)
        nw_node.id = nw_node.generate_node_id(self.id)
        ne_node.id = ne_node.generate_node_id(self.id)
        se_node.id = se_node.generate_node_id(self.id)
        self.add_to_child_node(node_storage, sw_node, nw_node, ne_node, se_node, body_list)

    def add_to_child_node(self, node_storage, sw_node, nw_node, ne_node, se_node, body_list):
        comm_id = node_storage.get_storage_element_using_id(self.id)[2]
        comm_body = body_list[comm_id - 1]
        if sw_node.is_body_in_node(comm_body):
            sw_node.isEmpty = False
            node_storage.add_node_to_storage(sw_node, comm_body.get_id())
        else:
            node_storage.add_node_to_storage(sw_node, None)
        if nw_node.is_body_in_node(comm_body):
            nw_node.isEmpty = False
            node_storage.add_node_to_storage(nw_node, comm_body.get_id())
        else:
            node_storage.add_node_to_storage(nw_node, None)
        if ne_node.is_body_in_node(comm_body):
            ne_node.isEmpty = False
            node_storage.add_node_to_storage(ne_node, comm_body.get_id())
        else:
            node_storage.add_node_to_storage(ne_node, None)
        if se_node.is_body_in_node(comm_body):
            se_node.isEmpty = False
            node_storage.add_node_to_storage(se_node, comm_body.get_id())
        else:
            node_storage.add_node_to_storage(se_node, None)

    def add_body_to_quadtree(self, body, node_storage, body_list):
        if self.is_body_in_node(body):
            node_storage.add_node_to_storage(self, body.get_id())
            if not self.isEmpty:
                if not self.hasChildren:
                    self.divide_node(node_storage, body_list)
                    for i in range(1, 5):
                        if self.id == 0:
                            temp_node = node_storage.get_node_using_id(i)
                        else:
                            temp_node = node_storage.get_node_using_id(int(str(self.id) + str(i)))
                        temp_node.add_body_to_quadtree(body, node_storage, body_list)
                elif self.hasChildren:
                    for i in range(1, 5):
                        if self.id == 0:
                            temp_node = node_storage.get_node_using_id(i)
                        else:
                            temp_node = node_storage.get_node_using_id(int(str(self.id) + str(i)))
                        temp_node.add_body_to_quadtree(body, node_storage, body_list)
            elif self.isEmpty:
                self.add_body_to_node(body, node_storage)

    def generate_node_id(self, parent_node_id):
        if self.direction == 'ROOT':
            return parent_node_id
        elif self.direction == 'SW':
            return int(str(parent_node_id) + '1')
        elif self.direction == 'NW':
            return int(str(parent_node_id) + '2')
        elif self.direction == 'NE':
            return int(str(parent_node_id) + '3')
        elif self.direction == 'SE':
            return int(str(parent_node_id) + '4')

    def get_id(self):
        return self.id

    def get_info(self):
        return self.id, self.x0, self.x1, self.y0, self.y1

    def get_level(self):
        return int(math.log(1 / (self.x1 - self.x0), 2))
