from main.python.io.inputFileReader import read_data_to_body_list
from main.python.quadtree.node import Node
from main.python.quadtree.node_storage import NodeStorage
from main.python.math.center_of_mass import calculate_com


def main():
    body_list = read_data_to_body_list("randominput.dat")
    node_storage = NodeStorage()
    root_node = Node(0.0, 1.0, 0.0, 1.0, 'ROOT')
    node_storage.add_node_to_storage(root_node, None)

    for i in range(100):
        root_node.add_body_to_quadtree(body_list[i], node_storage, body_list)

    # print(node_storage.get_non_empty_child_nodes(10))
    # node_storage.print_node_storage()
    # print(node_storage.get_childest_node_using_body_id(10).get_info())
    # print(node_storage.get_ids_dict()[1])
    print("Center of mass in root node:")
    print(calculate_com(node_storage, body_list, 0))
