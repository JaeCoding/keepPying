# Invert a binary tree. 
# 
#  Example: 
# 
#  Input: 
# 
#  
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9 
# 
#  Output: 
# 
#  
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1 
# 
#  Trivia: 
# This problem was inspired by this original tweet by Max Howell: 
# 
#  Google: 90% of our engineers use the software you wrote (Homebrew), but you c
# an’t invert a binary tree on a whiteboard so f*** off. 
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from foo.lc.TreeNode import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return root


        def dfs(node: TreeNode):
            if not node.left and not node.right:
                return

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            tmp = node.left
            node.left = node.right
            node.right = tmp
        dfs(root)

        return root


# leetcode submit region end(Prohibit modification and deletion)
