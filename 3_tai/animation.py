import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- データ読み込み ---
data = np.loadtxt("result.dat")
times = data[:, 0]
positions = data[:, 1:]  # x1 y1 x2 y2 x3 y3

# 0.1秒ごとのインデックスを取得
dt = times[1] - times[0]
interval_step = int(0.1 / dt + 0.5)  # 四捨五入
selected_indices = np.arange(0, len(times), interval_step)


# --- アニメーション描画 ---
fig, ax = plt.subplots()
sc = ax.scatter([], [], s=40)
ax.set_xlim(-2.5, 3.0)
ax.set_ylim(-2.5, 3.0)
ax.grid()
ax.set_aspect('equal')
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

def update(frame):
    i = selected_indices[frame]
    x = positions[i, 0::2]
    y = positions[i, 1::2]
    sc.set_offsets(np.c_[x, y])
    time_text.set_text(f"t = {times[i]:.2f} s")
    return sc, time_text

ani = FuncAnimation(fig, update, frames=len(selected_indices), interval=100, blit=True)
ani.save('three_body.gif', writer='ffmpeg', fps=10)

print("保存完了：three_body.gif")

# plt.show() 注: ani.save は ffmpegのインストールが必要
