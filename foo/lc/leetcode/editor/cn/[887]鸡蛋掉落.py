# You are given K eggs, and you have access to a building with N floors from 1 t
# o N. 
# 
#  Each egg is identical in function, and if an egg breaks, you cannot drop it a
# gain. 
# 
#  You know that there exists a floor F with 0 <= F <= N such that any egg dropp
# ed at a floor higher than F will break, and any egg dropped at or below floor F 
# will not break. 
# 
#  Each move, you may take an egg (if you have an unbroken one) and drop it from
#  any floor X (with 1 <= X <= N). 
# 
#  Your goal is to know with certainty what the value of F is. 
# 
#  What is the minimum number of moves that you need to know with certainty what
#  F is, regardless of the initial value of F? 
# 
#  
# 
#  
#  
# 
#  
#  Example 1: 
# 
#  
# Input: K = 1, N = 2
# Output: 2
# Explanation: 
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty th
# at F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with certainty.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: K = 2, N = 6
# Output: 3
#  
# 
#  
#  Example 3: 
# 
#  
# Input: K = 3, N = 14
# Output: 4
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= K <= 100 
#  1 <= N <= 10000 
#  
#  
#  
#  
#  Related Topics 数学 二分查找 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # K个蛋 N层
    def superEggDrop(self, K: int, N: int) -> int:

        # 一个蛋 或者 一层 直接返回层数
        if K == 1 or N == 1:
            return N
        # 行：层数  列：蛋数
        dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
        # 当K=1,此列解等于行：因为只能从第一层往上试，最坏情况要N次
        for i in range(N + 1):
            dp[i][1] = i
        # 当F=1,此行解等于1，因为只需要试一次
        for i in range(1,K + 1):
            dp[1][i] = 1

        # 外层：蛋的数量   内层：层数
        for i in range(2, K + 1):
            for j in range(2, N + 1):
                # dp[j][i] = min{ max(dp[k-1][i-1], dp[N-k][i]) + 1 }   1 <= k <= N
                min_step = 100000000000000000000
                # 注意：这里j作为当前的N而存在
                for k in range(1, j + 1):
                    # k层破：dp[k-1][i-1]   k层没破：dp[N - k][i]   加一是因为操作了一次,取最大值因为 问题是求最坏情况下的次数
                    break_or_not = max(dp[k - 1][i - 1], dp[j - k][i]) + 1
                    min_step = min(min_step, break_or_not)
                dp[j][i] = min_step

        return dp[N][K]

a = Solution().superEggDrop(2,100)
print(a)




        
# leetcode submit region end(Prohibit modification and deletion)
