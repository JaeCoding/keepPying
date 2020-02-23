# Given a singly linked list where elements are sorted in ascending order, conve
# rt it to a height balanced BST. 
# 
#  For this problem, a height-balanced binary tree is defined as a binary tree i
# n which the depth of the two subtrees of every node never differ by more than 1.
#  
# 
#  Example: 
# 
#  
# Given the sorted linked list: [-10,-3,0,5,9],
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
#  Related Topics 深度优先搜索 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from foo.lc.ListNode import ListNode
from foo.lc.TreeNode import TreeNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next


        def build_binary_tree(left, right) -> TreeNode:

            if left > right:
                return None
            mid = int((left + right) / 2)
            node = TreeNode(nums[mid])

            node.left = build_binary_tree(left, mid-1)
            node.right = build_binary_tree(mid+1, right)

            return node

        return build_binary_tree(0, len(nums)-1)
        
# leetcode submit region end(Prohibit modification and deletion)
