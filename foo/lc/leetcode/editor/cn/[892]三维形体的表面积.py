# On a N * N grid, we place some 1 * 1 * 1 cubes. 
# 
#  Each value v = grid[i][j] represents a tower of v cubes placed on top of grid
#  cell (i, j). 
# 
#  Return the total surface area of the resulting shapes. 
# 
#  
# 
#  
#  
#  
#  
#  
#  
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [[2]]
# Output: 10
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [[1,2],[3,4]]
# Output: 34
#  
# 
#  
#  Example 3: 
# 
#  
# Input: [[1,0],[0,2]]
# Output: 16
#  
# 
#  
#  Example 4: 
# 
#  
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
#  
# 
#  
#  Example 5: 
# 
#  
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= N <= 50 
#  0 <= grid[i][j] <= 50 
#  
#  
#  
#  
#  
#  
#  Related Topics 几何 数学


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:

        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                layer = grid[i][j]
                if layer == 0:
                    continue
                else:
                    base = 2 + 4 * layer
                    base -= 0 if i - 1 < 0 else min(layer, grid[i - 1][j])
                    base -= 0 if i + 1 == len(grid) else min(layer, grid[i + 1][j])
                    base -= 0 if j - 1 < 0 else min(layer, grid[i][j - 1])
                    base -= 0 if j + 1 == len(grid[0]) else min(layer, grid[i][j + 1])
                    count += base
        return count


a = Solution().surfaceArea([[2,2,2],[2,1,2],[2,2,2]])
print(a)
# leetcode submit region end(Prohibit modification and deletion)
