from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:

        s = set()
        for i in range(n):
            s.add(i)

        for item in edges:
            from1 = item[0]
            to = item[1]
            if to in s:
                s.remove(to)
        return list(s)

a = Solution().findSmallestSetOfVertices(5, [[0,1],[2,1],[3,1],[1,4],[2,4]])
print(a)