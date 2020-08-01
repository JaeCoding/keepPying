# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。 
# 
#  现在要求你戳破所有的气球。如果你戳破气球 i ，就可以获得 nums[left] * nums[i] * nums[right] 个硬币。 这里的 lef
# t 和 right 代表和 i 相邻的两个气球的序号。注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。 
# 
#  求所能获得硬币的最大数量。 
# 
#  说明: 
# 
#  
#  你可以假设 nums[-1] = nums[n] = 1，但注意它们不是真实存在的所以并不能被戳破。 
#  0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100 
#  
# 
#  示例: 
# 
#  输入: [3,1,5,8]
# 输出: 167 
# 解释: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#      coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#  
#  Related Topics 分治算法 动态规划 
#  👍 423 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        points = [1] + nums + [1]
        # （首尾引入了两个虚拟气球）
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        # 定义dp[i][j]为 戳破(i,j) 之间的所有气球，(i,j)之间气球能获得多少硬币，开区间
        # 目标dp[0][len + 1] （因为首尾引入了两个虚拟气球）
        # 当 i + 1 == j 时，dp[i][j] 必然为0，因为是开区间，中间没有任何可以戳破
        for i in range(n, -1, -1):
            for j in range(i + 1, n + 2):
                # 因为是开区间，k取 (i,j),  也就是[i+1, j-1] 之间。 找寻最大值
                for k in range(i + 1, j):
                    # 状态转移 因为是戳破i,j 内所有气球，所以k的前一个是i，后一个是j.(而不是k-1与k+1,因为可能已经破了）
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + points[i] * points[k] * points[j])
        return dp[0][-1]

a = Solution().maxCoins([3, 1, 5, 8])


# leetcode submit region end(Prohibit modification and deletion)
