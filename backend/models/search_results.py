from dataclasses import dataclass

from models.vector import Vector


@dataclass(order=True)
class SearchResult:

    distance: float

    vector: Vector