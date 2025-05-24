import numpy as np
import matplotlib.pyplot as plt

# --- データ読み込み ---
data = np.loadtxt("result.dat")
positions = data[:, 1:]  # x1 y1 x2 y2 x3 y3

# 粒子の数を自動判定
n_particles = positions.shape[1] // 2

# 軌跡を描画
colors = ['red', 'green', 'blue']
labels = [f'Particle {i+1}' for i in range(n_particles)]

plt.figure(figsize=(6, 6))
for i in range(n_particles):
    x = positions[:, 2 * i]
    y = positions[:, 2 * i + 1]
    plt.plot(x, y, color=colors[i % len(colors)], label=labels[i])

plt.xlabel('x')
plt.ylabel('y')
plt.title('Three-body trajectories')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("trajectories.png")  # 結果を画像として保存
plt.show()
