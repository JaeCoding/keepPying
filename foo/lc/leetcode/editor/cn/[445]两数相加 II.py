# You are given two non-empty linked lists representing two non-negative integer
# s. The most significant digit comes first and each of their nodes contain a sing
# le digit. Add the two numbers and return it as a linked list. 
# 
#  You may assume the two numbers do not contain any leading zero, except the nu
# mber 0 itself. 
# 
#  Follow up: 
# What if you cannot modify the input lists? In other words, reversing the lists
#  is not allowed.
#  
# 
#  
# Example:
#  
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        h1 = l1
        num1 = 0
        h2 = l2
        num2 = 0
        while h1:
            num1 = h1.val + 10 * num1
            h1 = h1.next
        while h2:
            num2 = h2.val + 10 * num2
            h2 = h2.next
        sum = str(num1 + num2)

        dummy = ListNode(-1)
        now = dummy
        for s in sum:
            node = ListNode(s)
            now.next = node
            now = now.next
        return dummy.next



# leetcode submit region end(Prohibit modification and deletion)
