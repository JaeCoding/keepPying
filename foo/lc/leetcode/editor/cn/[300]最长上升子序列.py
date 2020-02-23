# Given an unsorted array of integers, find the length of longest increasing sub
# sequence. 
# 
#  Example: 
# 
#  
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the 
# length is 4. 
# 
#  Note: 
# 
#  
#  There may be more than one LIS combination, it is only necessary for you to r
# eturn the length. 
#  Your algorithm should run in O(n2) complexity. 
#  
# 
#  Follow up: Could you improve it to O(n log n) time complexity? 
#  Related Topics 二分查找 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    # 10, 9, 2, 5, 3, 7, 101, 18
    # find the LIS, is try to add the current element to previous sequences,
    # as 3, only can add to 2, but to 101, can add to every element cause it more the before
    # dp[i] represents lengthOfLIS in i, and for j in [0, i), dp[i] = dp[j] + 1 in one choice, finally, dp[i] = max(dp[j] + 1)
    def lengthOfLIS(self, nums: List[int]) -> int:

        # boundary
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(0, len(nums)):
            for j in range(0, i):
                # allow to added after j
                if nums[i] > nums[j]:
                    # choose the max one
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)



        
# leetcode submit region end(Prohibit modification and deletion)
