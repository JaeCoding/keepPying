# Given a 2d grid map of '1's (land) and '0's (water), count the number of islan
# ds. An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all su
# rrounded by water. 
# 
#  Example 1: 
# 
#  
# Input:
# 11110
# 11010
# 11000
# 00000
# 
# Output: 1
#  
# 
#  Example 2: 
# 
#  
# Input:
# 11000
# 11000
# 00100
# 00011
# 
# Output: 3
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        next_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '-1'
                    stack = [(i, j)]
                    while stack:
                        (now_i, now_j) = stack.pop()
                        for (plus_i, plus_j) in next_list:
                            next_i = now_i + plus_i
                            next_j = now_j + plus_j
                            if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]) and grid[next_i][next_j] == '1':
                                stack.append((next_i, next_j))
                                grid[next_i][next_j] = '-1'
        return count


# a = Solution().numIslands([["1","1","1","1","0"],
#                            ["1","1","0","1","0"],
#                            ["1","1","0","0","0"],
#                            ["0","0","0","0","0"]])

a = Solution().numIslands([["1","1","0","0","0"],
                           ["1","1","0","0","0"],
                           ["0","0","1","0","0"],
                           ["0","0","0","1","1"]])
print(a)





# leetcode submit region end(Prohibit modification and deletion)
