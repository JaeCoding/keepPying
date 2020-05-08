# Merge k sorted linked lists and return it as one sorted list. Analyze and desc
# ribe its complexity. 
# 
#  Example: 
# 
#  
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#  
#  Related Topics 堆 链表 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List

from foo.lc.ListNode import ListNode
from foo.lc.ListUtil import ListUtil


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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        count_now = len(lists)
        # 难点在于位置 奇偶的判断 自己画个草图就很清晰了
        while count_now > 1:
            position = 0
            while position < count_now:
                if position != count_now - 1:
                    # 如果当前位置不是最后一个,就合并
                    lists[int(position / 2)] = self.mergeTwoLists(lists[position], lists[position + 1])
                else:
                    # 否则直接移过去
                    lists[int(position / 2)] = lists[count_now - 1]
                position += 2
            count_now = int((count_now + 1)/2)
        return lists[0] if len(lists) > 0 else None



l1 = ListUtil().creat_tree([1,4,7])
l2 = ListUtil().creat_tree([2,5,8])
l3 = ListUtil().creat_tree([3,6,9])
l = [l1, l2, l3]
a = Solution().mergeKLists(l)
print(a)


# leetcode submit region end(Prohibit modification and deletion)
