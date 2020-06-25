# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes 
# in the tree. 
# 
#  According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T that has both p and
#  q as descendants (where we allow a node to be a descendant of itself).” 
# 
#  Given the following binary tree: root = [3,5,1,6,2,0,8,null,null,7,4] 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant o
# f itself according to the LCA definition.
#  
# 
#  
# 
#  Note: 
# 
#  
#  All of the nodes' values will be unique. 
#  p and q are different and both values will exist in the binary tree. 
#  
#  Related Topics 树


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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        res = []
        to_find = [p, q]

        def in_order(now: list, node: TreeNode):
            if not node:
                return
            now.append(node)
            # 发现重合值 添加当前路径
            if node in to_find:
                res.append(now.copy())
            in_order(now, node.left)
            in_order(now, node.right)
            now.pop()
            return res

        in_order([], root)
        root1, root2 = res[0], res[1]
        i = 0
        while i < min(len(root1), len(root2)) and root1[i] == root2[i]:
            i += 1
        return root1[i-1]


root = TreeUtil.creat_tree([3, 5, 1, 6, 2, 0, 8, 'null', 'null', 7, 4])
l = root.left
r = root.left.right.right
a = Solution().lowestCommonAncestor(root, l, r)
print(a.val)

# leetcode submit region end(Prohibit modification and deletion)
