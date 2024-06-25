resources_path = 'resources/'


def data_from(filename):
    with open(resources_path + filename, 'r') as file:
        return file.readlines()


# Standard results for showing at front page.
standard_level_file_data = data_from('nivel-tq2.txt')
standard_sp_file_data = data_from('sp-tq2.txt')
standard_valve_file_data = data_from('valve-tq2.txt')

# Adaptive gain comparison results.
ad_gain_level_file_data = data_from('AD-GAIN-lvl-tank2.txt')
ad_gain_sp_file_data = data_from('AD-GAIN-sp-tank2.txt')
ad_gain_valve_file_data = data_from('AD-GAIN-ab-valve.txt')

# Anti-reset windup comparison results.
arw_level_file_data = data_from('ARW-HI-lvl-tank2.txt')
arw_sp_file_data = data_from('ARW-HI-sp-tank2.txt')
arw_valve_file_data = data_from('ARW-HI-ab-valve.txt')

# Temperature test results
tank_temperature_file_data = data_from('temp2-tank.txt')
sp_temperature_file_data = data_from('temp2-sp.txt')

