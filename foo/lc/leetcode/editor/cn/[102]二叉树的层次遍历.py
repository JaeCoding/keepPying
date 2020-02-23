# Given a binary tree, return the level order traversal of its nodes' values. (i
# e, from left to right, level by level). 
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
# return its level order traversal as: 
#  
# [
#   [3],
#   [9,20],
#   [15,7]
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

from foo.lc.TreeNode import TreeNode


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        levels: List[List[int]] = []
        if not root:
            return levels

        def helper(node: TreeNode, level: int):
            # 初次进入新的一层, 需要添加一个列表以供使用。 比如初次进入第二层，  只有原先第一层列表，此时添加
            if len(levels) == level:
                levels.append([])

            # 将当前加入对应层
            levels[level].append(node.val)

            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels




# leetcode submit region end(Prohibit modification and deletion)