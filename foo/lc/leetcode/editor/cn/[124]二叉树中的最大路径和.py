# Given a non-empty binary tree, find the maximum path sum. 
# 
#  For this problem, a path is defined as any sequence of nodes from some starti
# ng node to any node in the tree along the parent-child connections. The path mus
# t contain at least one node and does not need to go through the root. 
# 
#  Example 1: 
# 
#  
# Input: [1,2,3]
# 
#        1
#       / \
#      2   3
# 
# Output: 6
#  
# 
#  Example 2: 
# 
#  
# Input: [-10,9,20,null,null,15,7]
# 
#    -10
#    / \
#   9  20
#     /  \
#    15   7
# 
# Output: 42
#  
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from foo import TreeNode
from foo import TreeUtil


class Solution:
    def __init__(self):
        self.m = float("-inf")
        # self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def max_sum(node: TreeNode):
            if not node:
                return 0
            left_max = max(max_sum(node.left), 0)
            right_max = max(max_sum(node.right), 0)
            node_sum = node.val + left_max + right_max
            self.m = max(self.m, node_sum)
            return max(left_max + node.val, right_max + node.val)  # 只能上报左路径或者右路径中的一条

        max_sum(root)
        return self.m


root = TreeUtil.creat_tree([-10, 9, 20, 'null', 'null', 15, 7])
# root = TreeUtil.creat_tree([5, 4, 8, 11, 'null', 13, 4, 7, 2, 'null', 'null', 'null', 1])
a = Solution().maxPathSum(root)
print(a)

# leetcode submit region end(Prohibit modification and deletion)
