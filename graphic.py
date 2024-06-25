from dataclasses import dataclass
import numpy as np


@dataclass
class GraphicInfo:
    time: np.array
    result: np.array


def join_graph_info_from(filedata):
    time, result = list(), list()

    filedata = filedata[1:]  # Jumps useless header info.

    for line in filedata:
        line = line.split()

        time.append(line[0])
        result.append(line[2])

    time = np.array(time, dtype=float)
    result = np.array(result, dtype=float)

    return GraphicInfo(time, result)
