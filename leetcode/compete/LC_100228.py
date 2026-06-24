import math
from cmath import inf


class Solution:
    def minOperations(self, k: int) -> int:
        if k == 1:
            return 0
        minOperations = inf

        for count_add in range(0, k - 1):
            count_duplicate = math.ceil(k / (1 + count_add)) - 1

            minOperations = min(minOperations, count_add + count_duplicate)

        return minOperations


def minOperations(k):
    # 如果k小于等于1，不需要任何操作
    if k <= 1:
        return 0

    # 二分搜索寻找最少的操作次数
    left, right = 1, k
    while left < right:
        mid = (left + right) // 2
        if (mid * (mid + 1)) // 2 < k:  # 判断增加到mid需要的操作次数是否足够
            left = mid + 1
        else:
            right = mid

    steps = 0
    while k > 0:
        if k >= left:
            k -= left
            steps += 1
        else:
            left -= 1
    return steps


# 使用示例输入运行检验
print(minOperations(11))  # 示例 1
print(minOperations(1))  # 示例 2

print(Solution().minOperations(11))