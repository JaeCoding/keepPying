from typing import List

from foo.lc.ListNode import ListNode


class ListUtil:
    def creat_tree(self, input: List[int]) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        for i in range(0, len(input)):
            node = ListNode(input[i])
            cur.next = node
            cur = cur.next
        return dummy.next


a = ListUtil().creat_tree([1, 2, 3])
