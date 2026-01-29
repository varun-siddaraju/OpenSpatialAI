from dataclasses import dataclass
from typing import Tuple
from datetime import datetime


@dataclass
class Pose3D:
    """
    Represents a 3D pose in a given reference frame.
    """

    position: Tuple[float, float, float]
    rotation: Tuple[float, float, float, float]  # quaternion (x, y, z, w)
    reference_frame: str
    timestamp: datetime