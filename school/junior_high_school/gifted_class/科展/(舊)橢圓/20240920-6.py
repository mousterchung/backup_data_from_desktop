import numpy as np
import matplotlib.pyplot as plt

def draw_circle(ax, center, diameter):
    radius = diameter / 2
    circle = plt.Circle(center, radius, fill=False, color='blue', linestyle='--')
    ax.add_artist(circle)

def calculate_midpoint(p1, p2):
    return (p1 + p2) / 2

def generate_squares(points, num_samples=100):
    squares = []
    for i in range(len(points)):
        p1 = points[i]
        p2 = points[(i + 1) % len(points)]
        mid = calculate_midpoint(p1, p2)
        diameter = np.linalg.norm(p2 - p1)
        radius = diameter / 2

        for _ in range(num_samples):
            # 在圆上随机取一点
            angle = np.random.uniform(0, 2 * np.pi)
            circle_point = mid + radius * np.array([np.cos(angle), np.sin(angle)])

            # 生成与圆形有交点的正方形
            half_side = radius * np.sqrt(2) / 2
            square = np.array([
                circle_point + np.array([half_side, half_side]),
                circle_point + np.array([-half_side, half_side]),
                circle_point + np.array([-half_side, -half_side]),
                circle_point + np.array([half_side, -half_side])
            ])
            squares.append(square)

    return squares

def main():
    # 用户输入四边形的四个点
    points = []
    print("请输入四边形的四个点（格式: x,y），输入 'done' 完成：")
    while len(points) < 4:
        inp = input(f"点 {len(points) + 1}: ")
        if inp.lower() == 'done':
            break
        try:
            x, y = map(float, inp.split(','))
            points.append(np.array([x, y]))
        except ValueError:
            print("输入格式错误，请使用 'x,y' 的格式。")

    points = np.array(points)

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

    ax.set_xlim(min(points[:, 0]) - 1, max(points[:, 0]) + 1)
    ax.set_ylim(min(points[:, 1]) - 1, max(points[:, 1]) + 1)
    ax.set_aspect('equal', adjustable='box')
    plt.grid()
    plt.title("Squares Generated from Circles on Edges")
    plt.show()

if __name__ == "__main__":
    main()