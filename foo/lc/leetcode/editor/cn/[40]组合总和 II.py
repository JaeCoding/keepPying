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
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
#  
#  Related Topics 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        out = []
        result = []
        # has: set = set()
        def backtrace(target_now, cur):
            if target_now == 0:
                result.append(out.copy())
            else:
                for i in range(cur, len(candidates)):
                    # 如果i比入口位置大，且i与上一个位置元素相同
                    # 比如在[1,2,2,2,5],5迭代到[1,2,2]添加一个结果，然后返回pop成[1,2]时，cur是2，i是3,
                    # 然后发现 i > cur and i位置与上一个相同，那么就没必要再算一次[1,2,2]了
                    if i > cur and candidates[i] == candidates[i - 1]:
                        continue
                    if candidates[i] > target_now:
                        break

                    out.append(candidates[i])
                    # has.add(i)
                    backtrace(target_now - candidates[i], i+1)
                    out.pop()
                    # has.remove(i)
        backtrace(target, 0)
        return result



# leetcode submit region end(Prohibit modification and deletion)

a = Solution().combinationSum2([2,5,2,1,2], 5)
print(a)