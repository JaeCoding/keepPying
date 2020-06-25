# Given a 2D binary matrix filled with 0's and 1's, find the largest square cont
# aining only 1's and return its area. 
# 
#  Example: 
# 
#  
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
#  Related Topics 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    add = 1
                    flag = True
                    while flag:
                        for z in range(0, add + 1):
                            # 对于扩大后的多出一列 col
                            if i + add >= len(matrix) or j + z >= len(matrix[0]) or matrix[i + add][j + z] == '0':
                                flag = False
                                break
                            # 对于扩大后的多出一行 col
                            if i + z >= len(matrix) or j + add >= len(matrix[0]) or matrix[i + z][j + add] == '0':
                                flag = False
                                break
                        if flag:
                            add += 1
                    n = max(n, add)
        return n ** 2

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        if not matrix:
            return res
        # 多创建一行列 这样就不用处理第一行第一列的边界了
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                # -1 映射回去
                if matrix[i - 1][j - 1] == '1':
                    # 关键！ 如果左、上、左上都有值，那么此点可以扩大了，取三者最小者 + 1
                    if dp[i-1][j - 1] and dp[i-1][j] and dp[i][j-1]:
                        dp[i][j] = min(dp[i-1][j - 1], dp[i-1][j], dp[i][j-1]) + 1
                    else:
                        dp[i][j] = 1
                    res = max(res, dp[i][j])
        return pow(res, 2)





a = Solution().maximalSquare([["1", "1", "1", "1", "1", "1", "1", "1"],
                              ["1", "1", "1", "1", "1", "1", "1", "0"],
                              ["1", "1", "1", "1", "1", "1", "1", "0"],
                              ["1", "1", "1", "1", "1", "0", "0", "0"],
                              ["0", "1", "1", "1", "1", "0", "0", "0"]])

a = Solution().maximalSquare(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
a = Solution().maximalSquare([])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
