# Given an image represented by an N x N matrix, where each pixel in the image i
# s 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in 
# place? 
# 
#  
# 
#  Example 1: 
# 
#  
# Given matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# 
# Rotate the matrix in place. It becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
#  
# 
#  Example 2: 
# 
#  
# Given matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 
# 
# Rotate the matrix in place. It becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 先沿着左上到右下对角线，即\， 做翻转（若要左旋，则对 / 对角线翻转
        for i, j in [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])) if i > j]:
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        # 再对中对称轴 | 做翻转
        for i, j in [(i, j) for i in range(len(matrix)) for j in range(int(len(matrix[0])/2))]:
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][len(matrix) - 1 - j]
            matrix[i][len(matrix) - 1 - j] = temp

        print(matrix)

a = Solution().rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
])







# leetcode submit region end(Prohibit modification and deletion)
