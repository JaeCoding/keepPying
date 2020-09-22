from foo import ListNode
from foo import ListUtil
from foo import TreeNode
from foo import TreeUtil


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:

        def dfs(node_t: TreeNode, node_l: ListNode):
            if node_t.val == node_l.val:
                if dfs2(node_t, node_l):
                    return True

            l = dfs(node_t.left, node_l) if node_t.left else False
            r = dfs(node_t.right, node_l) if node_t.right else False
            return l or r

        def dfs2(node_t: TreeNode, node_l: ListNode) -> bool:


            if node_t.val == node_l.val and node_l.next is None:
                return True
            elif node_t.val != node_l.val:
                return False
            else:
                l = dfs2(node_t.left, node_l.next) if node_t.left else False
                r = dfs2(node_t.right, node_l.next) if node_t.right else False
                return l or r

        return dfs(root, head)


r1 = TreeUtil().creat_tree([1, 4, 4, 'null', 2, 2, 'null', 1, 'null', 6, 8, 'null', 'null', 'null', 'null', 1, 3])
r2 = ListUtil().creat_tree([1,4,2,6,8])

a = Solution().isSubPath(r2, r1)
print(a)
