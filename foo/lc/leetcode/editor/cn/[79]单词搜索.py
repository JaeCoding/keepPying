# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例: 
# 
#  board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false 
# 
#  
# 
#  提示： 
# 
#  
#  board 和 word 中只包含大写和小写英文字母。 
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  1 <= word.length <= 10^3 
#  
#  Related Topics 数组 回溯算法 
#  👍 604 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        to = [(-1,0), (1,0), (0, -1), (0, 1)]
        def dfs(x_in, y_in, visited, index):
            # 如果字符不同，直接返回不可
            if word[index] != board[x_in][y_in]:
                return False
            # 如果长度已满足
            if index + 1 == len(word):
                return True
            visited.append((x_in, y_in))
            for to_x, to_y in to:
                x_next = x_in + to_x
                y_next = y_in + to_y
                if 0 <= x_next < len(board) and 0 <= y_next < len(board[0]) and (x_next, y_next) not in visited and index + 1 < len(word):
                    if dfs(x_next, y_next, visited, index + 1):
                        return True
            visited.pop()
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, [], 0):
                    return True
        return False


# a = Solution().exist([
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ], "ABCESEEEFS")
# ], "ABCCED")
# ], "SEE")
# ], "ABCB")

# a = Solution().exist([["a"]], "a")
# a = Solution().exist([["a","b"]], "aa")
a = Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS")

print(a)
# leetcode submit region end(Prohibit modification and deletion)
