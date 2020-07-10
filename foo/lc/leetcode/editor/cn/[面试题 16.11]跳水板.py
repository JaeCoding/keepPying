# You are building a diving board by placing a bunch of planks of wood end-to-en
# d. There are two types of planks, one of length shorter and one of length longer
# . You must use exactly K planks of wood. Write a method to generate all possible
#  lengths for the diving board. 
# 
#  return all lengths in non-decreasing order. 
# 
#  Example: 
# 
#  
# Input: 
# shorter = 1
# longer = 2
# k = 3
# Output:  {3,4,5,6}
#  
# 
#  Note: 
# 
#  
#  0 < shorter <= longer 
#  0 <= k <= 100000 
#  
#  Related Topics 递归 记忆化


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        result = set()
        s = 0
        l = k
        while l >= 0:
            result.add(s * shorter + l * longer)
            s += 1
            l -= 1
        return sorted(list(result))

# a = Solution().divingBoard(1,2,3)
a = Solution().divingBoard(2,1118596,979)
print(a)


# leetcode submit region end(Prohibit modification and deletion)
