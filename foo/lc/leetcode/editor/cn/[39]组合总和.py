# Given a set of candidate numbers (candidates) (without duplicates) and a targe
# t number (target), find all unique combinations in candidates where the candidat
# e numbers sums to target. 
# 
#  The same repeated number may be chosen from candidates unlimited number of ti
# mes. 
# 
#  Note: 
# 
#  
#  All numbers (including target) will be positive integers. 
#  The solution set must not contain duplicate combinations. 
#  
# 
#  Example 1: 
# 
#  
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
#  
#  Related Topics 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        out = []
        result = []

        def back_track(cur_target, index) -> int:
            if cur_target == 0:
                result.append(out.copy())
                return 0
            else:
                for i in range(index, len(candidates)):
                    if candidates[i] <= cur_target:
                        out.append(candidates[i])
                        back_track(cur_target - candidates[i], i)
                        out.pop()
                    else:
                        break

        back_track(target, 0)

        return result


a = Solution().combinationSum([2, 3, 5], 8)

# leetcode submit region end(Prohibit modification and deletion)
