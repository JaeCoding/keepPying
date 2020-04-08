# Given an N x N grid containing only values 0 and 1, where 0 represents water a
# nd 1 represents land, find a water cell such that its distance to the nearest la
# nd cell is maximized and return the distance. 
# 
#  The distance used in this problem is the Manhattan distance: the distance bet
# ween two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|. 
# 
#  If no land or water exists in the grid, return -1. 
# 
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: 
# The cell (1, 1) is as far as possible from all the land with distance 2.
#  
# 
#  Example 2: 
# 
#  
# 
#  
# Input: [[1,0,0],[0,0,0],[0,0,0]]
# Output: 4
# Explanation: 
# The cell (2, 2) is as far as possible from all the land with distance 4.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= grid.length == grid[0].length <= 100 
#  grid[i][j] is 0 or 1 
#  
#  Related Topics 广度优先搜索 图


# leetcode submit region begin(Prohibit modification and deletion)
import queue
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        def dis(row, col) -> int:
            q = queue.Queue()
            q.put((row, col, 0))
            visit = set()
            visit.add((row, col))  # simplify?
            while not q.empty():
                (row_now, col_now, distance) = q.get()
                # 上 若上为0
                if row_now - 1 >= 0 and (row_now - 1, col_now) not in visit:
                    if grid[row_now - 1][col_now] == 0:
                        q.put((row_now - 1, col_now, distance + 1))
                        visit.add((row_now - 1, col_now))
                    else:
                        return distance + 1
                # down
                if row_now + 1 < len(grid) and (row_now + 1, col_now) not in visit:
                    if grid[row_now + 1][col_now] == 0:
                        q.put((row_now + 1, col_now, distance + 1))
                        visit.add((row_now + 1, col_now))
                    else:
                        return distance + 1
                # left
                if col_now - 1 >= 0 and (row_now, col_now - 1) not in visit:
                    if grid[row_now][col_now - 1] == 0:
                        q.put((row_now, col_now - 1, distance + 1))
                        visit.add((row_now, col_now - 1))
                    else:
                        return distance + 1
                # right
                if col_now + 1 < len(grid[0]) and (row_now, col_now + 1) not in visit:
                    if grid[row_now][col_now + 1] == 0:
                        q.put((row_now, col_now + 1, distance + 1))
                        visit.add((row_now, col_now + 1))
                    else:
                        return distance + 1
            return -1

        m = -1
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 0:
                    m = max(m, dis(i, j))
        return m


class Solution2:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        steps = -1
        # 将所有陆地依次加入到队列
        queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        # 全为1或者全为0
        if len(queue) == 0 or len(queue) == n ** 2:
            return steps
        while len(queue) > 0:
            # 每次循环掉当前队列的元素（含义是 每一轮就是一次距离的迭代，从每个陆地开始向四周扩散
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                # 对于上下左右
                for xi, yj in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    # 如果是0，加入队列，并且标记位置为-1
                    if xi >= 0 and xi < n and yj >= 0 and yj < n and grid[xi][yj] == 0:
                        queue.append((xi, yj))
                        grid[xi][yj] = -1
            steps += 1

        return steps

    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        step = 0
        queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        if len(queue) == 0 or len(queue) == n ** 2:
            return False
        while len(queue) > 0:
            x, y = queue.pop()
            # 从队列每个点开始扩散，至海洋
            for _ in range(len(queue)):
                for xi, yi in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if xi >= 0 and xi < n and yi >= 0 and yi < n and grid[xi][yi] == 0:
                        queue.append((xi, yi))
                        # 将位置标记成已访问
                        grid[xi][yi] = -1
            step += 1
            # 多计算了一次 减去1
        return step-1



# a = Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
# a = Solution().maxDistance([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
a = Solution().maxDistance([[0, 0], [0, 0]])
a = Solution().maxDistance([[1, 1], [1, 1]])
# a = Solution().maxDistance([[1,0,1],[0,0,0],[1,0,1]])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
