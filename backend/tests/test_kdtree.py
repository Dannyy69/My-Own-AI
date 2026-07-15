import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from algorithms.kdtree import KDTree
from models.vector import Vector

tree = KDTree()

vectors = [

    Vector(1, [1, 2]),

    Vector(2, [4, 5]),

    Vector(3, [7, 3]),

    Vector(4, [2, 8]),

    Vector(5, [9, 1]),

]

tree.build(vectors)

print()

print("Nodes:")

print(tree.count())

print()

query = Vector(
    0,
    [2, 3]
)

results = tree.nearest(
    query,
    3
)

for distance, vector in results:

    print(
        vector.id,
        distance
    )