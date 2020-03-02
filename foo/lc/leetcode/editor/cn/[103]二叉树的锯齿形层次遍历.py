# Given a binary tree, return the zigzag level order traversal of its nodes' val
# ues. (ie, from left to right, then right to left for the next level and alternat
# e between). 
# 
#  
# For example: 
# Given binary tree [3,9,20,null,null,15,7], 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  
#  
# return its zigzag level order traversal as: 
#  
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#  Related Topics 栈 树 广度优先搜索


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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        result = []
        stack = []
        stack.append(root)
        direct = 'right'
        while stack:
            next_stack = []
            for i in range(0, len(stack)):
                node = stack.pop()
                if direct == 'right':
                    if node.right:
                        next_stack.append(node.right)
                    if node.left:
                        next_stack.append(node.left)
                elif direct == 'left':
                    if node.right:
                        next_stack.append(node.right)
                    if node.left:
                        next_stack.append(node.left)
            result.append(next_stack)
            stack = next_stack
            direct = 'left' if(direct == 'right') else 'right'
        return result
# leetcode submit region end(Prohibit modification and deletion)


a = Solution().zigzagLevelOrder()