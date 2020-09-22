# Find the sum of all left leaves in a given binary tree. 
# 
#  Example:
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15 respectivel
# y. Return 24.
#  
#  Related Topics 树 
#  👍 207 👎 0


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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        what is the left leaves, it has no son node and is left of his father
        @param root:
        """
        result = [0]
        def dfs(node: TreeNode, pos: str):
            if not node:
                return
            if not node.left and not node.right:
                if pos == 'left':
                    result[0] += node.val
                return
            dfs(node.left, 'left')
            dfs(node.right, 'right')
        dfs(root, 'mid')
        return result[0]

root = TreeUtil.creat_tree([0, 2, 4, 1, 'null', 3, -1, 5, 1, 'null', 6, 'null', 8])


a = Solution().sumOfLeftLeaves(root)
print(a)
# leetcode submit region end(Prohibit modification and deletion)
