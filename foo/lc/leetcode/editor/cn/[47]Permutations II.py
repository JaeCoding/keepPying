# Given a collection of numbers that might contain duplicates,
# return all possible unique permutations.
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
#  👍 442 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        out = []
        used = []
        def back_trace(start: int):
            if len(out) == len(nums):
                result.append(out.copy())
            else:
                for i in range(len(nums)):
                    # ti
                    if i in used:
                        continue
                    # if n[i] same with n[i-1] and i > index
                    if start < i and nums[i] == nums[i-1]:
                        continue
                    out.append(nums[i])
                    used.append(i)
                    back_trace(i)
                    out.pop()
                    used.pop()

        back_trace(0)
        return result

a = Solution().permuteUnique([1,2,1])
print(a)
# leetcode submit region end(Prohibit modification and deletion)
