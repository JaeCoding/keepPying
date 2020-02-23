# Given a linked list and a value x, partition it such that all nodes less than 
# x come before nodes greater than or equal to x. 
# 
#  You should preserve the original relative order of the nodes in each of the t
# wo partitions. 
# 
#  Example: 
# 
#  
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
#  
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from foo.lc.ListNode import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        less_tail = dummy
        more_tail = dummy
        while cur:
            # 重要思想：从链表中摘除一个元素；
            if cur.val < x:  # put cur after less_tail
                # -1(less_tail) -> 1(cur) -> 4
                more_tail.next = cur.next  # pick out the cur from the list  -1(less_tail) -> 4     1(cur)
                cur.next = less_tail.next  # link the post     -1(less_tail) -> 4  and    1(cur) -> 4
                less_tail.next = cur  # link the pre          -1(less_tail) -> 1(cur) -> 4
                more_tail = more_tail.next if (more_tail == less_tail) else more_tail
                less_tail = less_tail.next
            else:  # put cur after more_tail
                more_tail.next = cur.next
                cur.next = more_tail.next
                more_tail.next = cur
                more_tail = more_tail.next

            cur = more_tail.next

        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
