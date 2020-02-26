# Given a collection of numbers that might contain duplicates, return all possib
# le unique permutations. 
# 
#  Example: 
# 
#  
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#  
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]
        nums.sort()
        result = []
        out = []
        contained: set = set()

        def back_trace(position: int):
            if len(out) == len(nums):
                result.append(out.copy())
            else:

                for i in range(0, len(nums)):
                    if i in contained:
                        continue
                    # same as previous and previous not add, as [1,1,3]
                    if i > 0 and nums[i] == nums[i-1] and i-1 not in contained:
                        continue
                    out.append(nums[i])
                    contained.add(i)
                    back_trace(i)
                    out.pop()
                    contained.remove(i)

        back_trace(0)

        return result




# leetcode submit region end(Prohibit modification and deletion)

a = Solution().permuteUnique([1,1,2])