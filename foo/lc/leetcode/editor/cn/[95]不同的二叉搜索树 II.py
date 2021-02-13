# Given an integer n, generate all structurally unique BST's (binary search tree
# s) that store values 1 ... n. 
# 
#  Example: 
# 
#  
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  
#  Related Topics 树 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from foo import TreeNode
import copy


class Solution:

    def generateTrees(self, n: int) -> List[TreeNode]:

        if n == 0:
            return []

        def helper(left: int, right: int) -> List[TreeNode]:
            if left == right:
                return [None]

            tree_list: List[TreeNode] = []
            for i in range(left, right):
                node = TreeNode(i)
                left_list = helper(left, i)
                right_list = helper(i + 1, right)
                for leftNode in left_list:
                    for rightNode in right_list:
                        node.left = leftNode
                        node.right = rightNode
                        tree_list.append(copy.copy(node))

            return tree_list

        return helper(1, n+1)


a = Solution().generateTrees(3)
# leetcode submit region end(Prohibit modification and deletion)
