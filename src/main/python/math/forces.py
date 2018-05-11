from math import sqrt
from numpy import sign


def calculate_forces(node_storage, body_list, theta):
    force_on_body_list = []
    for i in range(len(body_list)):
        calculated_nodes = []
        force_x = 0.0
        force_y = 0.0
        tmp_body = body_list[i]
        for j in range(len(body_list)):
            tmp_node = node_storage.get_childest_node_using_body_id(body_list[j].get_id())
            if tmp_node.get_id() != node_storage.get_childest_node_using_body_id(tmp_body.get_id()).get_id():
                if not tmp_node.is_empty():
                    force_x, force_y = calc_force_on_body(node_storage, tmp_node, tmp_body, theta, force_x, force_y,
                                                          calculated_nodes)
        force_on_body_list.append([tmp_body.get_id(), force_x, force_y])
    return force_on_body_list


def calc_force_on_body(node_storage, tmp_node, tmp_body, theta, force_x, force_y, calculated_nodes):
    G = 6.674e-11
    x_dist = tmp_node.get_com()[0] - tmp_body.get_x()
    y_dist = tmp_node.get_com()[1] - tmp_body.get_y()
    ratio_list = check_neighboring_nodes(node_storage, tmp_node, tmp_body)
    is_added = check_if_related_node_added(tmp_node, calculated_nodes)
    if theta >= ratio_list[0] or theta >= ratio_list[1] or theta >= ratio_list[2] or theta >= ratio_list[3]:
        tmp_id = int(str(tmp_node.get_id())[:-1])
        calc_force_on_body(node_storage, node_storage.get_node_using_id(tmp_id), tmp_body, theta, force_x, force_y,
                           calculated_nodes)
    else:
        if not is_added:
            if x_dist == 0.0:
                x_dist = 0.01
            if y_dist == 0.0:
                y_dist = 0.01
            force_x += sign(x_dist) * G * ((tmp_body.get_mass() * tmp_node.get_com()[2]) / x_dist ** 2)
            force_y += sign(y_dist) * G * ((tmp_body.get_mass() * tmp_node.get_com()[2]) / y_dist ** 2)
            calculated_nodes.append(tmp_node.get_id())
    return force_x, force_y


def check_neighboring_nodes(node_storage, tmp_node, tmp_body):
    if len(str(tmp_node.get_id())) > 1:
        reduced_id = int(str(tmp_node.get_id())[:-1])
    else:
        reduced_id = ''
    ratio_list = []
    for i in range(1, 5):
        current_node = node_storage.get_node_using_id(int(str(reduced_id) + str(i)))
        x_dist_current = current_node.get_com()[0] - tmp_body.get_x()
        y_dist_current = current_node.get_com()[1] - tmp_body.get_y()
        s_current = current_node.get_size()
        d_current = sqrt(x_dist_current ** 2 + y_dist_current ** 2)
        if not d_current == 0:
            ratio_list.append(s_current / d_current)
        else:
            ratio_list.append(0)
    return ratio_list


def check_if_related_node_added(tmp_node, calculated_nodes):
    is_added = False
    tmp_id = tmp_node.get_id()
    length = len(str(tmp_node.get_id()))
    for i in range(len(calculated_nodes)):
        if str(calculated_nodes[i]).find(str(tmp_id)) == 0:
            is_added = True
    for i in range(length - 1):
        if tmp_id in calculated_nodes:
            is_added = True
        tmp_id = int(str(tmp_id)[:-1])
    return is_added
