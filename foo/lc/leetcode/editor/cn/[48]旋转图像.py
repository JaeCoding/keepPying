# You are given an n x n 2D matrix representing an image. 
# 
#  Rotate the image by 90 degrees (clockwise). 
# 
#  Note: 
# 
#  You have to rotate the image in-place, which means you have to modify the inp
# ut 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation. 
# 
#  Example 1: 
# 
#  
# Given input matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# 
# rotate the input matrix in-place such that it becomes:
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
# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 
# 
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
import math
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        top = len(matrix) - 1
        j_num = top
        for i in range(0, int(len(matrix) / 2)):
            for j in range(i, j_num):
                # save 2
                put = matrix[i][j]
                save = matrix[j][top - i]
                matrix[j][top - i] = put

                # save 3
                put = save
                save = matrix[top - i][top - j]
                matrix[top - i][top - j] = put

                #
                put = save
                save = matrix[top - j][i]
                matrix[top - j][i] = put

                #
                put = save
                matrix[i][j] = put
            j_num -= 1



a = Solution().rotate([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# leetcode submit region end(Prohibit modification and deletion)
