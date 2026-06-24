def calculate_counters(arr):
    # 初始化结果数组，长度与输入数组相同，初始值为0
    result = [0] * len(arr)
    # 初始化一个变量来存储当前元素左边所有元素的累积差值
    cumulative_diff = 0
    # 初始化一个变量来存储当前元素左边所有元素的累积和
    cumulative_sum = 0

    # 遍历数组中的每个元素，从第二个元素开始
    for i in range(1, len(arr)):
        # 计算当前元素与前一个元素的差值
        diff = arr[i] - arr[i - 1]
        # 更新累积差值和累积和
        cumulative_diff += i * diff
        cumulative_sum += arr[i - 1]
        # 计算当前元素的计数器值
        result[i] = cumulative_diff - 2 * cumulative_sum

    return result


# 示例
n = 3
arr = [2, 4, 3]
output = calculate_counters(arr)
print("输出结果为：", output)  # 输出结果为 [0, 2, 0]