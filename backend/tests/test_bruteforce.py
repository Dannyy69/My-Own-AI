import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from algorithms.bruteforce import BruteForce
from algorithms.distance import cosine
from models.vector import VectorItem

db = BruteForce()

db.insert(
    VectorItem(
        1,
        "Linked List",
        "cs",
        [1.0, 2.0, 3.0]
    )
)

db.insert(
    VectorItem(
        2,
        "Binary Tree",
        "cs",
        [4.0, 5.0, 6.0]
    )
)

db.insert(
    VectorItem(
        3,
        "Pizza",
        "food",
        [8.0, 1.0, 2.0]
    )
)

results = db.knn(
    [1.0, 2.0, 3.0],
    2,
    cosine
)

print()

for distance, item_id in results:

    print(
        item_id,
        distance
    )

print()

print(
    "Items:",
    db.size()
)