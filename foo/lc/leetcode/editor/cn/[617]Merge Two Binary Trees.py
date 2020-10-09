# Given two binary trees and imagine that when you put one of them to cover the 
# other, some nodes of the two trees are overlapped while the others are not. 
# 
#  You need to merge them into a new binary tree. The merge rule is that if two 
# nodes overlap, then sum node values up as the new value of the merged node. Othe
# rwise, the NOT null node will be used as the node of new tree. 
# 
#  Example 1: 
# 
#  
# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7
#  
# 
#  
# 
#  Note: The merging process must start from the root nodes of both trees. 
#  Related Topics 树 
#  👍 523 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from foo.lc.leetcode.editor.TreeNode import TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        elif not t2:
            return t1

        def dfs(tt1: TreeNode, tt2: TreeNode, tt3: TreeNode):
            if not tt1 and not tt2:
                return None
            left = dfs(tt1.left, tt2.left)
            right = dfs(tt1.right, tt2.right)
            if left and right:
                return TreeNode(left.val + right.val)
            elif left:
                return TreeNode


# leetcode submit region end(Prohibit modification and deletion)
