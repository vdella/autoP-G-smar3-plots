from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np


@dataclass
class GraphicInfo:
    time: np.array
    result: np.array
    label: str
    color: str = 'black'
    linestyle: str = 'solid'
    position: int = 0  # States into which column the graphic info must be placed.


def join_graphic_info_from(filedata):
    time, result = list(), list()

    label = filedata[0].split()[2:]
    filedata = filedata[1:]  # Jumps useless header info.

    for line in filedata:
        line = line.split()

        time.append(line[0])
        result.append(line[2])

    time = np.array(time, dtype=float)
    result = np.array(result, dtype=float)

    return GraphicInfo(time, result, label)


def plot(cols=1, *args):
    _, axis = plt.subplots(cols)

    for arg in args:
        column = arg.position

        if cols > 1:
            axis[column].plot(arg.time,
                              arg.result,
                              label=arg.label,
                              color=arg.color,
                              linestyle=arg.linestyle)
            axis[column].legend()
        else:
            axis.plot(arg.time,
                      arg.result,
                      label=arg.label,
                      color=arg.color,
                      linestyle=arg.linestyle)
            axis.legend()

    return plt
