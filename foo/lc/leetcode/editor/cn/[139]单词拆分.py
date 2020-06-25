# Given a non-empty string s and a dictionary wordDict containing a list of non-
# empty words, determine if s can be segmented into a space-separated sequence of 
# one or more dictionary words. 
# 
#  Note: 
# 
#  
#  The same word in the dictionary may be reused multiple times in the segmentat
# ion. 
#  You may assume the dictionary does not contain duplicate words. 
#  
# 
#  Example 1: 
# 
#  
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
#  
# 
#  Example 2: 
# 
#  
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pe
# n apple".
#              Note that you are allowed to reuse a dictionary word.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        contain = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        # dp[i] 表示 0 - i 在拆分后，能找到
        for i in range(1, len(dp)):
            base = False
            for j in range(0, i):
                if dp[j] and s[j:i] in contain:
                    base = True
                    break
            dp[i] = base
        return dp[-1]





# a = Solution().wordBreak("leetcode", ["leet", "code"])
a = Solution().wordBreak("aaaaaaa", ["aaaa","aaa"])
print(a)
# leetcode submit region end(Prohibit modification and deletion)
