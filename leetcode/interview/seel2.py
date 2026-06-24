from collections import deque


class MyTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_node_in_k(root, target, len):
    # Add the mapping of each node
    parent_map = {}

    def add_parent(node, parent):
        if node:
            parent_map[node] = parent
            add_parent(node.left, node)
            add_parent(node.right, node)

    add_parent(root, None)

    # BFS from node
    queue = deque()
    queue.append([target, 0])
    visited = {target}
    while queue:
        # Return condition: the depth is len
        if queue[0][1] == len:
            return [node.val for node, depth in queue]

        node, depth = queue.popleft()
        for next in (node.left, node.right, parent_map[node]):
            if next and next not in visited:
                visited.add(next)
                queue.append((next, depth + 1))
    return []


root = MyTreeNode(3)
root.left = MyTreeNode(5)
root.right = MyTreeNode(1)
root.left.left = MyTreeNode(6)
root.left.right = MyTreeNode(2)
root.left.right.left = MyTreeNode(7)
root.left.right.right = MyTreeNode(4)

root.right.left = MyTreeNode(0)
root.right.right = MyTreeNode(8)

result = find_node_in_k(root, root.left, 2)
print(result)
