# In a deck of cards, each card has an integer written on it. 
# 
#  Return true if and only if you can choose X >= 2 such that it is possible to 
# split the entire deck into 1 or more groups of cards, where: 
# 
#  
#  Each group has exactly X cards. 
#  All the cards in each group have the same integer. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: deck = [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
#  
# 
#  Example 2: 
# 
#  
# Input: deck = [1,1,1,2,2,2,3,3]
# Output: false´
# Explanation: No possible partition.
#  
# 
#  Example 3: 
# 
#  
# Input: deck = [1]
# Output: false
# Explanation: No possible partition.
#  
# 
#  Example 4: 
# 
#  
# Input: deck = [1,1]
# Output: true
# Explanation: Possible partition [1,1].
#  
# 
#  Example 5: 
# 
#  
# Input: deck = [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= deck.length <= 10^4 
#  0 <= deck[i] < 10^4 
#  
#  Related Topics 数组 数学


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    # 特殊情况 1,1,1,1,2,2,2,2,2,2 不能用排序，然后模拟计数
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        def gcb(a: int, b: int) -> int:
            return a if b == 0 else gcb(b, a % b)
        # 使用map存下每个数出现的次数，然后求出最大公约数，大于0且相同即满足
        if len(deck) == 1:
            return False
        count = collections.Counter(deck)
        g = 0
        for c in count.values():
            g = gcb(g, c)
            if g == 1:
                return False
        return True





a = Solution().hasGroupsSizeX([1,1,1,1,2,3,2,2,2,2])

print(a)

# leetcode submit region end(Prohibit modification and deletion)
