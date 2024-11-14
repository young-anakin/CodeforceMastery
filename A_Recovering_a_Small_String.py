def find_square_area(points):
    points.sort(key=lambda p: (p[0], p[1]))
    corner1, corner2 = points[0], points[-1]
    side_length = ((corner2[0] - corner1[0]) ** 2 + (corner2[1] - corner1[1]) ** 2) ** 0.5
    area = side_length ** 2
    return area

t = int(input())
for _ in range(t):
    points = []
    for _ in range(4):
        x, y = map(int, input().split())
        points.append((x, y))
    area = find_square_area(points)
    print(area)
