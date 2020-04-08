# Given an array of integers A, a move consists of choosing any A[i], and increm
# enting it by 1. 
# 
#  Return the least number of moves to make every value in A unique. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: [1,2,2]
# Output: 1
# Explanation:  After 1 move, the array could be [1, 2, 3].
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [3,2,1,2,1,7]
# Output: 6
# Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to ha
# ve all unique values.
#  
# 
#  
#  
# 
#  Note: 
# 
#  
#  0 <= A.length <= 40000 
#  0 <= A[i] < 40000 
#  
# 
#  
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # 此种解法 当数量很大时会超时
    def minIncrementForUnique(self, A: List[int]) -> int:
        sorted(A)
        has = set(A)
        result = 0
        not_one = set()
        for i in range(0, len(A)):
            if A[i] not in not_one:
                not_one.add(A[i])
            else:
                not_use = min(has)
                while not_use in has or not_use <= A[i]:
                    not_use += 1
                result += not_use - A[i]
                has.add(not_use)
        return result

    def minIncrementForUnique2(self, A: List[int]) -> int:
        A.sort()
        res = 0
        for i in range(1, len(A)):
            if A[i] <= A[i - 1]:
                res += A[i - 1] - A[i] + 1
                A[i] = A[i - 1] + 1
        return res

a = Solution().minIncrementForUnique2([1,2,2])
print(a)
        
# leetcode submit region end(Prohibit modification and deletion)
