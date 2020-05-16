# Given a linked list, reverse the nodes of a linked list k at a time and return
#  its modified list. 
# 
#  k is a positive integer and is less than or equal to the length of the linked
#  list. If the number of nodes is not a multiple of k then left-out nodes in the 
# end should remain as it is. 
# 
#  
#  
# 
#  Example: 
# 
#  Given this linked list: 1->2->3->4->5 
# 
#  For k = 2, you should return: 2->1->4->3->5 
# 
#  For k = 3, you should return: 3->2->1->4->5 
# 
#  Note: 
# 
#  
#  Only constant extra memory is allowed. 
#  You may not alter the values in the list's nodes, only nodes itself may be ch
# anged. 
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from foo.lc.ListNode import ListNode
from foo.lc.ListUtil import ListUtil


class Solution:

    def reverseK(self, head: ListNode, k: int) -> ListNode:
        # 传入head的前驱，比如dummy
        # 看当前开始是否有K个, 如果没有k个 直接返回不翻转了
        end = head  # end其实是下一段的开头了
        for i in range(k):
            end = end.next
            if not end:
                return None  # 返回个空，提示外部调用，已经结束
        # 开始翻转，记录三个指针
        pre = head
        cur = pre.next
        next = cur.next
        # 开始翻转k个，其实只要摘出k-1个,放到前部，所以大于1就好
        while k > 1:
           cur.next = next.next  # 将next摘出来
           next.next = pre.next  # 将next指向头部的后面
           pre.next = next  # 将头部指向插入的节点
           next = cur.next  # 下一待摘出节点
           k -= 1

        return cur  # 把最后一个元素返回，用于下一轮的前驱（dummy）


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        end = dummy
        while end:
            # 只要不为None 说明还能翻转
            end = self.reverseK(end, k)
        return dummy.next



head = ListUtil().creat_tree([1,2,3,4,5,6,7])
a = Solution().reverseKGroup(head, 3)
print(a)

# leetcode submit region end(Prohibit modification and deletion)
