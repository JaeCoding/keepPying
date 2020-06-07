# Given a binary tree, check whether it is a mirror of itself (ie, symmetric aro
# und its center). 
# 
#  For example, this binary tree [1,2,2,3,4,4,3] is symmetric: 
# 
#  
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#  
# 
#  
# 
#  But the following [1,2,2,null,3,null,3] is not: 
# 
#  
#     1
#    / \
#   2   2
#    \   \
#    3    3
#  
# 
#  
# 
#  Follow up: Solve it both recursively and iteratively. 
#  Related Topics 树 深度优先搜索 广度优先搜索


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
    def isSymmetric(self, root: TreeNode) -> bool:

        def is_mirror(node1: TreeNode, node2: TreeNode):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            return is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)

        return is_mirror(root, root)


# head = TreeUtil.creat_tree(['1', '2', '2', '3', '4', '4', '3'])
head = TreeUtil.creat_tree([1,2,2,'null',3,'null',3])
a = Solution().isSymmetric(head)
print(a)

# leetcode submit region end(Prohibit modification and deletion)
