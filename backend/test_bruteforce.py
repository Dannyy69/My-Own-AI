from algorithms.bruteforce import BruteForceIndex
from models.vector import Vector

db = BruteForceIndex()

db.insert(
    Vector(
        1,
        [1, 2, 3]
    )
)

db.insert(
    Vector(
        2,
        [3, 5, 1]
    )
)

db.insert(
    Vector(
        3,
        [2, 1, 0]
    )
)

results = db.search(
    [1, 2, 3],
    2
)

for score, vector in results:
    print(vector.id, score)