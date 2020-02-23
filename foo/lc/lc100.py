from foo.lc.TreeNode import TreeNode

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        :rtype: object
        """
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

n = TreeNode(1)
c = TreeNode(1)
result = Solution().isSameTree(n, c)
print(result)
