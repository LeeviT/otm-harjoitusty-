from math import sqrt
from numpy import sign


def calculate_forces(node_storage, body_list, theta):
    for i in range(len(body_list)):
        force_x = 0.0
        force_y = 0.0
        tmp_body = body_list[i]
        for j in range(len(body_list)):
            tmp_node = node_storage.get_childest_node_using_body_id(body_list[j].get_id())
            if tmp_node.get_id() != node_storage.get_childest_node_using_body_id(tmp_body.get_id()).get_id():
                if not tmp_node.is_empty():
                    force_x, force_y = calc_force_on_body(node_storage, tmp_node, tmp_body, theta, force_x, force_y)
        print(tmp_body.get_id(), "      |", force_x, " | ", force_y)


def calc_force_on_body(node_storage, tmp_node, tmp_body, theta, force_x, force_y):
    G = 6.674e-11
    x_dist = tmp_node.get_com()[0] - tmp_body.get_x()
    y_dist = tmp_node.get_com()[1] - tmp_body.get_y()
    d = sqrt(x_dist ** 2 + y_dist ** 2)
    s = tmp_node.get_size()
    if theta >= s / d:
        tmp_id = int(str(tmp_node.get_id())[:-1])
        # print(tmp_node.get_id(), tmp_id)
        calc_force_on_body(node_storage, node_storage.get_node_using_id(tmp_id), tmp_body, theta, force_x, force_y)
    elif theta < s / d:
        # print(tmp_node.get_id(), tmp_node.get_com())
        force_x += sign(x_dist) * G * ((tmp_body.get_mass() * tmp_node.get_com()[2]) / x_dist ** 2)
        force_y += sign(y_dist) * G * ((tmp_body.get_mass() * tmp_node.get_com()[2]) / y_dist ** 2)

    return force_x, force_y
