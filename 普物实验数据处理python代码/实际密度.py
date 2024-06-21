def calculate_operations(array, M, rho):
    result = [(1 / num) * M * rho for num in array]
    return result

# 示例数组
#input_array = [0.565]
#input_array = [0.4399999999999977, 0.6599999999999682, 0.5699999999999932, 0.5400000000000205, 0.5699999999999932, 0.6100000000000136]
#input_array = [0.258]
#input_array = [0.2599999999999909, 0.25, 0.25, 0.2699999999999818, 0.26000000000004775, 0.2599999999999909]
#input_array = [0.255]
input_array = [0.25, 0.25, 0.2599999999999909, 0.2599999999999909, 0.25, 0.26000000000004775]

# 设置 M 和 ρ 的值
#M_value = 3.19
#M_value = 1.05
M_value = 0.88
rho_value = 1

# 计算结果
output_result = calculate_operations(input_array, M_value, rho_value)

# 格式化输出结果，保留三位小数
formatted_result = [round(num, 3) for num in output_result]

# 输出结果
print("原始数组:", input_array)
print("密度", formatted_result)
