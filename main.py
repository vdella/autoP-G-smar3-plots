import numpy as np
import matplotlib.pyplot as plt
from __init__ import level_file_data, sp_file_data, valve_file_data


def join_graph_info_from(filedata):
    time, interval, result = list(), list(), list()

    filedata = filedata[1:]  # Jumps useless header info.

    for line in filedata:
        line = line.split()

        time.append(line[0])
        interval.append(line[1])
        result.append(line[2])

    for t, _ in enumerate(time):
        print(f'{time[t]} {interval[t]} {result[t]}')


if __name__ == '__main__':
    join_graph_info_from(level_file_data)
    join_graph_info_from(sp_file_data)
    join_graph_info_from(valve_file_data)
