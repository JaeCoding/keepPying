# Given two non-empty binary trees s and t, check whether tree t has exactly the
#  same structure and node values with a subtree of s. A subtree of s is a tree co
# nsists of a node in s and all of this node's descendants. The tree s could also 
# be considered as a subtree of itself. 
# 
#  Example 1: 
# Given tree s: 
# 
#  
#      3
#     / \
#    4   5
#   / \
#  1   2
#  
# Given tree t:
# 
#  
#    4 
#   / \
#  1   2
#  
# Return true, because t has the same structure and node values with a subtree o
# f s.
# 
#  
# 
#  Example 2: 
# Given tree s: 
# 
#  
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
#  
# Given tree t:
# 
#  
#    4
#   / \
#  1   2
#  
# Return false.
# 
#  
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from foo import TreeNode
from foo import TreeUtil


class Solution:
    def __init__(self):
        self.flag = False

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not t:
            return True
        if not s:
            return False

        r = t.val

        def in_order(node: TreeNode):
            if not node:
                return
            in_order(node.left)
            if node.val == r:
                self.flag = self.flag or is_sub(node, t)
            in_order(node.right)


        def is_sub(node_l: TreeNode, node_r: TreeNode) -> bool:
            if not node_l and not node_r:
                return True
            if not node_l or not node_r or node_l.val != node_r.val:
                return False
            return is_sub(node_l.left, node_r.left) and is_sub(node_l.right, node_r.right)

        in_order(s)
        return self.flag

root1 = TreeUtil().creat_tree([3, 4, 5, 1, 2, 'null', 'null'])
root2 = TreeUtil().creat_tree([4, 1, 2])

a = Solution().isSubtree(root1, root2)
print(a)
        
# leetcode submit region end(Prohibit modification and deletion)
