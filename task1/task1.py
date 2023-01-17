import itertools
import sys


def find_path(n, m):
    int_n = int(n)
    int_m = int(m)
    point = 0
    path = []
    for i, value in enumerate(itertools.cycle(range(1, int_n + 1))):
        if i == point:
            if i != 0 and value == path[0]:
                break
            path.append(value)
            point += int_m - 1
        elif i > 20:
            break
        else:
            continue
    return path


if __name__ == "__main__":
    result = find_path(sys.argv[1], sys.argv[2])
    str_result = map(str, result)
    print(''.join(str_result))
