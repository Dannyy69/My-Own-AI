import time
from threading import Lock

from models.vector import VectorItem
from algorithms.bruteforce import BruteForce
from algorithms.kdtree import KDTree
from algorithms.hnsw import HNSW
from algorithms.distance import get_distance


class VectorDB:

    def __init__(self, dims):

        self.store = {}

        self.lock = Lock()

        self.next_id = 1

        self.dims = dims

        self.bruteforce = BruteForce()

        self.kdtree = KDTree()

        self.hnsw = HNSW()
    def insert(

        self,

        metadata,

        category,

        embedding,

        metric="cosine"

    ):

        with self.lock:

            item = VectorItem(

                id=self.next_id,

                metadata=metadata,

                category=category,

                emb=embedding

            )

            self.store[item.id] = item

            self.bruteforce.insert(item)

            self.kdtree.insert(item)

            self.hnsw.insert(item)

            self.next_id += 1

            return item.id    
    def remove(

        self,

        item_id

    ):

        with self.lock:

            if item_id not in self.store:

                return False

            del self.store[item_id]

            self.bruteforce.remove(item_id)

            self.hnsw.remove(item_id)

            return True
    def search(

        self,

        query,

        k=5,

        metric="cosine",

        algorithm="hnsw"

    ):

        dist = get_distance(metric)

        start = time.perf_counter()

        if algorithm == "bruteforce":

            raw = self.bruteforce.knn(

                query,

                k,

                dist

            )

        elif algorithm == "kdtree":

            raw = self.kdtree.knn(

                query,

                k

            )

        else:

            raw = self.hnsw.knn(

                query,

                k

            )

        latency = (

            time.perf_counter()

            - start

        ) * 1000000

        results = []

        for distance, item_id in raw:

            if item_id in self.store:

                item = self.store[item_id]

                results.append({

                    "id": item.id,

                    "metadata": item.metadata,

                    "category": item.category,

                    "embedding": item.emb,

                    "distance": distance

                })

        return {

            "results": results,

            "latency_us": int(latency),

            "algorithm": algorithm,

            "metric": metric

        }
    def size(self):

        return len(self.store)

    def all(self):

        return list(

            self.store.values()

        )

    def hnsw_info(self):

        return self.hnsw.get_info()