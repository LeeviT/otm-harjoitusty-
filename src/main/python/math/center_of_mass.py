def calculate_com(node_storage, body_list, elem):
    body_ids = node_storage.get_ids_dict()[elem]
    total_mass = 0.0
    com_x = 0.0
    com_y = 0.0
    for i in range(0, len(body_ids)):
        k = body_ids[i] - 1
        com_x += body_list[k].get_x()*body_list[k].get_mass()
        com_y += body_list[k].get_y()*body_list[k].get_mass()
        total_mass += body_list[k].get_mass()
    return com_x/total_mass, com_y/total_mass
