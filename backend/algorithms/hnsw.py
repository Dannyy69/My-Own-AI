import math
import heapq
import random

from dataclasses import dataclass, field
from typing import Dict, List

from models.vector import VectorItem
from algorithms.distance import cosine


@dataclass
class HNSWNode:

    vector: VectorItem

    max_level: int

    neighbors: List[List[int]] = field(default_factory=list)


class HNSW:

    def __init__(

        self,

        m: int = 16,

        ef_build: int = 200

    ):

        self.graph: Dict[int, HNSWNode] = {}

        self.M = m

        self.M0 = 2 * m

        self.ef_build = ef_build

        self.ml = 1.0 / math.log(m)

        self.top_layer = -1

        self.entry_point = None

        random.seed(42)

    def random_level(self):

        u = random.random()

        return int(

            math.floor(

                -math.log(u)

                * self.ml

            )

        )

    def select_neighbors(

        self,

        candidates,

        max_m

    ):

        candidates.sort(

            key=lambda x: x[0]

        )

        return [

            node_id

            for _, node_id

            in candidates[:max_m]

        ]
    def size(self):

        return len(

            self.graph

        )

    def clear(self):

        self.graph.clear()

        self.entry_point = None

        self.top_layer = -1    

    def search_layer(
    self,
    query: VectorItem,
        entry_point: int,
        ef: int,
        layer: int,
    ):

        visited = set()

        candidates = []

        found = []

        start_distance = cosine(
           query.emb if hasattr(query, "emb") else query,
            self.graph[entry_point].vector.emb
     )

        heapq.heappush(
            candidates,
            (
                start_distance,
                entry_point
            )
        )

        heapq.heappush(
            found,
            (
                -start_distance,
                entry_point
            )
        )

        visited.add(
            entry_point
        )

        while candidates:

            current_distance, current = heapq.heappop(
                candidates
            )

            if (
                len(found) >= ef
                and
                current_distance > -found[0][0]
            ):
                break

            node = self.graph[current]

            if layer >= len(node.neighbors):
                continue

            for neighbor in node.neighbors[layer]:

                if neighbor in visited:
                    continue

                if neighbor not in self.graph:
                    continue

                visited.add(neighbor)

                distance = cosine(
                    query.emb if hasattr(query, "emb") else query,
                    self.graph[neighbor].vector.emb
                )

                if (
                    len(found) < ef
                    or
                    distance < -found[0][0]
                ):

                    heapq.heappush(
                        candidates,
                        (
                            distance,
                            neighbor
                        )
                    )

                    heapq.heappush(
                        found,
                        (
                            -distance,
                            neighbor
                        )
                    )

                    if len(found) > ef:
                        heapq.heappop(found)

        result = []

        while found:

            distance, node = heapq.heappop(
                found
            )

            result.append(
                (
                    -distance,
                    node
                )
            )

        result.sort(
            key=lambda x: x[0]
        )

        return result
    def insert(
        self,
        vector: VectorItem
    ):

        node_id = vector.id

        level = self.random_level()

        self.graph[node_id] = HNSWNode(
            vector=vector,
            max_level=level,
            neighbors=[
                [] for _ in range(level + 1)
            ]
        )

        if self.entry_point is None:

            self.entry_point = node_id

            self.top_layer = level

            return

        entry = self.entry_point

        #
        # Traverse from top layer down
        #
        for current_layer in range(
            self.top_layer,
            level,
            -1
        ):

            if current_layer < len(
                self.graph[entry].neighbors
            ):

                result = self.search_layer(
                    vector,
                    entry,
                    1,
                    current_layer
                )

                if result:

                    entry = result[0][1]

        #
        # Connect layers
        #
        for current_layer in range(

            min(
                self.top_layer,
                level
            ),

            -1,

            -1

        ):

            result = self.search_layer(

                vector,

                entry,

                self.ef_build,

                current_layer

            )

            max_neighbors = (

                self.M0

                if current_layer == 0

                else self.M

            )

            selected = self.select_neighbors(

                result,

                max_neighbors

            )

            self.graph[node_id].neighbors[
                current_layer
            ] = selected
                        #
            # Bidirectional links
            #
            for neighbor in selected:

                if neighbor not in self.graph:
                    continue

                while len(
                    self.graph[neighbor].neighbors
                ) <= current_layer:

                    self.graph[neighbor].neighbors.append([])

                connections = self.graph[
                    neighbor
                ].neighbors[current_layer]

                connections.append(
                    node_id
                )

                if len(connections) > max_neighbors:

                    distances = []

                    for candidate in connections:

                        if candidate not in self.graph:
                            continue

                        d = cosine(
                            self.graph[neighbor].vector.emb,
                            self.graph[candidate].vector.emb
)

                        distances.append(

                            (
                                d,
                                candidate
                            )

                        )

                    distances.sort(
                        key=lambda x: x[0]
                    )

                    self.graph[
                        neighbor
                    ].neighbors[
                        current_layer
                    ] = [

                        candidate

                        for _, candidate

                        in distances[:max_neighbors]

                    ]

            if result:

                entry = result[0][1]

        #
        # Update entry point
        #
        if level > self.top_layer:

            self.top_layer = level

            self.entry_point = node_id
    def knn(
        self,
        query: VectorItem,
        k: int = 5,
        ef: int = 50
    ):

        if self.entry_point is None:
            return []

        entry = self.entry_point

        #
        # Greedy search from top layer
        #
        for current_layer in range(
            self.top_layer,
            0,
            -1
        ):

            if current_layer < len(
                self.graph[entry].neighbors
            ):

                result = self.search_layer(
                    query,
                    entry,
                    1,
                    current_layer
                )

                if result:
                    entry = result[0][1]

        result = self.search_layer(
            query,
            entry,
            max(
                ef,
                k
            ),
            0
        )

        return result[:k]
    def remove(
        self,
        node_id: int
    ):

        if node_id not in self.graph:
            return

        for other in self.graph.values():

            for layer in other.neighbors:

                if node_id in layer:

                    layer.remove(
                        node_id
                    )

        if self.entry_point == node_id:

            self.entry_point = None

            for nid in self.graph:

                if nid != node_id:

                    self.entry_point = nid

                    break

        del self.graph[node_id] 

    def get_info(self):

        info = {

            "top_layer": self.top_layer,

            "node_count": len(
                self.graph
            ),

            "layers": [],

            "nodes": []

        }

        for node_id, node in self.graph.items():

            info["nodes"].append(

                {

                    "id": node_id,

                    "max_level": node.max_level,

                    "layers": len(
                        node.neighbors
                    )

                }

            )

        return info      