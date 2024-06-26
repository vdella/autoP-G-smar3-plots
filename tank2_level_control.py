import matplotlib.pyplot as plt
from __init__ import standard_level_file_data, standard_sp_file_data, standard_valve_file_data
from graphic import join_graphic_info_from, plot


level_info = join_graphic_info_from(standard_level_file_data)
sp_info = join_graphic_info_from(standard_sp_file_data)
valve_info = join_graphic_info_from(standard_valve_file_data)


if __name__ == '__main__':
    level_info.color = 'green'
    level_info.label = 'Nível'
    level_info.linestyle = 'solid'

    sp_info.color = 'blue'
    sp_info.label = 'Setpoint'
    sp_info.linestyle = 'dotted'

    valve_info.color = 'red'
    valve_info.label = 'Válvula'
    valve_info.linestyle = 'dashed'

    plot(1, level_info, sp_info, valve_info)

    plt.savefig('graphics/standard.png')
