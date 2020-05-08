# Given an array of non-negative integers, you are initially positioned at the f
# irst index of the array. 
# 
#  Each element in the array represents your maximum jump length at that positio
# n. 
# 
#  Your goal is to reach the last index in the minimum number of jumps. 
# 
#  Example: 
# 
#  
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index. 
# 
#  Note: 
# 
#  You can assume that you can always reach the last index. 
#  Related Topics 贪心算法 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0
        count = 0
        step = nums[0]
        position = 0
        while position + step < len(nums) - 1:  # 当前位置 + 步数 < 最后
            m = 0
            step_next = 0
            for i in range(1, step + 1):
                if (nums[position + i] + i) > m:
                    m = nums[position + i] + i
                    step_next = i
            position += step_next
            step = nums[position]
            count += 1

        return count + 1  # 加一步走到最后位置


    # 错误解法 在2,3,1情况下  贪心走到3再走到1，其实可以一步到1，因为优先走到最后一格，走不到再贪心最长距离
    def jump2(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        step_len = nums[0]  # 可跳跃步数
        pos = 0  # 当前位置
        count = 0
        while pos < len(nums) - 1:  # 只要没达到最后一格
            longest = 0  # 计算跳跃最远位置
            next = 0  # 计算要跳的长度
            for i in range(1, step_len + 1):
                if pos + i < len(nums) and nums[pos + i] + i >= longest:  # >=  尽量选靠后的位置
                    longest = nums[pos + i] + i
                    next = i
            pos += next  # 跳过去
            step_len = nums[pos]  # 下一次可跳的步数
            count += 1
        return count
a = Solution().jump2([2,3,1,1,4])
a = Solution().jump2([3,2,1])
a = Solution().jump2([2,3,1])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
