# Implement a method to perform basic string compression using the counts of rep
# eated characters. For example, the string aabcccccaaa would become a2blc5a3. If 
# the "compressed" string would not become smaller than the original string, your 
# method should return the original string. You can assume the string has only upp
# ercase and lowercase letters (a - z). 
# 
#  Example 1: 
# 
#  
# Input: "aabcccccaaa"
# Output: "a2b1c5a3"
#  
# 
#  Example 2: 
# 
#  
# Input: "abbccd"
# Output: "abbccd"
# Explanation: 
# The compressed string is "a1b2c2d1", which is longer than the original string.
# 
#  
# 
#  
# 
#  Note: 
# 
#  
#  0 <= S.length <= 50000 
#  
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return ""
        result = ""
        count = 0
        for i in range(0, len(S)):
            now = S[i]
            count += 1
            if i == len(S) - 1 or now != S[i+1]:
                result += now
                result += str(count)
                count = 0
        return result if len(result) < len(S) else S

a = Solution().compressString("AAABBBCC")

print(a)


# leetcode submit region end(Prohibit modification and deletion)
