# Given an array of n positive integers and a positive integer s, find the minim
# al length of a contiguous subarray of which the sum ≥ s. If there isn't one, ret
# urn 0 instead. 
# 
#  Example: 
# 
#  
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem const
# raint. 
# 
#  Follow up: 
# 
#  If you have figured out the O(n) solution, try coding another solution of whi
# ch the time complexity is O(n log n). 
#  Related Topics 数组 双指针 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or sum(nums) < s:
            return 0

        l_now, r_now = 0, 0
        min_len = 10000000
        sum_now = 0
        while l_now < len(nums):

            if sum_now < s and r_now < len(nums):
                sum_now += nums[r_now]
                r_now += 1
            else:
                # compare len
                if sum_now >= s and r_now - l_now < min_len:
                    min_len = r_now - l_now

                sum_now -= nums[l_now]
                l_now += 1

        return min_len

a = Solution().minSubArrayLen(7, [2,3,1,2,4,3])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
