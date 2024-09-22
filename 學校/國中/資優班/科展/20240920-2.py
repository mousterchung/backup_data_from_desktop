import numpy as np
import matplotlib.pyplot as plt

def draw_circle(ax, center, diameter):
    radius = diameter / 2
    circle = plt.Circle(center, radius, fill=False, color='blue', linestyle='--')
    ax.add_artist(circle)

def calculate_midpoint(p1, p2):
    return (p1 + p2) / 2

def generate_squares(points):
    squares = []
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]
        mid = calculate_midpoint(p1, p2)
        diameter = np.linalg.norm(p2 - p1)
        radius = diameter / 2

        # 在圆上取一点
        angle = np.random.uniform(0, 2 * np.pi)
        circle_point = mid + radius * np.array([np.cos(angle), np.sin(angle)])

        # 生成正方形
        square = np.array([
            circle_point,
            circle_point + np.array([radius * np.sqrt(2) / 2, radius * np.sqrt(2) / 2]),
            circle_point + np.array([-radius * np.sqrt(2) / 2, radius * np.sqrt(2) / 2]),
            circle_point + np.array([-radius * np.sqrt(2) / 2, -radius * np.sqrt(2) / 2]),
            circle_point + np.array([radius * np.sqrt(2) / 2, -radius * np.sqrt(2) / 2])
        ])
        squares.append(square)

    return squares

def main():
    # 给定四边形的四个点
    points = np.array([[1, 1], [1, 4], [4, 4], [4, 1]])

    fig, ax = plt.subplots()
    
    # 绘制四边形
    polygon = plt.Polygon(points, fill=None, edgecolor='black')
    ax.add_artist(polygon)

    # 计算并绘制圆
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]
        mid = calculate_midpoint(p1, p2)
        diameter = np.linalg.norm(p2 - p1)
        draw_circle(ax, mid, diameter)

    # 生成所有可能的正方形
    squares = generate_squares(points)

    # 绘制正方形
    for square in squares:
        plt.fill(square[:, 0], square[:, 1], alpha=0.3)

    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.set_aspect('equal', adjustable='box')
    plt.grid()
    plt.title("Squares Generated from Circles on Edges")
    plt.show()

if __name__ == "__main__":
    main()