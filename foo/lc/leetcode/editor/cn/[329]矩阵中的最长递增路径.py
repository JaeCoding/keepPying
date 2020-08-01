# 给定一个整数矩阵，找出最长递增路径的长度。 
# 
#  对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。 
# 
#  示例 1: 
# 
#  输入: nums = 
# [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径为 [1, 2, 6, 9]。 
# 
#  示例 2: 
# 
#  输入: nums = 
# [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
#  
#  Related Topics 深度优先搜索 拓扑排序 记忆化 
#  👍 276 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[-100000 for _ in range(n)] for _ in range(m)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        max_total = -100000
        select = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i_in, j_in, base_value) -> int:
            add_value = 0
            visited[i_in][j_in] = True
            for (i_add, j_add) in select:
                i_next, j_next = i_in + i_add, j_in + j_add
                # 若下一位置在范围内 且未访问 且比当前位置大
                if 0 <= i_next < m and 0 <= j_next < n and not visited[i_next][j_next] and matrix[i_next][j_next] > matrix[i_in][j_in]:
                    if dp[i_next][j_next] != -100000:
                        # 已经计算出了 该位置的dp值 直接借用
                        add_value = max(add_value, dp[i_next][j_next])
                    else:
                        # 下位置没有计算过， 则计算之
                        add_value = max(add_value, dfs(i_next, j_next, base_value))
            visited[i_in][j_in] = False
            dp[i_in][j_in] = base_value + add_value
            return base_value + add_value

        for i in range(m):
            for j in range(n):
                i_j = dfs(i, j, 1)
                max_total = max(i_j, max_total)
        return max_total

a = Solution().longestIncreasingPath([
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
])
print(a)




        
# leetcode submit region end(Prohibit modification and deletion)
