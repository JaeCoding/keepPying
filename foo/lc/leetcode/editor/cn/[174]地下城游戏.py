# 
# 
#  一些恶魔抓住了公主（P）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（K）最初被安置在左上角的房间里，他必须穿
# 过地下城并通过对抗恶魔来拯救公主。 
# 
#  骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。 
# 
#  有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为负整数，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 0），要么
# 包含增加骑士健康点数的魔法球（若房间里的值为正整数，则表示骑士将增加健康点数）。 
# 
#  为了尽快到达公主，骑士决定每次只向右或向下移动一步。 
# 
#  
# 
#  编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。 
# 
#  例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 右 -> 右 -> 下 -> 下，则骑士的初始健康点数至少为 7。 
# 
#  
#  
#  -2 (K) 
#  -3 
#  3 
#  
#  
#  -5 
#  -10 
#  1 
#  
#  
#  10 
#  30 
#  -5 (P) 
#  
#  
# 
# 
#  
# 
#  说明: 
# 
#  
#  
#  骑士的健康点数没有上限。 
#  
#  任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。 
#  Related Topics 二分查找 动态规划 
#  👍 280 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        m, n = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 设dp[i][j] 为，计算本格(i,j)前的最少血量
        # 采用逆推法，假设在扣减完最后一格后，只剩下1点血， 为了防止最后是正数，所以要与1取最大值，这样若最后一格是正数，那么必然dp值为1
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # 最后一格不参与dp
                if i == m - 1 and j == n - 1:
                    continue
                # 逆推，若来自下方。 dp = dp下方 - 当前格子值（负数扣血，则会让初始血量增多，正数加血，会让初始血量减少），至少留有1点血
                down = max(1, dp[i + 1][j] - dungeon[i][j]) if i + 1 < m else 10000000000
                right = max(1, dp[i][j + 1] - dungeon[i][j]) if j + 1 < n else 10000000000
                dp[i][j] = min(down, right)
        return dp[0][0]


a = Solution().calculateMinimumHP([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
