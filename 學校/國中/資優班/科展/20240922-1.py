# 計算每條邊的中點和對應的圓半徑（邊的長度的一半）
midpoints = [(A + B) / 2, (B + C) / 2, (C + D) / 2, (D + A) / 2]
radii = [np.linalg.norm(B - A) / 2, np.linalg.norm(C - B) / 2, np.linalg.norm(D - C) / 2, np.linalg.norm(A - D) / 2]

# 在每個中點周圍生成圓上的點
points = []
for mid, r in zip(midpoints, radii):
    theta = np.linspace(0, 2 * np.pi, 20)  # 減少點數來提高效能
    circle_points = mid + r * np.array([np.cos(theta), np.sin(theta)]).T
    points.extend(circle_points)

# 檢查四個點是否構成正方形
def is_square(p1, p2, p3, p4):
    dists = sorted([np.linalg.norm(p1 - p2), np.linalg.norm(p1 - p3), np.linalg.norm(p1 - p4),
                    np.linalg.norm(p2 - p3), np.linalg.norm(p2 - p4), np.linalg.norm(p3 - p4)])
    return dists[0] == dists[1] and dists[2] == dists[3] and np.isclose(dists[0]**2 + dists[2]**2, dists[4]**2)

# 從點中找出正方形
squares = []
for combo in combinations(points, 4):  # 檢查 4 個點的組合
    if is_square(*combo):
        squares.append(combo)