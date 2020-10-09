# Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
#  given nodes in the BST. 
# 
#  According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T that has both p and
#  q as descendants (where we allow a node to be a descendant of itself).” 
# 
#  Given binary search tree: root = [6,2,8,0,4,7,9,'null','null',3,5]
# 
#  
# 
#  Example 1: 
# 
#  
# Input: root = [6,2,8,0,4,7,9,'null','null',3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [6,2,8,0,4,7,9,'null','null',3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant o
# f itself according to the LCA definition.
#  
# 
#  
#  Constraints: 
# 
#  
#  All of the nodes' values will be unique. 
#  p and q are different and both values will exist in the BST. 
#  
#  Related Topics 树 
#  👍 446 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from foo.lc.leetcode.editor.TreeNode import TreeNode
from foo.lc.leetcode.editor.TreeUtil import TreeUtil


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # to confirm p is less one
        if p.val > q.val:
            p, q = q, p

        def dfs(node: TreeNode) -> TreeNode:
            if p.val <= node.val <= q.val:
                return node
            elif p.val <= q.val < node.val:
                return dfs(node.left)
            else:
                return dfs(node.right)

        return dfs(root)

root = TreeUtil.creat_tree([6,2,8,0,4,7,9,'null','null',3,5])

a = Solution().lowestCommonAncestor(root, root.left, root.left.right)
print(a.val)

# leetcode submit region end(Prohibit modification and deletion)
