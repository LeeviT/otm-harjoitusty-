from main.python.structures.body import Body


class InputFileReader:

    def read_number_of_bodies(file_name):
        global nob
        file = open(file_name, "r")
        first_line = file.readline()
        nob = int(first_line[4:100])
        return nob

    def read_data_to_body_list(file_name):
        input_data = [None]*nob
        body_list = [None]*nob
        i = 0
        with open(file_name, "r") as file:
            lines = file.readlines()[1:]
            for line in lines:
                input_data[i] = list(map(float, line.split()))
                body_id, mass, x = i, input_data[i][0], input_data[i][1]
                y, vx, vy = input_data[i][2], input_data[i][3], input_data[i][4]
                body_list[i] = Body(body_id, mass, x, y, vx, vy)
                i += 1
        return body_list

    read_number_of_bodies("src/main/python/io/testi.dat")
    read_data_to_body_list("src/main/python/io/testi.dat")
