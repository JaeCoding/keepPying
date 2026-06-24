class Solution(object):
    def getAncestors(self, n, edges):
        # 初始化邻接表
        adjList = [[] for _ in range(n)]
        for frm, to in edges:
            adjList[to].append(frm)  # 反向建图

        # 使用DFS找到所有祖先
        def dfs(node):
            visited[node] = True
            for last_node in adjList[node]:
                if not visited[last_node]:
                    dfs(last_node)

        ancestors = [None] * n  # 存储每个节点的祖先
        for i in range(n):
            visited = [False] * n
            dfs(i)
            visited[i] = False  # 不包含当前节点
            ancestors[i] = [j for j, b in enumerate(visited) if b] # 对于 b 为 True的所有item， j为其index，而且自带有序的

        return ancestors


result = Solution().getAncestors(8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]])
# result = Solution().getAncestors(9, [[3,6],[2,4],[8,6],[7,4],[1,4],[2,1],[7,2],[0,4],[5,0],[4,6],[3,2],[5,6],[1,6]])
print(result)
