# 手动输入数据
L = 72.50
H = 70.05
d = 0.013
D = 3.50
k = 0.05

# 计算表达式
import math

E = 9.8 *8 * L * H * k / (math.pi * d ** 2 * D )

# 输出结果
print(f"E 的结果为: {E}")