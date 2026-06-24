def mark_elements(nums, queries):
    marked = [False] * len(nums)  # 标记数组初始化
    answer = []  # 结果数组

    for index, k in queries:
        if index < len(nums):  # 防止index越界
            marked[index] = True  # 标记指定元素

        # 创建(值, 索引)对的列表，仅包含未标记元素
        unmarked_elements = [(val, i) for i, val in enumerate(nums) if not marked[i]]
        unmarked_elements.sort()  # 根据值排序，确保优先标记最小元素

        # 标记ki个最小的未标记元素
        for i in range(min(k, len(unmarked_elements))):
            _, idx = unmarked_elements[i]
            marked[idx] = True

        # 计算未标记元素的总和
        sum_unmarked = sum(nums[i] for i in range(len(nums)) if not marked[i])
        answer.append(sum_unmarked)

    return answer

# 测试代码
nums = [1,2,2,1,2,3,1]
queries = [[1,2],[3,3],[4,2]]
print(mark_elements(nums, queries))
