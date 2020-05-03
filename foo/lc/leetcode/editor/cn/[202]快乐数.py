# Write an algorithm to determine if a number n is "happy". 
# 
#  A happy number is a number defined by the following process: Starting with an
# y positive integer, replace the number by the sum of the squares of its digits, 
# and repeat the process until the number equals 1 (where it will stay), or it loo
# ps endlessly in a cycle which does not include 1. Those numbers for which this p
# rocess ends in 1 are happy numbers. 
# 
#  Return True if n is a happy number, and False if not. 
# 
#  Example: 
# 
#  
# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#  
#  Related Topics 哈希表 数学


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isHappy(self, n: int) -> bool:

        has = set()
        while n != 1:
            base = 0
            for s in str(n):
                base += int(s) ** 2
            n = base
            if n in has:
                return False
            has.add(n)
        return True


a = Solution().isHappy(19)
print(a)




        
# leetcode submit region end(Prohibit modification and deletion)
