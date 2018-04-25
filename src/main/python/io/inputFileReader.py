from main.python.quadtree.body import Body


def read_number_of_bodies(file_name):
    file = open(file_name, "r")
    first_line = file.readline()
    nob = int(first_line[4:100])
    file.close()
    return nob


def read_data_to_body_list(file_name):
    nob = read_number_of_bodies(file_name)
    input_data = [None]*nob
    body_list = [None]*nob
    i = 0
    with open(file_name, "r") as file:
        lines = file.readlines()[1:]
        for line in lines:
            input_data[i] = list(map(float, line.split()))
            body_id, mass, x = i + 1, input_data[i][0], input_data[i][1]
            y, vx, vy = input_data[i][2], input_data[i][3], input_data[i][4]
            body_list[i] = Body(body_id, mass, x, y, vx, vy)
            i += 1
    file.close()
    return body_list
