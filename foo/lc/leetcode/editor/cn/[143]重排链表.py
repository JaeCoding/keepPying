# Given a singly linked list L: L0→L1→…→Ln-1→Ln, 
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→… 
# 
#  You may not modify the values in the list's nodes, only nodes itself may be c
# hanged. 
# 
#  Example 1: 
# 
#  
# Given 1->2->3->4, reorder it to 1->4->2->3. 
# 
#  Example 2: 
# 
#  
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from foo.lc.ListNode import ListNode


class Solution:

    # see 876
    def middleNode(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow if not fast else slow.next

    # see 206
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

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # 1. find the midpoint of list

        mid = self.middleNode(head)

        # 2. revert the second half of list

        min_next = self.reverseList(mid.next)

        # 3. insert the second half to first half

        pre, cur = head, min_next
        while cur:
            mid.next = cur.next  # pick out the cur
            cur.next = pre.next  # link the tail
            pre.next = cur  # link the head

            cur = mid.next
            pre = pre.next.next

# leetcode submit region end(Prohibit modification and deletion)
