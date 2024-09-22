import numpy as np
import matplotlib.pyplot as plt

def midpoint(p1, p2):
    return (p1 + p2) / 2

def distance(p1, p2):
    return np.linalg.norm(p1 - p2)

def circle_points(center, radius, num_points=100):
    angles = np.linspace(0, 2 * np.pi, num_points)
    return center[0] + radius * np.cos(angles), center[1] + radius * np.sin(angles)

def is_square(points):
    dists = [distance(points[i], points[j]) for i in range(4) for j in range(i + 1, 4)]
    dists.sort()
    return dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5]

def generate_square_points(c1, c2, c3, c4, r1, r2, r3, r4):
    squares = []
    points1 = circle_points(c1, r1)
    points2 = circle_points(c2, r2)
    points3 = circle_points(c3, r3)
    points4 = circle_points(c4, r4)

    for p1 in zip(*points1):
        for p2 in zip(*points2):
            for p3 in zip(*points3):
                for p4 in zip(*points4):
                    square = np.array([p1, p2, p3, p4])
                    if is_square(square):
                        squares.append(square)
    return squares

# 輸入四邊形的四個頂點
A = np.array([0, 0])
B = np.array([4, 0])
C = np.array([4, 3])
D = np.array([0, 3])

# 計算中點和半徑
M_AB = midpoint(A, B)
M_BC = midpoint(B, C)
M_CD = midpoint(C, D)
M_DA = midpoint(D, A)

r_AB = distance(A, B) / 2
r_BC = distance(B, C) / 2
r_CD = distance(C, D) / 2
r_DA = distance(D, A) / 2

# 從圓周上的點生成正方形
squares = generate_square_points(M_AB, M_BC, M_CD, M_DA, r_AB, r_BC, r_CD, r_DA)

# 可視化
plt.figure(figsize=(8, 8))
plt.plot([A[0], B[0]], [A[1], B[1]], 'b-')
plt.plot([B[0], C[0]], [B[1], C[1]], 'b-')
plt.plot([C[0], D[0]], [C[1], D[1]], 'b-')
plt.plot([D[0], A[0]], [D[1], A[1]], 'b-')

# 繪製圓
circle1_x, circle1_y = circle_points(M_AB, r_AB)
circle2_x, circle2_y = circle_points(M_BC, r_BC)
circle3_x, circle3_y = circle_points(M_CD, r_CD)
circle4_x, circle4_y = circle_points(M_DA, r_DA)

plt.plot(circle1_x, circle1_y, 'r-', label='Circle AB')
plt.plot(circle2_x, circle2_y, 'g-', label='Circle BC')
plt.plot(circle3_x, circle3_y, 'm-', label='Circle CD')
plt.plot(circle4_x, circle4_y, 'c-', label='Circle DA')

# 繪製正方形
for square in squares:
    square = np.array(square)
    plt.plot(np.append(square[:, 0], square[0, 0]), np.append(square[:, 1], square[0, 1]), 'k-')

plt.axis('equal')
plt.title("Squares with Vertices on Different Circles")
plt.legend()
plt.grid()
plt.show()

print(f"Found {len(squares)} squares.")