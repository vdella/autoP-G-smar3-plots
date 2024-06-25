from dataclasses import dataclass
import matplotlib.pyplot as plt
import numpy as np


@dataclass
class GraphicInfo:
    time: np.array
    result: np.array
    label: str
    color: str
    linestyle: str


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

    return GraphicInfo(time, result, label, 'black', 'solid')


def plot(*args):

    for arg in args:
        plt.plot(arg.time,
                 arg.result,
                 label=arg.label,
                 color=arg.color,
                 linestyle=arg.linestyle)

    plt.legend()

    return plt
