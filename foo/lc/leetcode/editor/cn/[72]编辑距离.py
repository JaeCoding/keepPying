# Given two words word1 and word2, find the minimum number of operations require
# d to convert word1 to word2. 
# 
#  You have the following 3 operations permitted on a word: 
# 
#  
#  Insert a character 
#  Delete a character 
#  Replace a character 
#  
# 
#  Example 1: 
# 
#  
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#  
# 
#  Example 2: 
# 
#  
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(len(word2) + 1):
            dp[0][i] = i
        for i in range(len(word1) + 1):
            dp[i][0] = i

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                # i与j位相同：hor->ror等价等价ho->ro  翻译：dp[i][j]=dp[i-1][j-1]
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 增操作：添加j字符。 hor->ro等价horo->ro等价hor->r  翻译：dp[i][j]=dp[i][j-1]
                    plus = dp[i][j - 1] + 1
                    # 减操作：删除i字符。 hor->ro等价ho->ro  翻译：dp[i][j]=dp[i-1][j]
                    minus = dp[i - 1][j] + 1
                    # 替换操作：i字符替换为j字符。 hor->ro等价hoo->ro等价ho->r  翻译：dp[i][j]=dp[i-1][j-1]
                    exchange = dp[i - 1][j - 1] + 1
                    dp[i][j] = min(plus, minus, exchange)
        return dp[len(word1)][len(word2)]

a = Solution().minDistance("", "execution")
print(a)
# leetcode submit region end(Prohibit modification and deletion)
