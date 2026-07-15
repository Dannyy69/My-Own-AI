from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List

from models.vector import VectorItem
from algorithms.distance import cosine


@dataclass
class KDNode:
    vector: VectorItem
    axis: int
    left: Optional["KDNode"] = None
    right: Optional["KDNode"] = None


class KDTree:

    def __init__(self):
        self.root = None
        self.dimension = None

    def build(self, vectors: List[VectorItem]):

        if not vectors:
            return

        self.dimension = len(vectors[0].emb)

        self.root = self._build(vectors, 0)

    def _build(self, vectors, depth):

        if not vectors:
            return None

        axis = depth % self.dimension

        vectors.sort(
            key=lambda v: v.emb[axis]
        )

        median = len(vectors) // 2

        node = KDNode(
            vectors[median],
            axis
        )

        node.left = self._build(
            vectors[:median],
            depth + 1
        )

        node.right = self._build(
            vectors[median + 1:],
            depth + 1
        )

        return node

    def insert(self, vector: VectorItem):

        if self.root is None:

            self.dimension = len(vector.emb)

            self.root = KDNode(vector, 0)

            return

        self._insert(self.root, vector, 0)

    def _insert(self, node, vector, depth):

        axis = depth % self.dimension

        if vector.emb[axis] < node.vector.emb[axis]:

            if node.left is None:

                node.left = KDNode(
                    vector,
                    (depth + 1) % self.dimension
                )

            else:

                self._insert(
                    node.left,
                    vector,
                    depth + 1
                )

        else:

            if node.right is None:

                node.right = KDNode(
                    vector,
                    (depth + 1) % self.dimension
                )

            else:

                self._insert(
                    node.right,
                    vector,
                    depth + 1
                )

    def knn(self, query, k=5):

        best = []

        self._nearest(
            self.root,
            query,
            k,
            best
        )

        best.sort(
            key=lambda x: x[0]
        )

        return [
            (distance, vector.id)
            for distance, vector in best
        ]

    def _nearest(
        self,
        node,
        query,
        k,
        best
    ):

        if node is None:
            return

        distance = cosine(
            query,
            node.vector.emb
        )

        best.append(
            (
                distance,
                node.vector
            )
        )

        best.sort(
            key=lambda x: x[0]
        )

        if len(best) > k:
            best.pop()

        axis = node.axis

        diff = (
            query[axis]
            -
            node.vector.emb[axis]
        )

        near = node.left if diff < 0 else node.right
        far = node.right if diff < 0 else node.left

        self._nearest(
            near,
            query,
            k,
            best
        )

        if (
            len(best) < k
            or
            abs(diff) < best[-1][0]
        ):

            self._nearest(
                far,
                query,
                k,
                best
            )

    def clear(self):
        self.root = None

    def empty(self):
        return self.root is None

    def count(self):

        def dfs(node):

            if node is None:
                return 0

            return (
                1
                + dfs(node.left)
                + dfs(node.right)
            )

        return dfs(self.root)