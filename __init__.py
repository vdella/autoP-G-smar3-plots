resources_path = 'resources/'


def data_from(filename):
    with open(resources_path + filename, 'r') as file:
        return file.readlines()


level_file_data = data_from('nivel-tq2.txt')
sp_file_data = data_from('sp-tq2.txt')
valve_file_data = data_from('valve-tq2.txt')
