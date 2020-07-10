# A robot is located at the top-left corner of a m x n grid (marked 'Start' in t
# he diagram below). 
# 
#  The robot can only move either down or right at any point in time. The robot 
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in the d
# iagram below). 
# 
#  Now consider if some obstacles are added to the grids. How many unique paths 
# would there be? 
# 
#  
# 
#  An obstacle and empty space is marked as 1 and 0 respectively in the grid. 
# 
#  Note: m and n will be at most 100. 
# 
#  Example 1: 
# 
#  
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#  
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if obstacleGrid[0][0] == 1:
            return 0

        row = len(obstacleGrid)
        col = len(obstacleGrid[0])

        dp = [[0 for _ in range(col)] for _ in range(row)]
        dp[0][0] = 1

        for i in range(row):
            for j in range(col):
                if (i, j) == (0, 0):
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    left = dp[i][j - 1] if j - 1 >= 0 else 0
                    up = dp[i - 1][j] if i - 1 >= 0 else 0
                    dp[i][j] = left + up
        return dp[row - 1][col - 1]

a = Solution().uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
