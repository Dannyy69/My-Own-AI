from models.vector import VectorItem
from algorithms.distance import get_distance


class BruteForce:

    def __init__(self):

        self.items = {}

    def insert(self, item: VectorItem):

        self.items[item.id] = item

    def remove(self, item_id: int):

        if item_id in self.items:

            del self.items[item_id]

    def clear(self):

        self.items.clear()

    def size(self):

        return len(self.items)

    def knn(

        self,

        query,

        k,

        distance_fn

    ):

        results = []

        for item in self.items.values():

            distance = distance_fn(

                query,

                item.emb

            )

            results.append(

                (

                    distance,

                    item.id

                )

            )

        results.sort(

            key=lambda x: x[0]

        )

        return results[:k]