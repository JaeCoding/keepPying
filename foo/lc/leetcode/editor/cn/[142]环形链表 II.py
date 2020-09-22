# Given a linked list, return the node where the cycle begins. If there is no cy
# cle, return null. 
# 
#  To represent a cycle in the given linked list, we use an integer pos which re
# presents the position (0-indexed) in the linked list where tail connects to. If 
# pos is -1, then there is no cycle in the linked list. 
# 
#  Note: Do not modify the linked list. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the s
# econd node.
#  
# 
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the f
# irst node.
#  
# 
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#  
# 
#  
# 
#  
# 
#  Follow-up: 
# Can you solve it without using extra space? 
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from foo import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head and head.next and head.next.next:
            return None
        f_step, s_step = 2, 1
        fast, slow = head.next.next, head.next
        while fast != slow:
            if not fast.next or not fast.next.next:
                return None
            fast, slow = fast.next.next, slow.next
            f_step += 2
            s_step += 1


        
# leetcode submit region end(Prohibit modification and deletion)
