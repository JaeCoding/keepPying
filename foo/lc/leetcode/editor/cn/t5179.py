from typing import List

from foo import TreeNode
from foo import TreeUtil


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[TreeNode]:
        if not root:
            return []
        result = []

        def recur(node: TreeNode):
            if not node:
                return
            recur(node.left)
            result.append(node)
            recur(node.right)

        recur(root)
        return result

    def sortedArrayToBST(self, nums: List[TreeNode]) -> TreeNode:

        def recur(left: int, right: int) -> TreeNode:
            if left == right:
                return None

            mid: int = int((left + right) / 2)
            root: TreeNode = nums[mid]

            root.left = recur(left, mid)
            root.right = recur(mid + 1, right)

            return root

        return recur(0, len(nums))

    def balanceBST(self, root: TreeNode) -> TreeNode:

        l = self.inorderTraversal(root)
        r = self.sortedArrayToBST(l)
        return r


root = TreeUtil.creat_tree([1,"null",2,"null",3,"null",4,"null","null"])

a = Solution().balanceBST(root)