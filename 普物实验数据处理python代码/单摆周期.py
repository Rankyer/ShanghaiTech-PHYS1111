import matplotlib.pyplot as plt
import numpy as np

# 数据
T = [2.655, 2.786, 2.924, 3.069, 3.200]
L = [45, 50, 55, 60, 65]
T_squared = [(t / 2) ** 2 for t in T]

# 绘制表格
fig, ax = plt.subplots()
table_data = [
    ["", "1", "2", "3", "4", "5"],
    ["2T", 2.655, 2.786, 2.924, 3.069, 3.200],
    ["T^2", f"{T_squared[0]:.4f}", f"{T_squared[1]:.4f}", f"{T_squared[2]:.4f}", f"{T_squared[3]:.4f}", f"{T_squared[4]:.4f}"],
    ["L", 45, 50, 55, 60, 65],
]
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=table_data, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(14)
table.scale(1, 1.5)

# 绘制T^2和L的图像
plt.figure()
plt.scatter(L, T_squared, c='black', s=60, label='Data Points (Highlighted)')
coefficients = np.polyfit(L, T_squared, 1)
polynomial = np.poly1d(coefficients)
plt.plot(L, polynomial(L), linestyle='--', label=f'Fit Line: {coefficients[0]:.4f}L + {coefficients[1]:.4f}')
plt.xlabel("L")
plt.ylabel("T^2")
plt.legend()
plt.title(f'Linear Fit: T^2 = {coefficients[0]:.4f}L + {coefficients[1]:.4f}')
plt.grid(True)

plt.show()
