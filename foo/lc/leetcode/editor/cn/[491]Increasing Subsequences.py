# Given an integer array, your task is to find all the different possible increa
# sing subsequences of the given array, and the length of an increasing subsequenc
# e should be at least 2. 
# 
#  
# 
#  Example: 
# 
#  
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4
# ,7,7]]
#  
# 
#  
#  Constraints: 
# 
#  
#  The length of the given array will not exceed 15. 
#  The range of integer in the given array is [-100,100]. 
#  The given array may contain duplicates, and two equal integers should also be
#  considered as a special case of increasing sequence. 
#  
#  Related Topics 深度优先搜索 
#  👍 170 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums: List[int], tmp: List[int]) -> None:
            # 大于2则添加
            if len(tmp) > 1:
                res.append(tmp)

            curPres = set()
            for inx, i in enumerate(nums):
                # 如果当前值在以前已被遍历，则跳过
                if i in curPres:
                    continue
                # 如果tmp为空 或者 i加入tmp可以形成递增子序列
                if not tmp or i >= tmp[-1]:
                    # 记录
                    curPres.add(i)
                    # 取inx后部分  已存list添加
                    dfs(nums[inx+1:], tmp+[i])

        dfs(nums, [])
        return res



a = Solution().findSubsequences([4, 6, 7, 7])
# a = Solution().findSubsequences([1,2,3,4,5,6,7,8,9,10,1,1,1,1,1])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
