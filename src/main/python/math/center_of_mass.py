def calculate_coms(node_storage, body_list):
    for i in range(len(body_list)):
        body_ids = node_storage.get_ids_dict()[node_storage.get_node_using_index(i).get_id()]
        if not node_storage.get_node_using_index(i).is_empty():
            total_mass = 0.0
            total_x = 0.0
            total_y = 0.0
            for j in range(0, len(body_ids)):
                k = body_ids[j] - 1
                total_x += body_list[k].get_x()*body_list[k].get_mass()
                total_y += body_list[k].get_y()*body_list[k].get_mass()
                total_mass += body_list[k].get_mass()
            com_x = total_x / total_mass
            com_y = total_y / total_mass
            node_storage.get_node_using_index(i)

