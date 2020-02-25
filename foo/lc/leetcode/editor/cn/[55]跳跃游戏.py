# Given an array of non-negative integers, you are initially positioned at the f
# irst index of the array. 
# 
#  Each element in the array represents your maximum jump length at that positio
# n. 
# 
#  Determine if you are able to reach the last index. 
# 
#  Example 1: 
# 
#  
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#  
# 
#  Example 2: 
# 
#  
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last ind
# ex.
#  
#  Related Topics 贪心算法 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        position = 0
        while position < len(nums)-1:
            if position + nums[position] >= len(nums)-1:
                return True
            if nums[position] == 0:
                return False

            step_count = 0
            m = 0
            for i in range(1, nums[position]+1):
                if nums[position + i] + i >= m:
                    step_count = i
                    m = nums[position + i] + i
            position += step_count
        return True

# leetcode submit region end(Prohibit modification and deletion)

a = Solution().canJump([2,5,0,0])