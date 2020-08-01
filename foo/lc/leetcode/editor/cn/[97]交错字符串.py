# -*- coding: utf-8 -*-

# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。
# 
#  示例 1: 
# 
#  输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false 
#  Related Topics 字符串 动态规划 
#  👍 288 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 == "" or s2 == "":
            return s2 == s3 or s1 == s3
        dp = [[False for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                # starting point
                if i == 0 and j == 0:
                    dp[i][j] = True
                    continue
                f1, f2 = False, False
                # j 控制内循环 s1
                if j - 1 >= 0 and s3[i + j - 1] == s1[j - 1]:
                    f1 = dp[i][j - 1]
                # i 控制外循环 s2
                if i - 1 >= 0 and s3[i + j - 1] == s2[i - 1]:
                    f2 = dp[i - 1][j]
                dp[i][j] = False or f1 or f2

        return dp[len(s2)][len(s1)]

# a = Solution().isInterleave("aabcc","dbbca","aadbbcbcac")
a = Solution().isInterleave("db","b","cbb")
# a = Solution().isInterleave("a","","a")
print(a)
# leetcode submit region end(Prohibit modification and deletion)
