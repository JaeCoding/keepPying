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
#  👍 419 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from foo.lc.leetcode.editor.ListNode import ListNode
from foo.lc.leetcode.editor.ListUtil import ListUtil


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        # find the mid
        mid, fast = head, head
        while fast.next and fast.next.next:
            mid = mid.next
            fast = fast.next.next
        # revert the second half
        tail = mid.next

        while tail.next:
            out = tail.next
            tail.next = out.next
            out.next = mid.next
            mid.next = out

        # combine the first half and second
        pre = head
        while mid.next and pre.next.next:
            out = mid.next
            mid.next = out.next
            out.next = pre.next
            pre.next = out
            pre = pre.next.next

        return head

node = ListUtil().creat_tree([1,2,3,4,5,6,7])
node = ListUtil().creat_tree([1,2,3])
a = Solution().reorderList(node)
ListUtil().printListNode(a)

# leetcode submit region end(Prohibit modification and deletion)
