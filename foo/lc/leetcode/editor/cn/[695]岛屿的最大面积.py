# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (r
# epresenting land) connected 4-directionally (horizontal or vertical.) You may as
# sume all four edges of the grid are surrounded by water. 
# 
#  Find the maximum area of an island in the given 2D array. (If there is no isl
# and, the maximum area is 0.) 
# 
#  Example 1: 
# 
#  
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#  
# Given the above grid, return 6. Note the answer is not 11, because the island 
# must be connected 4-directionally.
# 
#  Example 2: 
# 
#  
# [[0,0,0,0,0,0,0,0]] 
# Given the above grid, return 0.
# 
#  Note: The length of each dimension in the given grid does not exceed 50. 
#  Related Topics 深度优先搜索 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

#
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(row_now: int, col_now: int) -> int:

            if grid[row_now][col_now] != 1:
                return 0

            count = 1
            # mark has visit
            grid[row_now][col_now] = -2
            # up
            if row_now - 1 >= 0 and grid[row_now - 1][col_now] == 1:
                count += bfs(row_now - 1, col_now)
            # down
            if row_now + 1 < row and grid[row_now + 1][col_now] == 1:
                count += bfs(row_now + 1, col_now)
            # left
            if col_now - 1 >= 0 and grid[row_now][col_now - 1] == 1:
                count += bfs(row_now, col_now - 1)
            # right
            if col_now + 1 < col and grid[row_now][col_now + 1] == 1:
                count += bfs(row_now, col_now + 1)

            return count

        row = len(grid)
        col = len(grid[0])
        m = 0
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == 1:
                    m = max(m, bfs(i, j))
        return m

a = Solution().maxAreaOfIsland([[0,1],[1,1]])

print(a)





        
# leetcode submit region end(Prohibit modification and deletion)
