# Given a m x n grid. Each cell of the grid represents a street. The street of g
# rid[i][j] can be:
#  
#  1 which means a street connecting the left cell and the right cell. 
#  2 which means a street connecting the upper cell and the lower cell. 
#  3 which means a street connecting the left cell and the lower cell. 
#  4 which means a street connecting the right cell and the lower cell. 
#  5 which means a street connecting the left cell and the upper cell. 
#  6 which means a street connecting the right cell and the upper cell. 
#  
# 
#  
# 
#  You will initially start at the street of the upper-left cell (0,0). A valid 
# path in the grid is a path which starts from the upper left cell (0,0) and ends 
# at the bottom-right cell (m - 1, n - 1). The path should only follow the streets
# . 
# 
#  Notice that you are not allowed to change any street. 
# 
#  Return true if there is a valid path in the grid or false otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: grid = [[2,4,3],[6,5,2]]
# Output: true
# Explanation: As shown you can start at cell (0, 0) and visit all the cells of 
# the grid to reach (m - 1, n - 1).
#  
# 
#  Example 2: 
# 
#  
# Input: grid = [[1,2,1],[1,2,1]]
# Output: false
# Explanation: As shown you the street at cell (0, 0) is not connected with any 
# street of any other cell and you will get stuck at cell (0, 0)
#  
# 
#  Example 3: 
# 
#  
# Input: grid = [[1,1,2]]
# Output: false
# Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2
# ).
#  
# 
#  Example 4: 
# 
#  
# Input: grid = [[1,1,1,1,1,1,3]]
# Output: true
#  
# 
#  Example 5: 
# 
#  
# Input: grid = [[2],[2],[2],[2],[2],[2],[6]]
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  1 <= grid[i][j] <= 6 
#  
#  Related Topics 深度优先搜索 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # value 为对应方向的 可连接道路
        accept = {'up': [2, 3, 4],
                  'down': [2, 5, 6],
                  'left': [1, 4, 6],
                  'right': [1, 3, 5]
        }
        # value 为对应道路的 后续可连接方向
        directions = {
            1: ['left', 'right'],
            2: ['up', 'down'],
            3: ['left', 'down'],
            4: ['right', 'down'],
            5: ['left', 'up'],
            6: ['right', 'up'],
        }
        m = len(grid)
        n = len(grid[0])
        stack = []
        stack.append((0, 0))

        def solve(direction: str, row: int, col: int):
            if direction == 'left':
                col -= 1
            elif direction == 'right':
                col += 1
            elif direction == 'up':
                row -= 1
            elif direction == 'down':
                row += 1
            if 0 <= row < m and 0 <= col < n and grid[x][y] != -1 and grid[row][col] in accept[direction]:
                stack.append((row, col))

        while stack:
            (x, y) = stack.pop()
            if x == m - 1 and y == n - 1:
                return True
            # 当前道路类型
            way = grid[x][y]
            grid[x][y] = -1
            # 对当前道路类型 的 后续方向进行迭代
            for direction in directions[way]:
                solve(direction, x, y)
        return False

class Solution2:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        # value 为对应方向的 可连接道路
        dir = {1: [(0, 1), (0, -1)],
               2: [(1, 0), (-1, 0)],
               3: [(1, 0), (0, -1)],
               4: [(0, 1), (1, 0)],
               5: [(0, -1), (-1, 0)],
               6: [(0, 1), (-1, 0)]}
        m = len(grid)
        n = len(grid[0])
        x, y = 0, 0
        from collections import deque
        queue = deque([(x, y)])

        while queue:
            (x, y) = queue.popleft()
            for dx, dy in dir[grid[x][y]]:
                # 下一节点位置 = 原坐标 + 坐标变化情况
                nx, ny = x + dx, y + dy
                # boundary and not visited
                if 0 <= nx <m and 0 <= ny <n and grid[nx][ny] != -1:
                    # 校验连通性
                    for ndx, ndy in dir[grid[nx][ny]]:
                        # 关键点！！！ 若当前点的变化率与下一点的变化率互补！则连通成立！！
                        if ndx + dx == 0 and ndy + dy == 0:
                            if nx == m - 1 and ny == n - 1:
                                return True
                            queue.append((nx, ny))
            grid[x][y] = -1
            # 对当前道路类型 的 后续方向进行迭代
        return False

a = Solution().hasValidPath([[1,2,1],[1,2,1]])
a = Solution().hasValidPath([[1,1,1,1,1,1,3]])
a = Solution2().hasValidPath([[2,4,3],[6,5,2]])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
