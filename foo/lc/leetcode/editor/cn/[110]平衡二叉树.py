# Given a binary tree, determine if it is height-balanced. 
# 
#  For this problem, a height-balanced binary tree is defined as: 
# 
#  
#  a binary tree in which the left and right subtrees of every node differ in he
# ight by no more than 1. 
#  
# 
#  
# 
#  Example 1: 
# 
#  Given the following tree [3,9,20,null,null,15,7]: 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  Return true. 
#  
# Example 2: 
# 
#  Given the following tree [1,2,2,3,3,null,null,4,4]: 
# 
#  
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#  
# 
#  Return false. 
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from foo.lc.TreeNode import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        # if note.left and note.right both are balance then, node is balance
        if not root:
            return True

        def height(node: TreeNode) -> int:
            if not node:
                return 0
            else:
                return max(height(node.left), height(node.right)) + 1

        return self.isBalanced(root.left) and self.isBalanced(root.right) \
               and abs(height(root.left) - height(root.right)) <= 1




        
# leetcode submit region end(Prohibit modification and deletion)
