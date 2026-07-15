import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from algorithms.distance import Distance
from models.vector import Vector

v1 = Vector(
    1,
    [1, 2, 3]
)

v2 = Vector(
    2,
    [4, 5, 6]
)

print("Euclidean:", Distance.euclidean(v1, v2))
print("Cosine:", Distance.cosine(v1, v2))
print("Manhattan:", Distance.manhattan(v1, v2))