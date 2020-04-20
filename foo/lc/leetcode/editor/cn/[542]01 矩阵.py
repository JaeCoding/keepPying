# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for eac
# h cell. 
# 
#  The distance between two adjacent cells is 1. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
# 
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#  
# 
#  Example 2: 
# 
#  
# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
# 
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]
#  
# 
#  
# 
#  Note: 
# 
#  
#  The number of elements of the given matrix will not exceed 10,000. 
#  There are at least one 0 in the given matrix. 
#  The cells are adjacent in only four directions: up, down, left and right. 
#  
#  Related Topics 深度优先搜索 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix)):
            for j in range(len((matrix[0]))):
                if matrix[i][j] != 0:
                    matrix[i][j] = 100000000000000

        for i in range(len(matrix)):
            for j in range(len((matrix[0]))):
                if j < len(matrix[0]) - 1:
                    matrix[i][j] = min(matrix[i][j], matrix[i][j + 1] + 1)
                if i < len(matrix) - 1:
                    matrix[i][j] = min(matrix[i][j], matrix[i + 1][j] + 1)

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len((matrix[0])) - 1, -1, -1):
                if j > 0:
                    matrix[i][j] = min(matrix[i][j], matrix[i][j - 1] + 1)
                if i > 0:
                    matrix[i][j] = min(matrix[i][j], matrix[i - 1][j] + 1)
        return matrix

a = Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
a = Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
