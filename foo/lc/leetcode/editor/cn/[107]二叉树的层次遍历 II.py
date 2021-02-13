# Given a binary tree, return the bottom-up level order traversal of its nodes' 
# values. (ie, from left to right, level by level from leaf to root). 
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
# return its bottom-up level order traversal as: 
#  
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#  
#  Related Topics 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from foo import TreeNode


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        levels: List[List[int]] = []

        if not root:
            return levels

        def helper(node: TreeNode, level: int):

            if len(levels) == level:
                # 每次往头部插新数组，而不是在后面插，这样就是最底层在上啦
                levels.insert(0, [])

            # 从上往下层序遍历是 level[index]; 从下往上遍历，则需要 从后向前的第index个
            levels[len(levels) - 1 - level].append(node.val)

            if node.left:
                helper(node.left, level + 1)

            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)

        return levels
        
# leetcode submit region end(Prohibit modification and deletion)
