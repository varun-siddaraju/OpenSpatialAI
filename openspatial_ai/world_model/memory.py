from typing import List
from .scene_graph import SceneGraph


class SpatialMemory:
    """
    Stores historical snapshots of the world state.
    """

    def __init__(self):
        self._history: List[SceneGraph] = []

    def store(self, scene_graph: SceneGraph) -> None:
        self._history.append(scene_graph)

    def retrieve(self, steps_back: int = 1) -> SceneGraph:
        if steps_back > len(self._history):
            raise IndexError("Not enough history available")
        return self._history[-steps_back]