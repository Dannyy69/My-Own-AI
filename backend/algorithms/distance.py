import math


def euclidean(a, b):

    return math.sqrt(

        sum(

            (x - y) ** 2

            for x, y

            in zip(a, b)

        )

    )


def cosine(a, b):

    dot = sum(

        x * y

        for x, y

        in zip(a, b)

    )

    mag_a = math.sqrt(

        sum(

            x * x

            for x in a

        )

    )

    mag_b = math.sqrt(

        sum(

            y * y

            for y in b

        )

    )

    if mag_a == 0 or mag_b == 0:

        return 1.0

    return 1.0 - dot / (

        mag_a * mag_b

    )


def manhattan(a, b):

    return sum(

        abs(x - y)

        for x, y

        in zip(a, b)

    )


def get_distance(metric):

    metric = metric.lower()

    if metric == "euclidean":

        return euclidean

    if metric == "manhattan":

        return manhattan

    return cosine