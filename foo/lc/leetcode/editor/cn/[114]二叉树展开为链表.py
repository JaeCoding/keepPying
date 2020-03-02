# Given a binary tree, flatten it to a linked list in-place. 
# 
#  For example, given the following tree: 
# 
#  
#     1
#    / \
#   2   5
#  / \   \
# 3   4   6
#  
# 
#  The flattened tree should look like: 
# 
#  
# 1
#  \
#   2
#    \
#     3
#      \
#       4
#        \
#         5
#          \
#           6
#  
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from foo.lc.TreeNode import TreeNode


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        l: List[TreeNode] = []

        def dfs(node: TreeNode):
            l.append(node)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)

        for i in range(0, len(l)-1):
            l[i].left = None
            l[i].right = l[i+1]

        l[len(l)-1].right = None
        l[len(l)-1].left = None

# leetcode submit region end(Prohibit modification and deletion)
