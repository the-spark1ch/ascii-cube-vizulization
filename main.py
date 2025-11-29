import math
import time
import os

width = 60
height = 30
sleep_time = 0.05

vertices = [
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1],
]

edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

def rotate(vertex, angle_x, angle_y):
    x, y, z = vertex
    y, z = y*math.cos(angle_x) - z*math.sin(angle_x), y*math.sin(angle_x) + z*math.cos(angle_x)
    x, z = x*math.cos(angle_y) + z*math.sin(angle_y), -x*math.sin(angle_y) + z*math.cos(angle_y)
    return [x, y, z]

def project(vertex):
    x, y, z = vertex
    factor = 7 / (z + 10)
    x = int(width/2 + factor*x*width/2)
    y = int(height/2 - factor*y*height/2)
    return x, y

def render(vertices):
    screen = [[" "]*width for _ in range(height)]
    for edge in edges:
        x1, y1 = project(vertices[edge[0]])
        x2, y2 = project(vertices[edge[1]])
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))
        if steps == 0:
            if 0 <= x1 < width and 0 <= y1 < height:
                screen[y1][x1] = "#"
            continue
        for i in range(steps+1):
            xi = int(x1 + dx*i/steps)
            yi = int(y1 + dy*i/steps)
            if 0 <= xi < width and 0 <= yi < height:
                screen[yi][xi] = "#"
    print("\n".join("".join(row) for row in screen))
angle_x = 0
angle_y = 0

try:
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        rotated_vertices = [rotate(v, angle_x, angle_y) for v in vertices]
        render(rotated_vertices)
        angle_x += 0.05
        angle_y += 0.03
        time.sleep(sleep_time)
except KeyboardInterrupt:
    pass
