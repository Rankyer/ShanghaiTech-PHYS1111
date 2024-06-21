# 获取输入数据的组数
num_pairs = int(input("请输入数据的组数："))

# 循环获取每组数据并计算平均值
for i in range(num_pairs):
    # 获取每组数据
    data = input(f"请输入第 {i + 1} 组数据，用空格分隔：")
    values = data.split()  # 将输入的数据以空格分割成列表

    # 检查输入数据是否为两个
    if len(values) != 2:
        print("每组数据应该有两个数字，请重新输入。")
        continue

    # 将输入数据转换为浮点数并计算平均值
    num1, num2 = map(float, values)
    average = (num1 + num2) / 2

    print(f"第 {i + 1} 组数据的平均值为: {average}")
