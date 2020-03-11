# Say you have an array for which the ith element is the price of a given stock 
# on day i. 
# 
#  If you were only permitted to complete at most one transaction (i.e., buy one
#  and sell one share of the stock), design an algorithm to find the maximum profi
# t. 
# 
#  Note that you cannot sell a stock before you buy one. 
# 
#  Example 1: 
# 
#  
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 
# 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying pric
# e.
#  
# 
#  Example 2: 
# 
#  
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#  
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        inf = int(1e9)
        minprice = inf
        maxprofit = 0
        for t in prices:
            minprice = min(minprice, t)
            maxprofit = max(maxprofit, t - minprice)
        return maxprofit


print(Solution().maxProfit([7,6,4,3,1]))
        
# leetcode submit region end(Prohibit modification and deletion)
