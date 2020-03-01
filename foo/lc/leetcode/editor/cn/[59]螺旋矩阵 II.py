# Given a positive integer n, generate a square matrix filled with elements from
#  1 to n2 in spiral order. 
# 
#  Example: 
# 
#  
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        left = 0
        right = n - 1
        cur = 1
        while left <= right:

            if left == right:
                result[left][left] = cur

            for i in range(left, right):
                result[left][i] = cur
                cur += 1

            for i in range(left, right):
                result[i][right] = cur
                cur += 1

            for i in range(right, left, -1):
                result[right][i] = cur
                cur += 1

            for i in range(right, left, -1):
                result[i][left] = cur
                cur += 1

            left += 1
            right -= 1
        return result


# leetcode submit region end(Prohibit modification and deletion)


a = Solution().generateMatrix(1)

# print(a)
