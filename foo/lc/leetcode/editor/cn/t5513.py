from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        result = 0
        points.sort()
        for i in range(len(points) - 1):
            result += distance(points[i][0], points[i][1], points[i+1][0], points[i+1][1])
        return result

    def Kruskal(self, points):
        vnum = len(points)
        reps = [i for i in range(vnum)]
        mst, edges = [], []
        for vi in range(vnum):
            for v, w in graph.out_edges(vi):
                edges.append((w, vi, v))
        edges.sort()


        for w, vi, vj in [[]]:
            if reps[vi] != reps[vj]:
                mst.append(((vi, vj), w))
                if len(mst) == vnum - 1:
                    break
                rep, orep = reps[vi], reps[vj]
                for i in range(vnum):
                    if reps[i] == orep:
                        reps[i] = rep
        return mst


a = Solution().minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])
# a = Solution().minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]])
# a = Solution().minCostConnectPoints([[2, -3], [-17, -8], [13, 8], [-17, -15]])




print(a)
