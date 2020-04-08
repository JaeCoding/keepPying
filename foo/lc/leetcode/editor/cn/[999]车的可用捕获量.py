# On an 8 x 8 chessboard, there is one white rook. There also may be empty squar
# es, white bishops, and black pawns. These are given as characters 'R', '.', 'B',
#  and 'p' respectively. Uppercase characters represent white pieces, and lowercas
# e characters represent black pieces. 
# 
#  The rook moves as in the rules of Chess: it chooses one of four cardinal dire
# ctions (north, east, west, and south), then moves in that direction until it cho
# oses to stop, reaches the edge of the board, or captures an opposite colored paw
# n by moving to the same square it occupies. Also, rooks cannot move into the sam
# e square as other friendly bishops. 
# 
#  Return the number of pawns the rook can capture in one move. 
# 
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],["
# .",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".","
# .",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".","
# .","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation: 
# In this example the rook is able to capture all the pawns.
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],["
# .","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","
# B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".","
# .","."],[".",".",".",".",".",".",".","."]]
# Output: 0
# Explanation: 
# Bishops are blocking the rook to capture any pawn.
#  
# 
#  Example 3: 
# 
#  
# 
#  
# Input: [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],["
# .",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".","
# .",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".","
# .","."],[".",".",".",".",".",".",".","."]]
# Output: 3
# Explanation: 
# The rook can capture the pawns at positions b5, d6 and f5.
#  
# 
#  
# 
#  Note: 
# 
#  
#  board.length == board[i].length == 8 
#  board[i][j] is either 'R', '.', 'B', or 'p' 
#  There is exactly one cell with board[i][j] == 'R' 
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        count = 0
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 'R':
                    # 上 下 左 右
                    for m in range(i-1, -1, -1):
                        if board[m][j] != '.':
                            count += 1 if board[m][j] == 'p' else 0
                            break
                    for m in range(i+1, len(board)):
                        if board[m][j] != '.':
                            count += 1 if board[m][j] == 'p' else 0
                            break
                    for m in range(j - 1, -1, -1):
                        if board[i][m] != '.':
                            count += 1 if board[i][m] == 'p' else 0
                            break
                    for m in range(j + 1, len(board[0])):
                        if board[i][m] != '.':
                            count += 1 if board[i][m] == 'p' else 0
                            break
                    return count


a = Solution().numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]])

# leetcode submit region end(Prohibit modification and deletion)
