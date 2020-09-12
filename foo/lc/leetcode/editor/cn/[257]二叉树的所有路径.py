# 给定一个二叉树，返回所有从根节点到叶子节点的路径。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 
#  输入:
# 
#    1
#  /   \
# 2     3
#  \
#   5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3 
#  Related Topics 树 深度优先搜索 
#  👍 350 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from foo.lc.TreeNode import TreeNode
from foo.lc.TreeUtil import TreeUtil


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        result = []
        def bfs(node: TreeNode, s: str):
            ns = s + str(node.val)
            if not node.left and not node.right:
                result.append(ns)
            if node.left:
                bfs(node.left, ns + '->')
            if node.right:
                bfs(node.right, ns + '->')
        if root:
            bfs(root, '')
        return result

root = TreeUtil.creat_tree([1,2,3,'null',5])
a = Solution().binaryTreePaths(root)
print(a)

# leetcode submit region end(Prohibit modification and deletion)
