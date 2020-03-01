# Given a non-negative integer numRows, generate the first numRows of Pascal's t
# riangle. 
# 
#  
# In Pascal's triangle, each number is the sum of the two numbers directly above
#  it. 
# 
#  Example: 
# 
#  
# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = []
        for row in range(1, numRows+1):
            row_num = []
            for col in range(1, row+1):
                if col == 1 or col == row:
                    row_num.append(1)
                else:
                    row_num.append(result[row -2][col-2] + result[row -2][col-1])
            result.append(row_num)
        return result


# leetcode submit region end(Prohibit modification and deletion)

a = Solution().generate(3)
b = [0] * (3 + 1)

print(b)
b[2] = 1
print(b)
