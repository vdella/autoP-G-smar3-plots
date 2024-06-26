import matplotlib.pyplot as plt
from __init__ import measured_temperature_file_data, temperature_sp_file_data
from graphic import join_graphic_info_from, plot


tank_temp_info = join_graphic_info_from(measured_temperature_file_data)
sp_temp_info = join_graphic_info_from(temperature_sp_file_data)


if __name__ == '__main__':
    tank_temp_info.color = 'blue'
    tank_temp_info.label = 'Temperatura'
    tank_temp_info.linestyle = 'solid'

    sp_temp_info.color = 'red'
    sp_temp_info.label = 'Setpoint'
    sp_temp_info.linestyle = 'dotted'

    plot(tank_temp_info, sp_temp_info)

    plt.savefig('graphics/temperature.png')
