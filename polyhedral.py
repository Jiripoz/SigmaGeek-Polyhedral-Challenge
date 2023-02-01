import numpy as np
import itertools


def check_tetrahedron(pA, pB, pC, pD):
    # Defining a plane equation from 3 points
    vector_m = np.array(pB) - np.array(pA)
    vector_n = np.array(pC) - np.array(pA)
    normal = np.cross(vector_m, vector_n)
    const = np.dot(pA, normal)
    # print(f"The plane equation is {normal[0]}x + {normal[1]}y + {normal[2]}z = {const}")
    # Verifying coplanarity
    if np.dot(pD, normal) != const:
        return True
    return False


# Generic points of regular octahedron https://www.math.brown.edu/tbanchof/Beyond3d/chapter8/section05.html
vertices = [
    ([0, 0, 1]),  # A 0
    ([0, 1, 0]),  # B 1
    ([1, 0, 0]),  # C 2
    ([0, 0, -1]),  # D 3
    ([0, -1, 0]),  # E 4
    ([-1, 0, 0]),  # F 5
]
center_points = [
    list(
        np.average(
            (np.array(vertices[0]), np.array(vertices[1]), np.array(vertices[2])),
            axis=0,
        )
    ),
    list(
        np.average(
            (np.array(vertices[0]), np.array(vertices[1]), np.array(vertices[5])),
            axis=0,
        )
    ),
    list(
        np.average(
            (np.array(vertices[0]), np.array(vertices[4]), np.array(vertices[2])),
            axis=0,
        )
    ),
    list(
        np.average(
            (np.array(vertices[0]), np.array(vertices[4]), np.array(vertices[5])),
            axis=0,
        )
    ),
    list(
        np.average(
            (np.array(vertices[3]), np.array(vertices[1]), np.array(vertices[2])),
            axis=0,
        )
    ),
    list(
        np.average(
            (np.array(vertices[3]), np.array(vertices[1]), np.array(vertices[5])),
            axis=0,
        )
    ),
    list(
        np.average(
            (np.array(vertices[3]), np.array(vertices[4]), np.array(vertices[2])),
            axis=0,
        )
    ),
    list(
        np.average(
            (np.array(vertices[3]), np.array(vertices[4]), np.array(vertices[5])),
            axis=0,
        )
    ),
]

total = np.concatenate(
    ([np.array(x) for x in vertices], [np.array(y) for y in center_points]), axis=0
)
clean_total = [tuple(list(x)) for x in total]

iterations = 0
unq = list(itertools.combinations((clean_total), 4))

tetrahedron_list = []
for item in unq:
    if check_tetrahedron(item[0], item[1], item[2], item[3]):
        tetrahedron_list.append(item)

print(f"The answer is {len(tetrahedron_list)}")
