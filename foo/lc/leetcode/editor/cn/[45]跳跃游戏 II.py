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
        while position + step < len(nums) - 1:
            m = 0
            step_next = 0
            for i in range(1, step + 1):
                if (nums[position + i] + i) > m:
                    m = nums[position + i] + i
                    step_next = i
            position += step_next
            step = nums[position]
            count += 1

        return count + 1

# leetcode submit region end(Prohibit modification and deletion)
