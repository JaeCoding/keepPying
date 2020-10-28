# Given the root of a binary tree, return the preorder traversal of its nodes' v
# alues. 
# 
#  
#  Example 1: 
# 
#  
# Input: root = [1,null,2,3]
# Output: [1,2,3]
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: [1]
#  
# 
#  Example 4: 
# 
#  
# Input: root = [1,2]
# Output: [1,2]
#  
# 
#  Example 5: 
# 
#  
# Input: root = [1,null,2]
# Output: [1,2]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 100]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# 
#  Follow up: 
# 
#  Recursive solution is trivial, could you do it iteratively? 
# 
#  
#  Related Topics 栈 树 
#  👍 426 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from foo.lc.leetcode.editor.TreeNode import TreeNode
from foo.lc.leetcode.editor.TreeUtil import TreeUtil


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def pre(node: TreeNode):
            if not node:
                return
            result.append(node.val)
            pre(node.left)
            pre(node.right)
        pre(root)
        return result

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


# root = TreeUtil.creat_tree([1,2,3,4,5,6,7])
root = TreeUtil.creat_tree([])
a = Solution().preorderTraversal2(root)
print(a)
        
# leetcode submit region end(Prohibit modification and deletion)
