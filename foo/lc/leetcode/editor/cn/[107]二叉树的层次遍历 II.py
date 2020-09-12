# Given a binary tree, return the bottom-up level order traversal of its nodes' 
# values. (ie, from left to right, level by level from leaf to root). 
# 
#  
# For example: 
# Given binary tree [3,9,20,'null','null',15,7],
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  
#  
# return its bottom-up level order traversal as: 
#  
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#  
#  Related Topics 树 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
from typing import List

from foo.lc.TreeNode import TreeNode
from foo.lc.TreeUtil import TreeUtil


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        levels: List[List[int]] = []

        if not root:
            return levels

        def helper(node: TreeNode, level: int):

            if len(levels) == level:
                # 每次往头部插新数组，而不是在后面插，这样就是最底层在上啦
                levels.insert(0, [])

            # 从上往下层序遍历是 level[index]; 从下往上遍历，则需要 从后向前的第index个
            levels[len(levels) - 1 - level].append(node.val)

            if node.left:
                helper(node.left, level + 1)

            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)

        return levels

    def levelOrderBottom1(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        this_row = queue.Queue()
        next_row = queue.Queue()
        save = []
        this_row.put(root)
        while not this_row.empty():
            node = this_row.get()
            save.append(node.val)
            if node.left:
                next_row.put(node.left)
            if node.right:
                next_row.put(node.right)
            # 到达最后一个位置,更换队列
            if this_row.empty():
                result.insert(0, save.copy())
                this_row = next_row
                next_row = queue.Queue()
                save = []
        return result
root = TreeUtil.creat_tree([3,9,20,'null','null',15,7])
a = Solution().levelOrderBottom1(root)
print(a)

# leetcode submit region end(Prohibit modification and deletion)
