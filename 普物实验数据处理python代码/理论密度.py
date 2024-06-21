import math

def calculate_density_and_volume(ball_diameters, M):
    # 将球直径转换为半径（单位：cm）
    radii = [(diameter+0.003) / 20 for diameter in ball_diameters]

    # 计算每个球的体积和密度
    volumes = [(4/3) * math.pi * math.pow(radius, 3) for radius in radii]
    densities = [M / volume for volume in volumes]

    return densities, volumes

# 输入小球直径数组和 M 值
# ball_diameters = [10.486, 10.488, 10.490,10.489,10.488,10.490]  # 例如，这里是三个小球的直径
#ball_diameters = [7.925, 7.921, 7.923,7.922,7.923,7.920]  # 例如，这里是三个小球的直径
ball_diameters = [7.928, 7.932, 7.929,7.928,7.927,7.928]  # 例如，这里是三个小球的直径
# M = 3.19  # 例如，这里是 M 的值
#M = 1.05  # 例如，这里是 M 的值
M = 0.88  # 例如，这里是 M 的值

# 计算每个小球的密度和体积
result_densities, result_volumes = calculate_density_and_volume(ball_diameters, M)

# 输出结果（保留三位小数）
for i, (density, volume) in enumerate(zip(result_densities, result_volumes)):
    print(f"第{i+1}个小球的密度为: {round(density, 3)} g/cm^3，体积为: {round(volume, 3)} cm^3")

formatted_densities = [round(density, 3) for density in result_densities]
formatted_volumes = [round(volume, 3) for volume in result_volumes]

print("小球体积:", formatted_volumes)
print("小球密度:", formatted_densities)