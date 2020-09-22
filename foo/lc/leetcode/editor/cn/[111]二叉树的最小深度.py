# Given a binary tree, find its minimum depth. 
# 
#  The minimum depth is the number of nodes along the shortest path from the roo
# t node down to the nearest leaf node. 
# 
#  Note: A leaf is a node with no children. 
# 
#  Example: 
# 
#  Given binary tree [3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  return its minimum depth = 2. 
#  Related Topics 树 深度优先搜索 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from foo import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def recur(node: TreeNode):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            if not node.left:
                return recur(node.right) + 1
            if not node.right:
                return recur(node.left) + 1

            return min(recur(node.left), recur(node.right)) + 1

        return recur(root)


# leetcode submit region end(Prohibit modification and deletion)
