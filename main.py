import matplotlib.pyplot as plt
from __init__ import level_file_data, sp_file_data, valve_file_data
from graphic import join_graph_info_from


if __name__ == '__main__':
    level_info = join_graph_info_from(level_file_data)
    sp_info = join_graph_info_from(sp_file_data)
    valve_info = join_graph_info_from(valve_file_data)

    plt.plot(level_info.time,
             level_info.result,
             label='Level',
             color='green',
             linestyle='solid')
    plt.plot(sp_info.time,
             sp_info.result,
             label='Setpoint',
             color='blue',
             linestyle='dotted')
    plt.plot(valve_info.time,
             valve_info.result,
             label='Valve',
             color='red',
             linestyle='dashed')

    plt.legend()

    plt.savefig('graphics/level-sp-valve.png')
    plt.show()
