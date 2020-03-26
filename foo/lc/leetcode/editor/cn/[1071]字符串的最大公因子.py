# For strings S and T, we say "T divides S" if and only if S = T + ... + T (T co
# ncatenated with itself 1 or more times) 
# 
#  Return the largest string X such that X divides str1 and X divides str2. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#  
# 
#  Example 2: 
# 
#  
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#  
# 
#  Example 3: 
# 
#  
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= str1.length <= 1000 
#  1 <= str2.length <= 1000 
#  str1[i] and str2[i] are English uppercase letters. 
#  
#  Related Topics 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_common(s1: str, s2: str) -> bool:
            l1 = len(s1)
            l2 = len(s2)
            if l2 % l1 != 0:
                return False
            start, end = 0, l1
            while end <= len(s2):
                if s1 != s2[start: end]:
                    return False
                start += l1
                end += l1
            return True

        str_m = str1 if len(str1) >= len(str2) else str2
        min_l = min(len(str1), len(str2))

        result = ""
        for i in range(1, min_l+1):
            if len(str1) % i != 0 or len(str2) % i != 0:
                continue
            s_now = str2[0:i]
            if is_common(s_now, str_m):
                result = s_now
        return result


# a = Solution().gcdOfStrings("ABCABC", "ABCD")
# a = Solution().gcdOfStrings("ABABAB", "ABAB")
a = Solution().gcdOfStrings("leet", "code")
print(a)

# leetcode submit region end(Prohibit modification and deletion)
