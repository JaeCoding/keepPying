# Given a sorted linked list, delete all duplicates such that each element appea
# r only once. 
# 
#  Example 1: 
# 
#  
# Input: 1->1->2
# Output: 1->2
#  
# 
#  Example 2: 
# 
#  
# Input: 1->1->2->3->3
# Output: 1->2->3
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy: ListNode = ListNode(-1)
        dummy.next = head
        # previous different element
        cur = dummy
        after: ListNode = cur.next
        while cur.next:

            cur = cur.next
            if after.next and after.val == after.next.val:


                # find the end of duplication
                while after.next and after.val == after.next.val:
                    after = after.next
                cur.next = after.next

            after = cur.next


        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
