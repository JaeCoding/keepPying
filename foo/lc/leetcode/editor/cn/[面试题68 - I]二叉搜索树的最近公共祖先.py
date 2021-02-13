# English description is not available for the problem. Please switch to Chinese
# . Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from foo import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #　binary search tree
        if p.val > q.val:
            ma = p
            mi = q
        elif p.val < q.val:
            ma = q
            mi = p
        else:
            return p

        def dfs(cur: TreeNode) -> TreeNode:
            if mi.val <= cur.val <= ma.val:
                return cur
            elif mi.val < cur.val and ma.val < cur.val:
                return dfs(cur.left)
            else:
                return dfs(cur.right)
        return dfs(root)



# leetcode submit region end(Prohibit modification and deletion)
