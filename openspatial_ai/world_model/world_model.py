from ..core import SpatialEntity
from .scene_graph import SceneGraph
from .memory import SpatialMemory
from .relation import SpatialRelation


class WorldModel:
    """
    Maintains the system's belief about the world.
    """

    def __init__(self):
        self.scene_graph = SceneGraph()
        self.memory = SpatialMemory()

    def update_entity(self, entity: SpatialEntity) -> None:
        self.scene_graph.add_entity(entity)

    def update_relation(self, relation: SpatialRelation) -> None:
        self.scene_graph.add_relation(relation)

    def snapshot(self) -> None:
        """
        Save current world state to memory.
        """
        self.memory.store(self.scene_graph)