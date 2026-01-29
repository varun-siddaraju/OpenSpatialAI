from dataclasses import dataclass
from typing import Optional


@dataclass
class SpatialRelation:
    """
    Represents a semantic or spatial relationship between two entities.
    """

    subject_id: str
    predicate: str            # e.g. "on", "near", "inside"
    object_id: str
    confidence: float = 1.0