import matplotlib.pyplot as plt
from __init__ import (measured_temperature_file_data, temperature_sp_file_data,
                      tank2_level_temp_sim_file_data, tank2_sp_temp_sim_file_data, tank2_valve_temp_sim_file_data)
from graphic import join_graphic_info_from, plot

actual_temp_info = join_graphic_info_from(measured_temperature_file_data)
sp_temp_info = join_graphic_info_from(temperature_sp_file_data)

tank2_level_temp_info = join_graphic_info_from(tank2_level_temp_sim_file_data)
tank2_sp_temp_info = join_graphic_info_from(tank2_sp_temp_sim_file_data)
tank2_valve_temp_info = join_graphic_info_from(tank2_valve_temp_sim_file_data)

if __name__ == '__main__':
    actual_temp_info.color = 'blue'
    actual_temp_info.label = 'Temperatura'
    actual_temp_info.linestyle = 'solid'

    sp_temp_info.color = 'red'
    sp_temp_info.label = 'Setpoint'
    sp_temp_info.linestyle = 'dotted'

    tank2_level_temp_info.color = 'green'
    tank2_level_temp_info.label = 'Nível'
    tank2_level_temp_info.linestyle = 'solid'
    tank2_level_temp_info.position = 1

    tank2_sp_temp_info.color = 'blue'
    tank2_sp_temp_info.label = 'Setpoint'
    tank2_sp_temp_info.linestyle = 'dotted'
    tank2_sp_temp_info.position = 1

    tank2_valve_temp_info.color = 'red'
    tank2_valve_temp_info.label = 'Válvula'
    tank2_valve_temp_info.linestyle = 'dashed'
    tank2_valve_temp_info.position = 1

    plot(2,
         actual_temp_info,
         sp_temp_info,
         tank2_level_temp_info,
         tank2_sp_temp_info,
         tank2_valve_temp_info)

    plt.savefig('graphics/temperature.png')
