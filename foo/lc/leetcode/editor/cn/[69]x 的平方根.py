# Implement int sqrt(int x). 
# 
#  Compute and return the square root of x, where x is guaranteed to be a non-ne
# gative integer. 
# 
#  Since the return type is an integer, the decimal digits are truncated and onl
# y the integer part of the result is returned. 
# 
#  Example 1: 
# 
#  
# Input: 4
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.
#  
#  Related Topics 数学 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def mySqrt(self, x: int) -> int:

        left, right = 0, x
        while True:
            mid = int((left + right) / 2)
            if pow(mid, 2) <= x <= pow(mid + 1, 2):
                mid = mid + 1 if x == pow(mid + 1, 2) else mid
                break
            elif pow(mid, 2) > x:
                right = mid
            elif pow(mid, 2) < x:
                left = mid
        return mid

a = Solution().mySqrt(1)
print(a)
# leetcode submit region end(Prohibit modification and deletion)
