# Given a triangle, find the minimum path sum from top to bottom. Each step you 
# may move to adjacent numbers on the row below. 
# 
#  For example, given the following triangle 
# 
#  
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#  
# 
#  The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11). 
# 
#  Note: 
# 
#  Bonus point if you are able to do this using only O(n) extra space, where n i
# s the total number of rows in the triangle. 
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # 类似的最短路径问题，采用逆推法 shortest path problem, use the backward
    # 自低而上，sum = cur_val + min(left_way_sum, right_way_sum)
    # triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * (len(triangle) + 1)
        for level in range(len(triangle), 0, -1):
            for i in range(0, len(triangle[level-1])):
                dp[i] = min(dp[i], dp[i+1]) + triangle[level-1][i]

        return dp[0]
        
# leetcode submit region end(Prohibit modification and deletion)
