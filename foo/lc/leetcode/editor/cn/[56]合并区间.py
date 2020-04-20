# Given a collection of intervals, merge all overlapping intervals. 
# 
#  Example 1: 
# 
#  
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#  
# 
#  Example 2: 
# 
#  
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping. 
# 
#  NOTE: input types have been changed on April 15, 2019. Please reset to defaul
# t code definition to get new method signature. 
#  Related Topics 排序 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda word: word[0])

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            now = intervals[i]
            last = result[-1]
            if not now[1] < last[0] and not last[1] < now[0]:
                result[-1] = [min(last[0], now[0]), max(last[1], now[1])]
            else:
                result.append(now)
        return result


a = Solution().merge([[1,3],[2,6],[15,18],[8,10]])

a = Solution().merge([[1,4],[4,5]])
a = Solution().merge([[1,4]])
a = Solution().merge([])
a = Solution().merge([[1,4],[5,6]])
a = Solution().merge([[1,3],[2,6],[8,10],[15,18]])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
