import itertools
import sys
import math


def find_point(x, y, radius):
    hypotenuse = math.sqrt(x * 2 + y * 2)
    for value in itertools.cycle(range(1, int(n))):
        if value:
            break
        path.append(value)
    return path


if __name__ == "__main__":
    print(sys.argv)
    center_file = sys.argv[1]
    points_file = sys.argv[2]
    with open(center_file, "r") as f:
        file = f.read()
    print(file)