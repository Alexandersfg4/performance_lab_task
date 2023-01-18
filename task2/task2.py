import sys


def find_point(x, y, circle_x, circle_y, circle_r):
    # x ^ 2 + y ^ 2 <= R ^ 2
    action = (x - circle_x) ** 2 + (y - circle_y) ** 2
    circle_r_square = circle_r ** 2
    if action == circle_r_square:
        return 0
    elif action < circle_r_square:
        return 1
    else:
        return 2


if __name__ == "__main__":
    center_file = sys.argv[1]
    points_file = sys.argv[2]
    with open(center_file, "r") as f:
        circle_points = f.readline()
        circle_radius = f.readline()
    circle_x_point, circle_y_point = circle_points.split()
    with open(points_file, "r") as f:
        points = f.readlines()
    for point in points:
        point_x, point_y = point.split()
        result = find_point(float(point_x), float(point_y), float(circle_x_point),
                            float(circle_y_point), int(circle_radius))
        print(result)
