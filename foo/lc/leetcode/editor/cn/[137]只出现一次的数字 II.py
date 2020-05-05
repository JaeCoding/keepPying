# Given a non-empty array of integers, every element appears three times except 
# for one, which appears exactly once. Find that single one. 
# 
#  Note: 
# 
#  Your algorithm should have a linear runtime complexity. Could you implement i
# t without using extra memory? 
# 
#  Example 1: 
# 
#  
# Input: [2,2,3,2]
# Output: 3
#  
# 
#  Example 2: 
# 
#  
# Input: [0,1,0,1,0,1,99]
# Output: 99 
#  Related Topics 位运算


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def rshift(val, n):
            return val >> n if val >= 0 else (val + 0x100000000) >> n

        res = 0
        for i in range(64):  # 计算数的最大位置 假设最多64位
            number = 0
            for num in nums:
                number += (num >> i) & 1  # 计算所有数 在第i个位数上，有多少个1。
                # 但是如果num是个负数，
            res |= number % 3 << i  # 对第i位汇总后，对3取mod，余下结果，放在res的第i位上（或操作）
        return res




# a = Solution().singleNumber([0, 1, 0, 1, 0, 1, 99])
a = Solution().singleNumber([-2, -2, -4, -2])
print(a)
print(-2 >> 3)
# leetcode submit region end(Prohibit modification and deletion)
