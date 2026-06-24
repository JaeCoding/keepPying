def minMalwareSpread(graph, initial):
    from collections import defaultdict, deque

    def bfs(start, blocked, infected):
        # 创建队列并将起始节点加入队列
        queue = deque([start])
        # 创建访问集合并标记起始节点为已访问
        visited = set([start])
        # 初始化感染计数器
        count = 0
        # 广度优先搜索
        while queue:
            node = queue.popleft()
            # 如果当前节点是感染节点，增加计数器
            if node in infected:
                count += 1
            # 遍历所有邻居节点
            for neighbor in range(len(graph[node])):
                # 如果邻居未访问，且与当前节点有连接，且不是被阻塞的节点，则加入队列继续搜索
                if neighbor not in visited and graph[node][neighbor] == 1 and neighbor != blocked:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return count

    # 初始化初始感染节点集合
    initial_set = set(initial)
    # 获取图中的节点总数
    n = len(graph)
    # 初始化最小感染节点数为无限大
    min_infected = float('inf')
    # 初始化最佳节点为-1
    best_node = -1

    # 对初始感染的每个节点尝试移除，并计算移除后的感染节点数
    for node in sorted(initial):  # 排序保证优先返回索引最小的节点
        # 计算移除节点后的感染节点数
        infected_count = bfs(node, node, initial_set)
        # 如果当前计算的感染节点数更少，更新最佳节点和最小感染数
        if infected_count < min_infected:
            min_infected = infected_count
            best_node = node

    return best_node

# 测试示例
graph1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
initial1 = [0, 1]
result1 = minMalwareSpread(graph1, initial1)

graph2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
initial2 = [0, 1]
result2 = minMalwareSpread(graph2, initial2)

graph3 = [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]]
initial3 = [0, 1]
result3 = minMalwareSpread(graph3, initial3)

print(result1)
print(result2)
print(result3)
