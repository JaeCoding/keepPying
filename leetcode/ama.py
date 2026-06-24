def find_first_discontinuous_index(nums, left, right):
    # 当左右指针相邻时，检查是否连续
    if right - left <= 1:
        # 不连续则返回右
        if nums[right] != nums[left] + 1:
            return left
        else:
            return right

    mid = (left + right) // 2
    # 如果左半边是连续的，递归检查右半边
    if nums[left] + mid - left == nums[mid]:
        return find_first_discontinuous_index(nums, mid, right)
    else:  # 否则，递归检查左半边
        return find_first_discontinuous_index(nums, left, mid)

def compress_ranges(nums):
    result = []
    start = 0

    while start < len(nums):
        # 查找第一个不连续的数的索引
        end = find_first_discontinuous_index(nums, start, len(nums) - 1)
        # 添加到结果
        result.append([nums[start], nums[end]])
        # 移动到下一个子数组的开始
        start = end + 1

    return result

# 测试
print(compress_ranges([1, 2, 3, 4, 7, 8, 10]))
