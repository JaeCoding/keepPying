def minMalwareSpread(graph, initial):
    # 导入必要的库
    from collections import deque

    def bfs(start, blocked):
        """使用BFS方法计算从起点开始的感染节点数量，并记录访问过的节点"""
        queue = deque([start])
        visited = set([start])
        count = 1  # 起始节点已被感染
        while queue:
            node = queue.popleft()
            for neighbor in range(len(graph)):
                if graph[node][neighbor] == 1 and neighbor not in visited and neighbor != blocked:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    count += 1
        return count, visited

    # 初始节点按照索引排序
    initial.sort()

    # 计算不移除任何节点时的感染总数
    total_infected = set()
    for node in initial:
        if node not in total_infected:
            _, infected = bfs(node, -1)
            total_infected.update(infected)

    min_infected = len(total_infected)
    result = initial[0]

    # 对每个初始感染节点尝试移除，查看移除后的影响
    for node in initial:
        current_infected = 0
        for other_node in initial:
            if other_node != node:
                if other_node not in total_infected:
                    count, infected = bfs(other_node, node)
                    total_infected.update(infected)
                    current_infected += count
                else:
                    current_infected += len(bfs(other_node, node)[1])

        # 计算移除当前节点后的感染数
        if current_infected < min_infected:
            min_infected = current_infected
            result = node

    return result


# 示例输入和输出
graph1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
initial1 = [0, 1]
output1 = minMalwareSpread(graph1, initial1)
assert output1 == 0, f"Expected 0 but got {output1}"

graph2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
initial2 = [0, 1]
output2 = minMalwareSpread(graph2, initial2)
assert output2 == 1, f"Expected 1 but got {output2}"

graph3 = [[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1], [0, 0, 1, 1]]
initial3 = [0, 1]
output3 = minMalwareSpread(graph3, initial3)
assert output3 == 1, f"Expected 1 but got {output3}"

output1, output2, output3
