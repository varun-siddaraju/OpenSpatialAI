from dataclasses import dataclass
from typing import Any


@dataclass
class SpatialBounds:
    """
    Describes the spatial extent of an entity.
    """

    type: str  # e.g. "box", "sphere", "mesh"
    geometry: Any  # engine-agnostic representation