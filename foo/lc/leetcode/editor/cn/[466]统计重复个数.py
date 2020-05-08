# Define S = [s,n] as the string S which consists of n connected strings s. For 
# example, ["abc", 3] ="abcabcabc". 
#  On the other hand, we define that string s1 can be obtained from string s2 if
#  we can remove some characters from s2 such that it becomes s1. For example, “ab
# c” can be obtained from “abdbec” based on our definition, but it can not be obta
# ined from “acbbe”. 
#  You are given two non-empty strings s1 and s2 (each at most 100 characters lo
# ng) and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 
# and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S
# 2,M] can be obtained from S1. 
# 
#  Example:
#  
# Input:
# s1="acb", n1=4
# s2="ab", n2=2
# 
# Return:
# 2
#  
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:

        # dp[i] 表示s1和s2[i] 作为开头匹配时，下一个循环的s1会和s2的哪个索引作为开头匹配，同时也存储了能匹配到几个s2的末尾。
        dp = []
        for i in range(len(s2)):
            start = i
            cnt = 0
            for j in range(len(s1)):
                # 如果发现s1 中与 s2匹配的字符
                if s1[j] == s2[start]:
                    start += 1  #
                    if start == len(s2): # 能匹配到几个s2的末尾
                        start = 0
                        cnt += 1
            dp.append((start, cnt)) # 添加(下一次开头匹配的s2位置，与能匹配到几个s2的末尾）
        res = 0
        next = 0
        for _ in range(n1):
            res += dp[next][1]
            next = dp[next][0]
        return res // n2

a = Solution().getMaxRepetitions("abaacdabc",4,"adcbd",2)
# leetcode submit region end(Prohibit modification and deletion)
