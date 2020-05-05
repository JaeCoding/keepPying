# Given a binary tree, determine if it is a valid binary search tree (BST). 
# 
#  Assume a BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than the node's
#  key. 
#  The right subtree of a node contains only nodes with keys greater than the no
# de's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
# 
#  Example 1: 
# 
#  
#     2
#    / \
#   1   3
# 
# Input: [2,1,3]
# Output: true
#  
# 
#  Example 2: 
# 
#  
#     5
#    / \
#   1   4
#      / \
#     3   6
# 
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#  
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from foo.lc.TreeNode import TreeNode
from foo.lc.TreeUtil import TreeUtil


class Solution:
    def __init__(self):
        self.last = -100000
        self.flag = True
    def isValidBST(self, root: TreeNode) -> bool:

        def in_order(node: TreeNode):
            if not node:
                return
            in_order(node.left)  # if not left, return True
            if node.val <= self.last:  # 比上一个值小 说明发现了不是升序
                self.flag = False
            self.last = node.val
            in_order(node.right)  # compare now and father

        in_order(root)

        return self.flag

root = TreeUtil.creat_tree([3,2,5,1,3,'null', 'null'])
a = Solution().isValidBST(root)
print(a)
# leetcode submit region end(Prohibit modification and deletion)
