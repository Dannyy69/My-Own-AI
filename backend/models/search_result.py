from dataclasses import dataclass


@dataclass(order=True)
class SearchResult:

    distance: float

    id: int