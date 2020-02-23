# Reverse a singly linked list. 
# 
#  Example: 
# 
#  
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#  
# 
#  Follow up: 
# 
#  A linked list can be reversed either iteratively or recursively. Could you im
# plement both? 
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from foo.lc.ListNode import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        tail, cur = head, head.next
        while cur:

            tail.next = cur.next  # pick out
            cur.next = dummy.next  # link before the dummy
            dummy.next = cur  # link

            cur = tail.next

        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
