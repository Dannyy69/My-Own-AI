import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from database.vector_db import VectorDB

db = VectorDB(3)

db.insert(

    "Linked List",

    "cs",

    [1,2,3]

)

db.insert(

    "Binary Tree",

    "cs",

    [4,5,6]

)

db.insert(

    "Pizza",

    "food",

    [8,1,2]

)

print()

print(db.size())

print()

print(

    db.search(

        [1,2,3],

        2,

        "cosine",

        "bruteforce"

    )

)