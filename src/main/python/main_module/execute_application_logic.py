import os
from time import gmtime, strftime
from main.python.io.input_file_reader import read_data_to_body_list
from main.python.io.timestep_file_handler import write_new_timestep, read_previous_timestep
from main.python.quadtree.node import Node
from main.python.quadtree.node_storage import NodeStorage
from main.python.math.center_of_mass import calculate_coms
from main.python.math.forces import calculate_forces
from main.python.math.update_attributes import calc_updates
from main.python.ui.set_parameters import StartGUI
from main.python.ui.calculation_phase import CalculationView
from main.python.ui.final_info import FinalView


def main():
    input_file, n_timesteps, simulation_accuracy = StartGUI().return_params()
    timestep_counter = CalculationView(n_timesteps)
    timestep_counter.update_current_timestep(0)
    nob, body_list = read_data_to_body_list(input_file)
    simulation_accuracy = 0.01 + 0.03 * simulation_accuracy
    output_file = str("src/main/resources/nbodysim" + str(nob) + "_OUT_" + strftime("%Y-%m-%d_%H:%M:%S", gmtime()))
    try:
        os.remove(output_file)
    except OSError:
        pass
    node_storage = NodeStorage()
    root_node = Node(0.0, 1.0, 0.0, 1.0, 'ROOT')
    node_storage.add_node_to_storage(root_node, None)
    for i in range(nob):
        root_node.add_body_to_quadtree(body_list[i], node_storage, body_list)
    calculate_coms(node_storage, body_list)
    force_on_body_list = calculate_forces(node_storage, body_list, simulation_accuracy)
    upd_values = calc_updates(body_list, force_on_body_list, 0.001)
    write_new_timestep(output_file, 0, upd_values)
    for timestep in range(0, n_timesteps):
        timestep_counter.update_current_timestep(timestep + 1)
        print("timestep = " + str(timestep))
        calculate_timestep(timestep, output_file, nob)
    print("output file saved to: " + output_file)
    FinalView(output_file)


def calculate_timestep(timestep, output_file, nob):
    timestep += 1
    body_list = read_previous_timestep(output_file, nob, timestep)
    node_storage = NodeStorage()
    root_node = Node(0.0, 1.0, 0.0, 1.0, 'ROOT')
    node_storage.add_node_to_storage(root_node, None)
    for i in range(nob):
        root_node.add_body_to_quadtree(body_list[i], node_storage, body_list)
    calculate_coms(node_storage, body_list)
    force_on_body_list = calculate_forces(node_storage, body_list, 0.1)
    upd_values = calc_updates(body_list, force_on_body_list, 0.001)
    write_new_timestep(output_file, timestep, upd_values)
