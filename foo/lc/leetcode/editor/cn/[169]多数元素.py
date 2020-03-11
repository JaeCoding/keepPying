# Given an array of size n, find the majority element. The majority element is t
# he element that appears more than ⌊ n/2 ⌋ times. 
# 
#  You may assume that the array is non-empty and the majority element always ex
# ist in the array. 
# 
#  Example 1: 
# 
#  
# Input: [3,2,3]
# Output: 3 
# 
#  Example 2: 
# 
#  
# Input: [2,2,1,1,1,2,2]
# Output: 2
#  
#  Related Topics 位运算 数组 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 投票
        count = 0
        max = None
        for num in nums:
           if count == 0:
               max = num
               count += 1
           elif num != max:
               count -= 1
           elif num == max:
               count += 1
        return max



# leetcode submit region end(Prohibit modification and deletion)
Solution().majorityElement([3,3,4])