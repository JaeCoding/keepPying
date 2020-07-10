# Given a binary tree and a sum, determine if the tree has a root-to-leaf path s
# uch that adding up all the values along the path equals the given sum. 
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
#  /  \      \
# 7    2      1
#  
# 
#  return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22. 
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
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def helper(node: TreeNode, total: int):

            total = total + node.val

            # when it reach the leaf
            if not node.left and not node.right:
                return total == sum

            l = helper(node.left, total) if node.left else False
            r = helper(node.right, total) if node.right else False
            return l or r


        if not root:
            return False
        return helper(root, 0)



root = TreeUtil.creat_tree([5,4,8,11,'null',13,4,7,2,'null','null','null',1])
a = Solution().hasPathSum(root, 22)
print(a)
# leetcode submit region end(Prohibit modification and deletion)
