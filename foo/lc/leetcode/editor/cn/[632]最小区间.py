# 你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。 
# 
#  我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。 
# 
#  示例 1: 
# 
#  
# 输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出: [20,24]
# 解释: 
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
#  
# 
#  注意: 
# 
#  
#  给定的列表可能包含重复元素，所以在这里升序表示 >= 。 
#  1 <= k <= 3500 
#  -105 <= 元素的值 <= 105 
#  对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。 
#  
#  Related Topics 哈希表 双指针 字符串 
#  👍 202 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        # 默认dict，key为nums中出现的数字，value为数组吗，存放对应key出现的在nums中的list编号
        indices = collections.defaultdict(list)
        xMin, xMax = 10 ** 9, -10 ** 9
        # 预处理所有元素
        for i, vec in enumerate(nums):
            for x in vec:
                indices[x].append(i)
            # min可以直接传入一个list，带*表示多参数
            xMin = min(xMin, *vec)
            xMax = max(xMax, *vec)

        freq = [0] * n
        inside = 0  # 用于统计是否遍历完所有元素
        # 滑动窗口，先取最小。之后逐步更新
        left, right = xMin, xMin - 1
        bestLeft, bestRight = xMin, xMax

        while right < xMax:
            right += 1
            if right in indices:
                # 发现右元素还在dict中
                for x in indices[right]:
                    # 将此元素所有出现的数组，对应频次+1
                    freq[x] += 1
                    if freq[x] == 1:
                        # 初次添加新元素，inside+1
                        inside += 1
                # 若发现所有元素都统计过
                while inside == n:
                    # 以当前l,f 更新最佳值
                    if right - left < bestRight - bestLeft:
                        bestLeft, bestRight = left, right
                    # 如果左元素在dict中，则扣减对应频次
                    if left in indices:
                        for x in indices[left]:
                            freq[x] -= 1
                            if freq[x] == 0:
                                inside -= 1
                    left += 1

        return [bestLeft, bestRight]

a = Solution().smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]])
print(a)
# leetcode submit region end(Prohibit modification and deletion)
