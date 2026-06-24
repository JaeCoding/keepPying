def calculate_counters_optimized(arr):
    n = len(arr)
    if n <= 1:
        return [0] * n

    # 初始化结果数组和前缀和数组
    result = [0] * n
    prefix_sum = [0] * (n + 1)

    # 计算前缀和
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

    # 计算每个元素的计数器值
    for i in range(n):
        result[i] = (i + 1) * arr[i] - prefix_sum[i + 1]

    return result


# 测试示例
arr = [2, 4, 3]
print(calculate_counters_optimized(arr))
