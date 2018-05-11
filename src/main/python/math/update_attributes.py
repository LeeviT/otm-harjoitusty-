def calc_updates(body_list, force_on_body_list, dt):
    upd_values = []
    for i in range(len(body_list)):
        vx_updated = body_list[i].get_vx() + dt * (force_on_body_list[i][1] / body_list[i].get_mass())
        vy_updated = body_list[i].get_vy() + dt * (force_on_body_list[i][2] / body_list[i].get_mass())
        x_updated = body_list[i].get_x() + dt * vx_updated
        y_updated = body_list[i].get_y() + dt * vy_updated
        if x_updated >= 1.0:
            x_updated = 0.95
        elif x_updated <= 0.0:
            x_updated = 0.05
        if y_updated >= 1.0:
            y_updated = 0.95
        elif y_updated <= 0.0:
            y_updated = 0.05
        upd_values.extend([[body_list[i].get_mass(), x_updated, y_updated, vx_updated, vy_updated]])
    return upd_values
