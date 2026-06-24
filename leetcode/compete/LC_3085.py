def minDeletionsToMakeSpecialString(word, k):
    from collections import Counter

    # 统计每个字符的频率
    freq = Counter(word)
    freq_values = sorted(freq.values())

    min_deletions = float('inf')  # 初始化最小删除次数为无穷大

    # 遍历每个频率值作为基准
    for i in range(len(freq_values)):
        deletions = 0
        base_freq = freq_values[i]

        # 计算以当前频率作为最低频率时需要的删除次数
        for f in freq_values:
            if f < base_freq:
                deletions += f  # 完全删除低于基准的频率
            elif f > base_freq + k:
                deletions += f - (base_freq + k)  # 减少高于基准+k的频率

        # 更新最小删除次数
        min_deletions = min(min_deletions, deletions)

    return min_deletions

# 测试示例
example1 = ("aabcaba", 0)
example2 = ("dabdcbdcdcd", 2)
example3 = ("aaabaaa", 2)

# 运行测试
example1_result = minDeletionsToMakeSpecialString(*example1)  # 期望输出：3
example2_result = minDeletionsToMakeSpecialString(*example2)  # 期望输出：2
example3_result = minDeletionsToMakeSpecialString(*example3)  # 期望输出：1

print(example1_result)
print(example2_result)
print(example3_result)
