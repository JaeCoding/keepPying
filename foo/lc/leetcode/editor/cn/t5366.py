from typing import List


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        m = len(grid)
        n = len(grid[0])
        row, col = 0, 0
        # 上下左右1234
        reach = set()

        def dfs(row_now, col_now, come:set) -> bool:

            # 必须与上一道路拼接上
            if row_now < 0 or row_now >= m or col_now < 0 or col_now >= n:
                return False
            if (row_now, col_now) in reach:
                return False
            direction = grid[row_now][col_now]

            if come == "up" and (direction != 3 and direction != 4 and direction != 2):
                return False
            elif come == "down" and (direction != 5 and direction != 6 and direction != 2):
                return False
            elif come == "left" and (direction != 1 and direction != 4 and direction != 6):
                return False
            elif come == "right" and (direction != 1 and direction != 3 and direction != 5):
                return False


            if row_now == m-1 and col_now == n-1:
                return True
            reach.add((row_now, col_now))

            if direction == 2:
                # 上下
                return dfs(row_now -1, col_now, "up") or dfs(row_now + 1, col_now, "down")
            elif direction == 1:
                # 左右
                return dfs(row_now, col_now-1, "left") or dfs(row_now, col_now+1, "right")
            elif direction == 3:
                # 左下
                return dfs(row_now, col_now - 1, "left") or dfs(row_now + 1, col_now, "down")
            elif direction == 4:
                # 右下
                return dfs(row_now, col_now+1, "right") or dfs(row_now + 1, col_now, "down")
            elif direction == 5:
                # 左上
                return dfs(row_now, col_now - 1, "left") or dfs(row_now -1, col_now, "up")
            elif direction == 6:
                # 右上
                return dfs(row_now, col_now+1, "right") or dfs(row_now -1, col_now, "up")
        return dfs(0,0,None)


# a = Solution().hasValidPath([[2,4,3],[6,5,2]])
a = Solution().hasValidPath([[1,2,1],[1,2,1]])
a = Solution().hasValidPath([[1,1,2]])
print(a)

