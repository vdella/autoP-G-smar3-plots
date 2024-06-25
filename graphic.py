from dataclasses import dataclass
import numpy as np


@dataclass
class GraphicInfo:
    time: np.array
    interval: np.array
    result: np.array
