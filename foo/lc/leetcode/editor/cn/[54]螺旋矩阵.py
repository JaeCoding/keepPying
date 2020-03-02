# Given a matrix of m x n elements (m rows, n columns), return all elements of t
# he matrix in spiral order. 
# 
#  Example 1: 
# 
#  
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#  
# 
#  Example 2: 
#  
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

# 注意三种情况！ 注意流出最后一格。注意中途的边界。
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix:
            return []
        result = []

        r1, c1 = 0, 0
        r2, c2 = len(matrix) - 1, len(matrix[0]) - 1

        def recur(row1, col1, row2, col2):
            if row2 - row1 == 0:
                for i in range(col1, col2+1):
                    result.append(matrix[row2][i])
            elif col2 - col1 == 0:
                for i in range(row1, row2+1):
                    result.append(matrix[i][col2])
            else:

                # 留下最后一个不走
                for i in range(col1, col2):
                    result.append(matrix[row1][i])

                for i in range(row1, row2):
                    result.append(matrix[i][col2])

                for i in range(col2, col1, -1):
                    result.append(matrix[row2][i])

                for i in range(row2, row1, -1):
                    result.append(matrix[i][col1])

                if col1 == col2 and row1 == row2:
                    result.append(matrix[row1][col2])

        while r1 <= r2 and c1 <= c2:
            recur(r1, c1, r2, c2)
            r1 += 1
            c1 += 1
            r2 -= 1
            c2 -= 1

        return result



# leetcode submit region end(Prohibit modification and deletion)

a = Solution().spiralOrder([[1],[2]])
