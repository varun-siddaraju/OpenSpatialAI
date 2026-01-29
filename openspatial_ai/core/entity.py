from dataclasses import dataclass, field
from typing import Dict, Any, Optional
from uuid import uuid4

from .pose import Pose3D
from .bounds import SpatialBounds


@dataclass
class SpatialEntity:
    """
    A semantic object in the spatial world.
    """

    id: str = field(default_factory=lambda: str(uuid4()))
    pose: Optional[Pose3D] = None
    bounds: Optional[SpatialBounds] = None
    semantic_label: Optional[str] = None
    properties: Dict[str, Any] = field(default_factory=dict)
    confidence: float = 1.0