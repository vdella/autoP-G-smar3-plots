resources_path = 'resources/'


def data_from(filename):
    with open(resources_path + filename, 'r') as file:
        return file.readlines()


# Standard results for showing at front page.
standard_level_file_data = data_from('nivel-tq2.txt')
standard_sp_file_data = data_from('sp-tq2.txt')
standard_valve_file_data = data_from('valve-tq2.txt')

