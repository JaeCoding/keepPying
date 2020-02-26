# Given a set of distinct integers, nums, return all possible subsets (the power
#  set). 
# 
#  Note: The solution set must not contain duplicate subsets. 
# 
#  Example: 
# 
#  
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ] 
#  Related Topics 位运算 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []

        result: List[List[int]] = []
        out: List[int] = []

        def back_track(position):
            result.append(out.copy())

            for i in range(position, len(nums)):
                out.append(nums[i])
                back_track(i + 1)
                out.pop()
        back_track(0)

        return result



# leetcode submit region end(Prohibit modification and deletion)

a = Solution().subsets([1,2,3])