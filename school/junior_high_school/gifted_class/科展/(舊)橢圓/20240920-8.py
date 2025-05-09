import numpy as np
import matplotlib.pyplot as plt
import itertools

def get_midpoint(p1, p2):
    return (p1 + p2) / 2

def get_circle_points(center, radius, num_points=100):
    angles = np.linspace(0, 2 * np.pi, num_points)
    return center[0] + radius * np.cos(angles), center[1] + radius * np.sin(angles)

def generate_points_on_circle(center, radius, num_points=10):
    points = []
    for _ in range(num_points):
        angle = np.random.uniform(0, 2 * np.pi)
        points.append((center[0] + radius * np.cos(angle), center[1] + radius * np.sin(angle)))
    return points

def is_square(points):
    if len(points) != 4:
        return False
    dists = [np.linalg.norm(np.array(points[i]) - np.array(points[j])) for i in range(4) for j in range(i + 1, 4)]
    dists = sorted(dists)
    return (dists[0] == dists[1] == dists[2] == dists[3] and 
            dists[4] == dists[5] and 
            dists[0] * np.sqrt(2) == dists[4])

def main():
    # 输入四个点
    points = [tuple(map(float, input(f"Enter coordinates for point {i + 1} (x, y): ").split())) for i in range(4)]
    
    midpoints = []
    circles = []

    # 计算中点和半径
    for i in range(4):
        p1 = np.array(points[i])
        p2 = np.array(points[(i + 1) % 4])
        midpoint = get_midpoint(p1, p2)
        midpoints.append(midpoint)
        length = np.linalg.norm(p2 - p1)
        radius = length / 2
        circles.append((midpoint, radius))

    # 在每个圆上生成随机点
    random_points = []
    for midpoint, radius in circles:
        points_on_circle = generate_points_on_circle(midpoint, radius)
        random_points.append(points_on_circle)

    possible_squares = []

    # 检查所有点的组合
    for combination in itertools.product(*random_points):
        if is_square(combination):
            possible_squares.append(combination)

    # 输出所有可能的正方形
    print("Possible squares:")
    for square in possible_squares:
        print(square)

    # 可视化
    plt.figure()
    for midpoint, radius in circles:
        circle = plt.Circle(midpoint, radius, color='b', fill=False)
        plt.gca().add_artist(circle)

    for square in possible_squares:
        square = np.array(square)
        plt.fill(square[:, 0], square[:, 1], alpha=0.3)

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()