# Given an integer array nums, find the contiguous subarray (containing at least
#  one number) which has the largest sum and return its sum. 
# 
#  Example: 
# 
#  
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#  
# 
#  Follow up: 
# 
#  If you have figured out the O(n) solution, try coding another solution using 
# the divide and conquer approach, which is more subtle. 
#  Related Topics 数组 分治算法 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        result = nums[0]
        now = 0

        for i in nums:
            # 当前汇总为正的话 还有能力去添加下一个数
            if now > 0:
                now += i
            # 否则就成为 下一个数
            else:
                now = i
            result = max(result, now)
        return result


a = Solution().maxSubArray([-2, -1])
a = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(a)
# leetcode submit region end(Prohibit modification and deletion)
