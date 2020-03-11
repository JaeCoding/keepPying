# In a given grid, each cell can have one of three values: 
# 
#  
#  the value 0 representing an empty cell; 
#  the value 1 representing a fresh orange; 
#  the value 2 representing a rotten orange. 
#  
# 
#  Every minute, any fresh orange that is adjacent (4-directionally) to a rotten
#  orange becomes rotten. 
# 
#  Return the minimum number of minutes that must elapse until no cell has a fre
# sh orange. If this is impossible, return -1 instead. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never 
# rotten, because rotting only happens 4-directionally.
#  
# 
#  
#  Example 3: 
# 
#  
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer
#  is just 0.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= grid.length <= 10 
#  1 <= grid[0].length <= 10 
#  grid[i][j] is only 0, 1, or 2. 
#  
#  
#  
#  Related Topics 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        rotten: set = set()
        rotted: set = set()
        fresh = 0
        for i in range(0, row):
            for j in range(0, col):
                if grid[i][j] == 2:
                    rotten.add(str(i) + "-" + str(j))
                    rotted.add(str(i) + "-" + str(j))
                elif grid[i][j] == 1:
                    fresh += 1
        count = 0
        while rotten:
            if fresh == 0:
                break
            rotten_next: set = set()
            before = int(fresh)
            for s in rotten:
                i = int(s.split("-")[0])
                j = int(s.split("-")[1])
                # 上
                if i - 1 >= 0 and grid[i - 1][j] == 1 and str(i - 1) + "-" + str(j) not in rotted:
                    rotten_next.add(str(i - 1) + "-" + str(j))
                # 下
                if i + 1 < row and grid[i + 1][j] == 1 and str(i + 1) + "-" + str(j) not in rotted:
                    rotten_next.add(str(i + 1) + "-" + str(j))
                # 左
                if j - 1 >= 0 and grid[i][j - 1] == 1 and str(i) + "-" + str(j - 1) not in rotted:
                    rotten_next.add(str(i) + "-" + str(j - 1))
                # 右
                if j + 1 < col and grid[i][j + 1] == 1 and str(i) + "-" + str(j + 1) not in rotted:
                    rotten_next.add(str(i) + "-" + str(j + 1))
            fresh -= len(rotten_next)
            rotted = rotted.union(rotten_next)
            rotten = rotten_next
            count = count + 1 if (before > fresh) else count

        return count if(fresh == 0) else -1


# leetcode submit region end(Prohibit modification and deletion)

a = Solution().orangesRotting([[0,2]])

print(a)

