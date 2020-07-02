# Given two integer arrays A and B, return the maximum length of an subarray tha
# t appears in both arrays. 
# 
#  Example 1: 
# 
#  
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= len(A), len(B) <= 1000 
#  0 <= A[i], B[i] < 100 
#  
# 
#  Related Topics 数组 哈希表 二分查找 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:

        # prepare more rows and col, to solve the corner case
        dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

        m = 0
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if B[i - 1] == A[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    m = max(m, dp[i][j])

        return m

a = Solution().findLength([1,2,3,2,1], [3,2,1,4,7])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
