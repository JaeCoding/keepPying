# Given an array A of integers, return the number of (contiguous, non-empty) sub
# arrays that have a sum divisible by K. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 30000 
#  -10000 <= A[i] <= 10000 
#  2 <= K <= 10000 
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix = [0] * (len(A) + 1)
        pre_sum = 0
        for i in range(len(A)):
            prefix[i + 1] = (pre_sum + A[i]) % K
            pre_sum += A[i]
        c = Counter(prefix)
        sum = 0
        for (key, val) in c.items():
            if val > 1:
                sum += (val ** 2 - val) // 2
        return sum


a = Solution().subarraysDivByK([4,5,0,-2,-3,1], 5)
print(a)



        
# leetcode submit region end(Prohibit modification and deletion)
