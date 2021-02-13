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

from foo import TreeNode
from foo import TreeUtil


# Z字打印，关键在于使用了一个栈，以及使用了一个flag表示添加左右子树的顺序

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        stack: List[TreeNode] = []
        stack.append(root)
        result.append([root.val])
        direct = 'right'
        while stack:
            next_stack = []
            next_print = []
            for i in range(0, len(stack)):
                node = stack.pop()
                if direct == 'right':
                    if node.right:
                        next_stack.append(node.right)
                        next_print.append(node.right.val)
                    if node.left:
                        next_stack.append(node.left)
                        next_print.append(node.left.val)
                elif direct == 'left':
                    if node.left:
                        next_stack.append(node.left)
                        next_print.append(node.left.val)
                    if node.right:
                        next_stack.append(node.right)
                        next_print.append(node.right.val)
            if next_print:
                result.append(next_print)
            stack = next_stack
            direct = 'left' if(direct == 'right') else 'right'
        return result
# leetcode submit region end(Prohibit modification and deletion)

t = TreeUtil().creat_tree([1,2,3,4,'null','null',5])

a = Solution().zigzagLevelOrder(t)

print(a)