from main.python.structures.body import Body
from main.python.structures.quadtree import Node, NodeStorage


def main():
    body_list = []
    node_storage = NodeStorage()
    root_node = Node(0.0, 1.0, 0.0, 1.0, 'ROOT')
    node_storage.add_node_to_storage(0, root_node, None)
    test_body = Body(1, 1.2, 0.6, 0.1, 0.01, 0.01)
    test_body2 = Body(2, 1.2, 0.1, 0.1, 0.01, 0.01)
    test_body3 = Body(3, 1.2, 0.1, 0.15, 0.01, 0.01)
    body_list.extend((test_body, test_body2, test_body3))
    root_node.add_body_to_quadtree(test_body, node_storage, body_list)
    root_node.add_body_to_quadtree(test_body2, node_storage, body_list)
    root_node.add_body_to_quadtree(test_body3, node_storage, body_list)
    node_storage.print_node_storage()
    print(node_storage.get_non_empty_child_nodes(3))

main()
