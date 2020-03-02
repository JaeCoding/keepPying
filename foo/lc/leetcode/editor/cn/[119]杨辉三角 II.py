# Given a non-negative index k where k ≤ 33, return the kth index row of the Pas
# cal's triangle. 
# 
#  Note that the row index starts from 0. 
# 
#  
# In Pascal's triangle, each number is the sum of the two numbers directly above
#  it. 
# 
#  Example: 
# 
#  
# Input: 3
# Output: [1,3,3,1]
#  
# 
#  Follow up: 
# 
#  Could you optimize your algorithm to use only O(k) extra space? 
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        last = [1] * (rowIndex + 1)
        for row in range(0, rowIndex + 1):
            # 从中间向两边加，才不会影响 比如[1,3,3,1,1] -> [1,3,6,1,10 而不是[1,4,3,1,1]，这样位置1的元素被覆盖了
            for col in range(int(row / 2), 0, -1):
                if col != 0:
                    last[col] = last[col] + last[col - 1]
                last[row - col] = last[col]
        return last


# leetcode submit region end(Prohibit modification and deletion)

a = Solution().getRow(4)
print(3)
