# Given an array where elements are sorted in ascending order, convert it to a h
# eight balanced BST. 
# 
#  For this problem, a height-balanced binary tree is defined as a binary tree i
# n which the depth of the two subtrees of every node never differ by more than 1.
#  
# 
#  Example: 
# 
#  
# Given the sorted array: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following he
# ight balanced BST:
# 
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#  
#  Related Topics 树 深度优先搜索


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

    # buildBalanceBinaryTree
    # 1. find the mid
    # 2. find the mid of left part, it is mid.left
    # 3. find the mid of right part, it is mid.right

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def recur(left: int, right: int) -> TreeNode:
            if left == right:
                return None
            mid: int = int((left + right) / 2)
            root: TreeNode = TreeNode(nums[mid])
            root.left = recur(left, mid)
            root.right = recur(mid + 1, right)
            return root

        return recur(0, len(nums))

    def sortedArrayToBST2(self, nums: List[int]) -> TreeNode:

        def recur(left: int, right: int):
            if left == right:
                return None

            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = recur(left, mid)
            node.right = recur(mid + 1, right)
            return node

        a = recur(0, len(nums))
        return a





# leetcode submit region end(Prohibit modification and deletion)

# Solution().sortedArrayToBST([0, 1, 2, 3, 4, 5])
a = Solution().sortedArrayToBST2([-10,-3,0,5,9])
print(a)
