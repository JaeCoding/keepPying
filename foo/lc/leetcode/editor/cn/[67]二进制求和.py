# Given two binary strings, return their sum (also a binary string). 
# 
#  The input strings are both non-empty and contains only characters 1 or 0. 
# 
#  Example 1: 
# 
#  
# Input: a = "11", b = "1"
# Output: "100" 
# 
#  Example 2: 
# 
#  
# Input: a = "1010", b = "1011"
# Output: "10101" 
#  Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = max(len(a), len(a))
        plus = 0
        result = ""
        for i in range(0, l):
            i_a = a.index(len(a) - 1 - i) if(i < len(a)) else 0
            i_b = b.index(len(b) - 1 - i) if(i < len(b)) else 0
            sum: int = i_a + i_b + plus
            if sum > 1:
                plus = 1
                result = (sum - 2) + result
            else:
                plus = 0
                result = sum + result



        return result

# leetcode submit region end(Prohibit modification and deletion)


a = Solution().addBinary("1010",)