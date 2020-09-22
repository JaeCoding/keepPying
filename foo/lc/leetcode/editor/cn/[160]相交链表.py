# Write a program to find the node at which the intersection of two singly linke
# d lists begins. 
# 
#  For example, the following two linked lists: 
# 
# 
#  begin to intersect at node c1. 
# 
#  
# 
#  Example 1: 
# 
# 
#  
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2
# , skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not 
# be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. F
# rom the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the inter
# sected node in A; There are 3 nodes before the intersected node in B. 
# 
#  
# 
#  Example 2: 
# 
# 
#  
# Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skip
# B = 1
# Output: Reference of the node with value = 2
# Input Explanation: The intersected node's value is 2 (note that this must not 
# be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. F
# rom the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected
#  node in A; There are 1 node before the intersected node in B.
#  
# 
#  
# 
#  Example 3: 
# 
# 
#  
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: null
# Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B
# , it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 
# 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.
#  
# 
#  
# 
#  Notes: 
# 
#  
#  If the two linked lists have no intersection at all, return null. 
#  The linked lists must retain their original structure after the function retu
# rns. 
#  You may assume there are no cycles anywhere in the entire linked structure. 
#  Your code should preferably run in O(n) time and use only O(1) memory. 
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from foo import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        len_a = 0
        cur_a = headA
        while cur_a.next:
            cur_a = cur_a.next
            len_a += 1

        len_b = 0
        cur_b = headB
        while cur_b.next:
            cur_b = cur_b.next
            len_b += 1

        # tail not equals
        if cur_a != cur_b:
            return None

        cur_a_new = headA
        cur_b_new = headB
        if len_a >= len_b:
            for i in range(0, len_a - len_b):
                cur_a_new = cur_a_new.next
        else:
            for i in range(0, len_b - len_a):
                cur_b_new = cur_b_new.next

        while True:
            if cur_a_new == cur_b_new:
                return cur_a_new
            cur_a_new, cur_b_new = cur_a_new.next, cur_b_new.next

# leetcode submit region end(Prohibit modification and deletion)
