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
#  👍 705 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from foo import TreeNode


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        result = []
        def recursion(node: TreeNode):
            if not node:
                return
            recursion(node.left)
            result.append(node.val)
            recursion(node.right)
        recursion(root)
        return result

# leetcode submit region end(Prohibit modification and deletion)
