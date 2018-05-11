class NodeStorage:

    def __init__(self):
        self.node_list = []
        self.ids_dict = {}
        self.storage_size = 0
        self.body_id = None

    def add_node_to_storage(self, node, body_id):
        if not self.do_contain_id(node.get_id()):
            self.node_list.append([node.get_id(), node, body_id])
            if node.get_id() not in self.ids_dict:
                if node.get_id() is not None:
                    self.ids_dict[node.get_id()] = []
            if body_id is not None:
                self.ids_dict[node.get_id()].append(body_id)
            self.storage_size += 1
        else:
            if body_id is not None:
                self.ids_dict[node.get_id()].append(body_id)
        return self.node_list

    def get_ids_dict(self):
        return self.ids_dict

    def get_size(self):
        return self.storage_size

    def get_node_using_index(self, i):
        return self.node_list[i][1]

    def get_non_empty_child_nodes(self, nbod):
        child_nodes = []
        for i in range(nbod):
            child_nodes.append([self.get_childest_node_using_body_id(i + 1).get_id(),
                                self.get_childest_node_using_body_id(i + 1).get_info(), i + 1])
        return child_nodes

    def get_childest_node_using_body_id(self, body_id):
        returnable = []
        for i in range(self.storage_size):
            if self.node_list[i][2] == body_id:
                returnable.append(self.node_list[i][1])
        return returnable[-1]

    def get_node_using_id(self, node_id):
        for i in range(self.storage_size):
            if self.node_list[i][0] == node_id:
                return self.node_list[i][1]

    def get_storage_element_using_id(self, node_id):
        for i in range(self.storage_size):
            if self.node_list[i][0] == node_id:
                return self.node_list[i]

    def do_contain_id(self, node_id):
        for i in range(self.storage_size):
            if self.node_list[i][0] == node_id:
                return True
        return False
