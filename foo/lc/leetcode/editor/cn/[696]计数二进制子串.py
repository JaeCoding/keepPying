# 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。 
# 
#  重复出现的子串要计算它们出现的次数。 
# 
#  示例 1 : 
# 
#  
# 输入: "00110011"
# 输出: 6
# 解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
# 
# 请注意，一些重复出现的子串要计算它们出现的次数。
# 
# 另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
#  
# 
#  示例 2 : 
# 
#  
# 输入: "10101"
# 输出: 4
# 解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
#  
# 
#  注意： 
# 
#  
#  s.length 在1到50,000之间。 
#  s 只包含“0”或“1”字符。 
#  
#  Related Topics 字符串 
#  👍 257 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) < 2:
            return 0
        result = 0
        l, r = 0, 1
        while r < len(s):
            if s[l] != s[r]:
                in_l, in_r = l, r
                result += 1
                while in_l - 1 >= 0 and s[in_l - 1] == s[in_l] and in_r + 1 < len(s) and s[in_r + 1] == s[in_r]:
                    result += 1
                    in_l -= 1
                    in_r += 1

            l += 1
            r += 1
        return result

a = Solution().countBinarySubstrings("10101")
a = Solution().countBinarySubstrings("00110011")
print(a)
# leetcode submit region end(Prohibit modification and deletion)
