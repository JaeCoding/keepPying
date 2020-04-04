# Given a m x n matrix, if an element is 0, set its entire row and column to 0. 
# Do it in-place. 
# 
#  Example 1: 
# 
#  
# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
#  
# 
#  Follow up: 
# 
#  
#  A straight forward solution using O(mn) space is probably a bad idea. 
#  A simple improvement uses O(m + n) space, but still not the best solution. 
#  Could you devise a constant space solution? 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag = False
        line_flag = False
        for x, y in [(x, y) for x in range(len(matrix)) for y in range(len(matrix[0]))]:

            if matrix[x][y] == 0:
                if x == 0 and not row_flag:
                    row_flag = True #第一行发现了0，最后需要制空第一行
                if y == 0 and not line_flag:
                    line_flag = True #第一列发现了0，最后需要制空第一行
                matrix[x][0] = 0
                matrix[0][y] = 0
        for x, y in [(x, y) for x in range(len(matrix)) for y in range(len(matrix[0])) if matrix[x][0] == 0 or matrix[0][y] == 0]:
            # 暂时不能改第一行第一列，不然会影响判断
            if x > 0 and y > 0:
                matrix[x][y] = 0
        # 修改第一行第一列
        if row_flag:
            for y in range(len(matrix[0])):
                matrix[0][y] = 0
        if line_flag:
            for x in range(len(matrix)):
                matrix[x][0] = 0

        # print(matrix)




a = Solution().setZeroes([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

# a = Solution().setZeroes([[1,1,1],[0,1,2]])



# leetcode submit region end(Prohibit modification and deletion)
