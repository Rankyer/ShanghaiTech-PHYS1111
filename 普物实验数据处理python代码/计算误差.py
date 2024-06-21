actual_value = 642.434
predicted_value = 640

# 计算相对误差
relative_error = (abs(actual_value - predicted_value) / actual_value) * 100

print(f"实际值: {actual_value}")
print(f"预测值: {predicted_value}")
print(f"相对误差: {relative_error}%")