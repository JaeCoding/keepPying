# Merge two sorted linked lists and return it as a new list. The new list should
#  be made by splicing together the nodes of the first two lists. 
# 
#  Example:
#  
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from foo import ListNode
from foo import ListUtil


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy: ListNode = ListNode(0)
        now = dummy
        while l1 and l2:
            now.next = l1 if l1.val <= l2.val else l2
            now = now.next
            if l1.val <= l2.val:
                l1 = l1.next
            else:
                l2 = l2.next
        #  将剩余的尾部拼接上
        now.next = l1 if not l2 else l2
        return dummy.next


l1 = ListUtil().creat_tree([])
l2 = ListUtil().creat_tree([])
a = Solution().mergeTwoLists(l1, l2)
print(a)

# leetcode submit region end(Prohibit modification and deletion)
