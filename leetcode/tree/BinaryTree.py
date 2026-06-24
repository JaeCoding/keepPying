class TreeNode:
    # 树节点的定义
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree_from_list(lst):
    # 空数组情况
    if not lst:
        return None
    # 初始化根节点和队列
    root = TreeNode(lst[0])
    queue = [root]
    i = 1  # 数组索引
    # 按层构造树
    while i < len(lst):
        current = queue.pop(0)  # 当前父节点
        if lst[i] is not None:  # 左子节点
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:  # 右子节点
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root

# 层序遍历函数，用于验证构建的二叉树
def level_order_traversal_with_null(root):
    if not root:
        return []
    result, queue = [], [root]
    while any(queue):  # 当队列中有非空节点时继续遍历
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            if node:
                level.append(node.val)
                # 即使子节点为空也加入队列，用于保持树的完整结构
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)
        result.extend(level)  # 将本层结果加入最终结果，而不是作为子列表
    # 去除末尾的None值，这些值代表超出原始树深度的额外层
    while result and result[-1] is None:
        result.pop()
    return result

# 构造二叉树并进行层序遍历以验证
tree = construct_binary_tree_from_list([7, 4, 3, None, None, 6, 19])
print(level_order_traversal_with_null(tree))
