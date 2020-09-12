# 
#  Find all possible combinations of k numbers that add up to a number n, given 
# that only numbers from 1 to 9 can be used and each combination should be a uniqu
# e set of numbers. 
# 
#  Note: 
# 
#  
#  All numbers will be positive integers. 
#  The solution set must not contain duplicate combinations. 
#  
# 
#  Example 1: 
# 
#  
# Input: k = 3, n = 7
# Output: [[1,2,4]]
#  
# 
#  Example 2: 
# 
#  
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
#  
#  Related Topics 数组 回溯算法 
#  👍 191 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        out = []
        def back_trace(target_now: int, index: int, count: int):
            if target_now == 0 and count == 0:
                result.append(out.copy())
            else:
                for i in range(index, n):
                    if target_now - i < 0:
                        break
                    if i > 9:
                        break
                    out.append(i)
                    back_trace(target_now - i, i + 1, count - 1)
                    out.pop()
        back_trace(n, 1, k)
        return result


a = Solution().combinationSum3(3, 9)
a = Solution().combinationSum3(2, 18)
a = Solution().combinationSum3(3, 7)
print(a)
# leetcode submit region end(Prohibit modification and deletion)
