from main.python.quadtree.body import Body


def write_new_timestep(output_file, timestep_n, upd_values):
    f = open(output_file, mode="a")
    f.write("timestep = " + str(timestep_n) + "\n" + "\n")
    for i in range(len(upd_values)):
        f.write("{}  {}  {}  {}  {}".format(upd_values[i][0], upd_values[i][1], upd_values[i][2],
                                            upd_values[i][3], upd_values[i][4]))
        f.write("\n")
    f.write("\n" + "---end of timestep---" + "\n" + "\n")
    f.close()


def read_previous_timestep(output_file, nob, timestep_n):
    if timestep_n == 1:
        first_body_line_num = 2
    else:
        first_body_line_num = 2 + (timestep_n - 1) * (5 + nob)
    input_data = [None] * nob
    body_list = [None] * nob
    i = 0
    with open(output_file, "r") as file:
        lines = file.readlines()[first_body_line_num:first_body_line_num + nob]
        for line in lines:
            input_data[i] = list(map(float, line.split()))
            body_id, mass, x = i + 1, input_data[i][0], input_data[i][1]
            y, vx, vy = input_data[i][2], input_data[i][3], input_data[i][4]
            body_list[i] = Body(body_id, mass, x, y, vx, vy)
            i += 1
    file.close()
    return body_list
