# Given a collection of candidate numbers (candidates) and a target number (targ
# et), find all unique combinations in candidates where the candidate numbers sums
#  to target. 
# 
#  Each number in candidates may only be used once in the combination. 
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
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,5,2,1,2], target = 5,
#  1, 2, 2, 2, 5

# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
#  
#  Related Topics 数组 回溯算法 
#  👍 391 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        out = []
        def back_trace(target_now: int, index_now: int):
            if target_now == 0:
                result.append(out.copy())
            else:
                for i in range(index_now, len(candidates)):
                    if target_now - candidates[i] < 0:
                        break
                    # find the same, choose the last one
                    if i > index_now and candidates[i] == candidates[i - 1]:
                        continue
                    out.append(candidates[i])
                    back_trace(target_now - candidates[i], i + 1)
                    out.pop()
        back_trace(target, 0)
        return result

a = Solution().combinationSum2([2,5,2,1,2], 5)
print(a)
# leetcode submit region end(Prohibit modification and deletion)
