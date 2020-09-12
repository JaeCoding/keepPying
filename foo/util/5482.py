from typing import List
import sys

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:


        sys.setrecursionlimit(1000000)  # 表示递归深度为100w

        visited = set()
        to_next = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(x_in, y_in, value, from1):
            visited.add((x_in, y_in))
            for (x_add, y_add) in to_next:
                x_next, y_next = x_in + x_add, y_in + y_add
                if 0 <= x_next < len(grid) and 0 <= y_next < len(grid[0]) and grid[x_next][y_next] == value:
                    # 如果访问过
                    if (x_next, y_next) in visited:
                        if (x_next, y_next) != from1:
                            return True
                        else:
                            continue
                    # 递归
                    if dfs(x_next, y_next, value, (x_in, y_in)):
                        return True
            visited.remove((x_in, y_in))
            return False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if dfs(x, y, grid[x][y], (x, y)):
                    return True
        return False



    def containsCycle2(self, grid: List[List[str]]) -> bool:

        visited = set()
        to_next = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        stack = []
        def dfs(x_in, y_in, value, from1):
            visited.clear()
            stack.append((x_in, y_in))
            while len(stack) > 0:
                # 对于四个方向
                flag = True
                for (x_add, y_add) in to_next:
                    if flag:
                        x_in, y_in = stack.pop()
                        flag = False
                    visited.add((x_in, y_in))
                    x_next, y_next = x_in + x_add, y_in + y_add
                    if 0 <= x_next < len(grid) and 0 <= y_next < len(grid[0]) and grid[x_next][y_next] == value:
                        # 如果访问过
                        if (x_next, y_next) in visited:
                            if (x_next, y_next) != from1:
                                return True
                            else:
                                continue
                        # 满足，则加入栈，下一个弹出其，作为下一个点
                        stack.append((x_next, y_next))
                        from1 = (x_in, y_in)
                        flag = True
                return False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if dfs(x, y, grid[x][y], (x, y)):
                    return True
        return False


# a = Solution().containsCycle2([["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]])
# a = Solution().containsCycle2([["a","b","b"],["b","z","b"],["b","b","a"]])
a = Solution().containsCycle2([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]])
print(a)
