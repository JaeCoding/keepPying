# Reverse a linked list from position m to n. Do it in one-pass. 
# 
#  Note: 1 ≤ m ≤ n ≤ length of list. 
# 
#  Example: 
# 
#  
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if m == n:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        for i in range(0, m - 1):
            pre = pre.next

        tail = pre.next
        cur = tail.next
        for i in range(0, n - m):
            tail.next = cur.next  # pick out
            cur.next = pre.next  # link next
            pre.next = cur  # link pre

            cur = tail.next  # tail is always unchanged

        return dummy.next

        
# leetcode submit region end(Prohibit modification and deletion)
