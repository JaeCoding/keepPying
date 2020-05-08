# Given a 2D binary matrix filled with 0's and 1's, find the largest square cont
# aining only 1's and return its area. 
# 
#  Example: 
# 
#  
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        n = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    add = 1
                    flag = True
                    while flag:
                        for z in range(add):
                            # col
                            if j + z >= len(matrix[0]) or matrix[i][j + z] == '0':
                                flag = False
                                break
                            # row
                            if i + z >= len(matrix) or matrix[i + z][j] == '0':
                                flag = False
                                break
                        if flag:
                            add += 1
                    n = max(n, add - 1)
        return n ** 2

a = Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
a = Solution().maximalSquare([["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
