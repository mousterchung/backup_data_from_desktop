import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations

# 定義四邊形的四個點
A, B, C, D = np.array([0, 0]), np.array([2, 0]), np.array([2, 2]), np.array([0, 2])

# 計算中點和圓的點
midpoints = [(A + B) / 2, (B + C) / 2, (C + D) / 2, (D + A) / 2]
radii = [np.linalg.norm(B - A) / 2] * 4  # 假設每條邊長相同

# 生成圓的點
points = [mid + r * np.array([np.cos(theta), np.sin(theta)]) for mid, r in zip(midpoints, radii) for theta in np.linspace(0, 2 * np.pi, 100)]

# 檢查正方形
def is_square(p1, p2, p3, p4):
    dists = sorted([np.linalg.norm(p1 - p2), np.linalg.norm(p1 - p3), np.linalg.norm(p1 - p4),
                    np.linalg.norm(p2 - p3), np.linalg.norm(p2 - p4), np.linalg.norm(p3 - p4)])
    return dists[0] == dists[1] and dists[2] == dists[3] and dists[0]**2 + dists[2]**2 == dists[4]**2

squares = [combo for combo in permutations(np.vstack(points).T, 4) if is_square(*combo)]

# 繪圖
plt.figure(figsize=(8, 8))
plt.plot(*zip(A, B, C, D), 'ro')
for mid in midpoints:
    plt.gca().add_artist(plt.Circle(mid, radii[0], fill=False))
for square in squares:
    plt.plot(*zip(*square), 'g-')
plt.axis('equal')
plt.grid()
plt.show()