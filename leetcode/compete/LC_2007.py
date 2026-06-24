from typing import List, Counter

"""
一个整数数组 original 可以转变成一个 双倍 数组 changed ，转变方式为将 original 中每个元素 值乘以 2 加入数组中，然后将所有元素 随机打乱 。

给你一个数组 changed ，如果 change 是 双倍 数组，那么请你返回 original数组，否则请返回空数组。original 的元素可以以 任意 顺序返回。

 

示例 1：

输入：changed = [1,3,4,2,6,8]
输出：[1,3,4]
解释：一个可能的 original 数组为 [1,3,4] :
- 将 1 乘以 2 ，得到 1 * 2 = 2 。
- 将 3 乘以 2 ，得到 3 * 2 = 6 。
- 将 4 乘以 2 ，得到 4 * 2 = 8 。
其他可能的原数组方案为 [4,3,1] 或者 [3,1,4] 。
示例 2：

输入：changed = [6,3,0,1]
输出：[]
解释：changed 不是一个双倍数组。
示例 3：

输入：changed = [1]
输出：[]
解释：changed 不是一个双倍数组。

核心：关键在于统计 出现的频次，然后减少对应x 和 2x的频次

"""
class Solution:
    """
    My failure answer:
    can not pass the condition of [0,0,0,0]
    """
    def findOriginalArray2(self, changed: List[int]) -> List[int]:
        changed.sort()
        ans = []
        double_ans = set()
        for item in changed:
            # Find double element, skip
            if 2 * item in double_ans:
                continue
            # find single element add to ans
            elif item not in double_ans:
                double_ans.add(2 * item)
                ans.append(item)
        return ans if len(double_ans) == len(changed) // 2 else []

    def findOriginalArray(self, changed):
        """
        根据给定的可能的双倍数组，尝试找回原数组。
        如果成功找到，则返回原数组；否则返回空数组。

        :param changed: List[int] 一个可能的双倍数组
        :return: List[int] 原数组或空数组
        """
        if len(changed) % 2 != 0:  # 如果数组长度不是偶数，直接返回空数组
            return []

        # 统计changed数组中每个元素的频次
        count = Counter(changed)
        # 对changed中的元素进行排序，以确保从最小到最大处理元素
        changed.sort()

        original = []  # 用于存储原始数组的元素
        for x in changed:
            if count[x] == 0:  # 如果该元素已经被完全配对，则跳过
                continue
            if count[2 * x] == 0:  # 如果不存在2倍的元素或已被用尽，则无法形成双倍数组
                return []

            # 将当前元素加入到原数组中，并减少对应元素的频次
            original.append(x)
            count[x] -= 1
            count[2 * x] -= 1

            # 如果减少后2倍元素的频次小于0，说明配对不成功，返回空数组
            if count[2 * x] < 0:
                return []

        return original




print(Solution().findOriginalArray([1, 3, 4, 2, 6, 8]))
print(Solution().findOriginalArray([6, 3, 0, 1]))
print(Solution().findOriginalArray([1]))
print(Solution().findOriginalArray([0, 0, 0, 0]))
