# Given a binary tree, imagine yourself standing on the right side of it, return
#  the values of the nodes you can see ordered from top to bottom. 
# 
#  Example: 
# 
#  
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#  Related Topics 树 深度优先搜索 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from typing import List

from foo import TreeNode
from foo import TreeUtil


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        out = deque()
        result: List[int] = []
        out.append(root)
        while len(out) != 0:
            next_out = deque()
            for i in range(len(out)):
                node = out.pop()
                if node.left:
                    next_out.appendleft(node.left)
                if node.right:
                    next_out.appendleft(node.right)
                if len(out) == 0:
                    result.append(node.val)
            out = next_out

        return result

root = TreeUtil.creat_tree([1,2,3,'null',5,'null',4])

a = Solution().rightSideView(root)
print(a)

# leetcode submit region end(Prohibit modification and deletion)
