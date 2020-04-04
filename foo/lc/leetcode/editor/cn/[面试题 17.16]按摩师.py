# A popular masseuse receives a sequence of back-to-back appointment requests an
# d is debating which ones to accept. She needs a break between appointments and t
# herefore she cannot accept any adjacent requests. Given a sequence of back-to-ba
# ck appoint ment requests, find the optimal (highest total booked minutes) set th
# e masseuse can honor. Return the number of minutes. 
# 
#  Note: This problem is slightly different from the original one in the book. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input:  [1,2,3,1]
# Output:  4
# Explanation:  Accept request 1 and 3, total minutes = 1 + 3 = 4
#  
# 
#  Example 2: 
# 
#  
# Input:  [2,7,9,3,1]
# Output:  12
# Explanation:  Accept request 1, 3 and 5, total minutes = 2 + 9 + 1 = 12
#  
# 
#  Example 3: 
# 
#  
# Input:  [2,1,4,5,3,1,1,3]
# Output:  12
# Explanation:  Accept request 1, 3, 5 and 8, total minutes = 2 + 4 + 3 + 3 = 12
# 
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        dp0 = 0
        dp1 = nums[0]
        now = 0
        for i in range(0, n):  # 从1开始
            tdp0 = max(dp0, dp1)  # 若i不接,延续上一轮的大者
            tdp1 = dp0 + nums[i]  # 若i接了, 取上一轮的未接 + i
            dp0, dp1 = tdp0, tdp1
        return max(dp0, dp1)




# leetcode submit region end(Prohibit modification and deletion)
