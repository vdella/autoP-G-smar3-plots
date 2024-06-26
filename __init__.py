resources_path = 'resources/'


def data_from(filename):
    with open(resources_path + filename, 'r') as file:
        return file.readlines()


# Standard results for showing at front page.
standard_level_file_data = data_from('standard/level.txt')
standard_sp_file_data = data_from('standard/sp.txt')
standard_valve_file_data = data_from('standard/valve.txt')

# Adaptive gain comparison results.
ad_gain_level_file_data = data_from('ad_gain/level.txt')
ad_gain_sp_file_data = data_from('ad_gain/sp.txt')
ad_gain_valve_file_data = data_from('ad_gain/valve.txt')

# Anti-reset windup comparison results.
arw_level_file_data = data_from('antireset_windup/level.txt')
arw_sp_file_data = data_from('antireset_windup/sp.txt')
arw_valve_file_data = data_from('antireset_windup/valve.txt')

# Temperature test results
measured_temperature_file_data = data_from('temperature/temp.txt')
temperature_sp_file_data = data_from('temperature/temp-sp.txt')
tank2_level_temp_sim_file_data = data_from('temperature/tank-level.txt')
tank2_valve_temp_sim_file_data = data_from('temperature/tank-valve.txt')
tank2_sp_temp_sim_file_data = data_from('temperature/tank-sp.txt')
