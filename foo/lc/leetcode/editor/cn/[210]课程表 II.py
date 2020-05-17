# There are a total of n courses you have to take, labeled from 0 to n-1. 
# 
#  Some courses may have prerequisites, for example to take course 0 you have to
#  first take course 1, which is expressed as a pair: [0,1] 
# 
#  Given the total number of courses and a list of prerequisite pairs, return th
# e ordering of courses you should take to finish all courses. 
# 
#  There may be multiple correct orders, you just need to return one of them. If
#  it is impossible to finish all courses, return an empty array. 
# 
#  Example 1: 
# 
#  
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you shou
# ld have finished   
#              course 0. So the correct course order is [0,1] . 
# 
#  Example 2: 
# 
#  
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you shou
# ld have finished both     
#              courses 1 and 2. Both courses 1 and 2 should be taken after you f
# inished course 0. 
#              So one correct course order is [0,1,2,3]. Another correct orderin
# g is [0,2,1,3] . 
# 
#  Note: 
# 
#  
#  The input prerequisites is a graph represented by a list of edges, not adjace
# ncy matrices. Read more about how a graph is represented. 
#  You may assume that there are no duplicate edges in the input prerequisites. 
# 
#  
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # 三色标记法 0表示未访问 1表示访问过但是未访问完毕 2表示完全访问完毕
        visited = [0] * numCourses
        pre_node = [[] for _ in range(numCourses)]  # 这样创建的数组才是独立的
        res = []

        def dfs(node: int) -> bool:
            if visited[node] == 1:
                return False  # 表示走到了 访问过但是未访问完毕的点， 说明发现了环
            elif visited[node] == 2:
                return True
            visited[node] = 1
            # 如果节点有后续节点 则进行DFS，否则则标记并学习
            for i in pre_node[node]:
                if not dfs(i):  # 如果发现环，递归返回
                    return False
                # 没发现环 正常递归
            visited[node] = 2
            res.append(node)
            return True

        for cur, pre in prerequisites:
            # 记录每个点的后续节点，用于DFS
            pre_node[cur].append(pre)

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res

a = Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
