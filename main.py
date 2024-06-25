import numpy as np
import matplotlib.pyplot as plt
from __init__ import level_file_data, sp_file_data, valve_file_data
from graphic import GraphicInfo


def join_graph_info_from(filedata):
    time, interval, result = list(), list(), list()

    filedata = filedata[1:]  # Jumps useless header info.

    for line in filedata:
        line = line.split()

        time.append(line[0])
        interval.append(line[1])
        result.append(line[2])

    time = np.array(time, dtype=float)
    interval = np.array(interval, dtype=float)
    result = np.array(result, dtype=float)

    return GraphicInfo(time, interval, result)


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
