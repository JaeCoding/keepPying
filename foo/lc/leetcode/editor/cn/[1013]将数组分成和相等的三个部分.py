# Given an array A of integers, return true if and only if we can partition the 
# array into three non-empty parts with equal sums. 
# 
#  Formally, we can partition the array if we can find indexes i+1 < j with (A[0
# ] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... +
#  A[A.length - 1]) 
# 
#  
#  Example 1: 
# 
#  
# Input: A = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#  
# 
#  Example 2: 
# 
#  
# Input: A = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: A = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= A.length <= 50000 
#  -10^4 <= A[i] <= 10^4 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    # 错误的解法 只在全部是正数情况下有效
    def canThreePartsEqualSum(self, A: List[int]) -> bool:

        if len(A) < 3:
            return False

        total = sum(A)
        left, right = 0, len(A) - 1
        sum_l, sum_r = A[0], A[len(A) - 1]

        while left + 1 < right:
            if sum_l < sum_r:
                left += 1
                sum_l += A[left]
            elif sum_l > sum_r:
                right -= 1
                sum_r += A[right]
            else:
                if sum_l == total - sum_l - sum_r:
                    return True
                else:
                    left += 1
                    sum_l += A[left]

        return False

    # 从1/3关键单入手
    def canThreePartsEqualSum(self, A: List[int]) -> bool:

        if len(A) < 3:
            return False

        total = sum(A)

        if total % 3 != 0:
            return False

        target = total / 3

        left, right = 0, len(A) - 1
        sum_l, sum_r = A[0], A[len(A) - 1]

        while left + 1 < right:
            if sum_l != target:
                left += 1
                sum_l += A[left]

            if sum_r != target:
                right -= 1
                sum_r += A[right]
            if left + 1 >= right:
                return False
            if sum_l == sum_r == target:
                return True

        return False

a = Solution().canThreePartsEqualSum([1,-1,1,-1])
print(a)
# leetcode submit region end(Prohibit modification and deletion)
