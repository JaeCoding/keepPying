# Given a string which consists of lowercase or uppercase letters, find the leng
# th of the longest palindromes that can be built with those letters. 
# 
#  This is case sensitive, for example "Aa" is not considered a palindrome here.
#  
# 
#  Note: 
# Assume the length of given string will not exceed 1,010.
#  
# 
#  Example: 
#  
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#  
#  Related Topics 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = dict()
        count = 0
        use = False
        for i in s:
            m[i] = m[i] + 1 if i in m else 1
        for i in m:
            if m[i] % 2 == 0:
                count += m[i]
            else:
                if not use:
                    count += 1
                    use = True
                count += m[i] - 1
        return count

    def longestPalindrome(self, s: str) -> int:
        m = dict()
        count = 0
        use = False
        for i in s:
            m[i] = m[i] + 1 if i in m else 1
        for i in m:
            if m[i] % 2 == 0:
                count += m[i]
            else:
                if not use:
                    count += 1
                    use = True
                count += m[i] - 1
        return count



a = Solution().longestPalindrome("aabccccdd")
print(a)

# leetcode submit region end(Prohibit modification and deletion)
