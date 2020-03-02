# Given a binary tree, return the inorder traversal of its nodes' values. 
# 
#  Example: 
# 
#  
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
# 
# Output: [1,3,2] 
# 
#  Follow up: Recursive solution is trivial, could you do it iteratively? 
#  Related Topics 栈 树 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from foo.lc.TreeNode import TreeNode
from foo.lc.TreeUtil import TreeUtil


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return []
        result = []

        def recur(node: TreeNode):
            if not node:
                return
            recur(node.left)
            result.append(node.val)
            recur(node.right)

        recur(root)
        return result



# leetcode submit region end(Prohibit modification and deletion)

a = TreeUtil().creat_tree([1, 4, 4, 'null', 2, 2, 'null', 1, 'null', 6, 8, 'null', 'null', 'null', 'null', 1, 3])

b = Solution().inorderTraversal(a)

print(b)