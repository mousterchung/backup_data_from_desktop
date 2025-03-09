import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations

def midpoint(p1, p2):
    return (p1 + p2) / 2

def circle_points(center, radius, num_points=100):
    theta = np.linspace(0, 2 * np.pi, num_points)
    return center[0] + radius * np.cos(theta), center[1] + radius * np.sin(theta)

def distance(p1, p2):
    return np.sqrt(np.sum((p1 - p2) ** 2))

def is_square(p1, p2, p3, p4):
    dists = [distance(p1, p2), distance(p1, p3), distance(p1, p4),
             distance(p2, p3), distance(p2, p4), distance(p3, p4)]
    dists.sort()
    return dists[0] == dists[1] and dists[2] == dists[3] and dists[4] == dists[5] and dists[0]**2 + dists[2]**2 == dists[4]**2

def find_squares(points):
    squares = []
    for p1, p2, p3, p4 in permutations(points):
        if is_square(p1, p2, p3, p4):
            squares.append((p1, p2, p3, p4))
    return squares

# 定義四邊形的四個點
A = np.array([0, 0])
B = np.array([2, 0])
C = np.array([2, 2])
D = np.array([0, 2])

# 計算每條邊的中點和半徑
mid_AB = midpoint(A, B)
mid_BC = midpoint(B, C)
mid_CD = midpoint(C, D)
mid_DA = midpoint(D, A)

r_AB = distance(A, B) / 2
r_BC = distance(B, C) / 2
r_CD = distance(C, D) / 2
r_DA = distance(D, A) / 2

# 計算圓上的點
circle_AB = circle_points(mid_AB, r_AB)
circle_BC = circle_points(mid_BC, r_BC)
circle_CD = circle_points(mid_CD, r_CD)
circle_DA = circle_points(mid_DA, r_DA)

# 將圓上的點合併成一個列表
points = []
for i in range(len(circle_AB[0])):
    points.append(np.array([circle_AB[0][i], circle_AB[1][i]]))
for i in range(len(circle_BC[0])):
    points.append(np.array([circle_BC[0][i], circle_BC[1][i]]))
for i in range(len(circle_CD[0])):
    points.append(np.array([circle_CD[0][i], circle_CD[1][i]]))
for i in range(len(circle_DA[0])):
    points.append(np.array([circle_DA[0][i], circle_DA[1][i]]))

# 找出正方形
squares = find_squares(points)

# 繪圖
plt.figure(figsize=(8, 8))
plt.plot(A[0], A[1], 'ro')
plt.plot(B[0], B[1], 'ro')
plt.plot(C[0], C[1], 'ro')
plt.plot(D[0], D[1], 'ro')

# 畫圓
plt.plot(circle_AB[0], circle_AB[1], 'b')
plt.plot(circle_BC[0], circle_BC[1], 'b')
plt.plot(circle_CD[0], circle_CD[1], 'b')
plt.plot(circle_DA[0], circle_DA[1], 'b')

# 畫正方形
for square in squares:
    plt.plot(*zip(*square), 'g-')

plt.axis('equal')
plt.grid()
plt.show()