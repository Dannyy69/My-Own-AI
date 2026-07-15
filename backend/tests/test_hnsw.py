import os
import sys

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from algorithms.hnsw import HNSW
from models.vector import VectorItem

index = HNSW()

for i in range(20):

    index.insert(

        VectorItem(

            id=i,

            metadata=f"Item {i}",

            category="test",

            emb=[

                float(i),

                float(i + 1),

                float(i + 2)

            ]

        )

    )

print("Nodes:", index.size())
print("Entry:", index.entry_point)
print("Top Layer:", index.top_layer)