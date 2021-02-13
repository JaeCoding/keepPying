# Given a binary tree and a sum, find all root-to-leaf paths where each path's s
# um equals the given sum. 
# 
#  Note: A leaf is a node with no children. 
# 
#  Example: 
# 
#  Given the below binary tree and sum = 22, 
# 
#  
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
#  
# 
#  Return: 
# 
#  
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]
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

from foo import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        if not root:
            return []

        result = []
        out = []

        # element can be minus，so can't cur the branch
        def dfs(node: TreeNode, target: int):
            if node.val == target and not node.left and not node.right:
                out.append(node.val)
                result.append(out.copy())
                out.pop()
            else:
                if node.left:
                    out.append(node.val)
                    dfs(node.left, target - node.val)
                    out.pop()
                if node.right:
                    out.append(node.val)
                    dfs(node.right, target - node.val)
                    out.pop()

        dfs(root, sum)
        return result




# leetcode submit region end(Prohibit modification and deletion)
