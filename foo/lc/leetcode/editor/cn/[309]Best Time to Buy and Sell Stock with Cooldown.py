# Say you have an array for which the ith element is the price of a given stock 
# on day i. 
# 
#  Design an algorithm to find the maximum profit. You may complete as many tran
# sactions as you like (ie, buy one and sell one share of the stock multiple times
# ) with the following restrictions: 
# 
#  
#  You may not engage in multiple transactions at the same time (ie, you must se
# ll the stock before you buy again). 
#  After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 
# day) 
#  
# 
#  Example: 
# 
#  
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#  Related Topics 动态规划 
#  👍 458 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        # f[i][0]: 手上持有股票的最大收益
        # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
        # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益
        # 因为上来就默认买股票，其实是亏纯收益的（股票不算钱），并且只有在卖掉股票的时候才会收钱
        f = [[-prices[0], 0, 0]] + [[0] * 3 for _ in range(n - 1)]
        for i in range(1, n):
            # 此阶段持有股票 = max(上阶段持有股票且本期不卖， 上阶段未冻结可买且买入当期（亏钱）)
            f[i][0] = max(f[i - 1][0], f[i - 1][2] - prices[i])
            # 此阶段卖出变成冻结 = 上期持有 + 本期卖出（挣钱）
            f[i][1] = f[i - 1][0] + prices[i]
            # 此阶段未冻结 = 上期未冻结 or 上期卖了为冻结
            f[i][2] = max(f[i - 1][1], f[i - 1][2])

        return max(f[n - 1][1], f[n - 1][2])


a = Solution().maxProfit([1, 2, 3, 0, 2])
print(a)
