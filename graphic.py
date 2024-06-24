from dataclasses import dataclass
from typing import List


@dataclass
class GraphicInfo:
    time: List[float]
    interval: List[float]
    result: List[float]
