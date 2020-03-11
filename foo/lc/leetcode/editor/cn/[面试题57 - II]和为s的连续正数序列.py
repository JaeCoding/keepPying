# English description is not available for the problem. Please switch to Chinese
# . 
# 


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        result = []
        for i in range(1, target):
            w = (1-2*i + ((2 * i - 1) ** 2 + 8 * target) ** 0.5 ) / 2
            if w == int(w):
                result.append([j for j in range(i, i + int(w))])
        return result
# leetcode submit region end(Prohibit modification and deletion)

a = Solution().findContinuousSequence(0)

print(a)