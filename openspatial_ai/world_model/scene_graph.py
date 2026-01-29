from typing import Dict, List
from collections import defaultdict

from ..core import SpatialEntity
from .relation import SpatialRelation


class SceneGraph:
    """
    In-memory representation of spatial entities and their relationships.
    """

    def __init__(self):
        self.entities: Dict[str, SpatialEntity] = {}
        self.relations: List[SpatialRelation] = []

    def add_entity(self, entity: SpatialEntity) -> None:
        self.entities[entity.id] = entity

    def add_relation(self, relation: SpatialRelation) -> None:
        self.relations.append(relation)

    def get_entity(self, entity_id: str) -> SpatialEntity:
        return self.entities[entity_id]

    def get_relations_for(self, entity_id: str) -> List[SpatialRelation]:
        return [
            r for r in self.relations
            if r.subject_id == entity_id or r.object_id == entity_id
        ]