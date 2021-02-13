from typing import List

from foo.lc.leetcode.editor.TreeNode import TreeNode


class TreeUtil:
    @classmethod
    def creat_tree(self, input: List[str]) -> TreeNode:

        queue: List[TreeNode] = []
        flag = 'left'
        head = None
        for i in range(0, len(input)):
            node = TreeNode(input[i]) if (input[i] != 'null') else None
            if i == 0:
                head = node
            else:
                father = queue[0]
                if flag == 'left':
                    father.left = node
                    flag = 'right'
                elif flag == 'right':
                    father.right = node
                    flag = 'left'
                    del queue[0]
            if node:
                queue.append(node)

        return head


a = TreeUtil().creat_tree([1, 4, 4, 'null', 2, 2, 'null', 1, 'null', 6, 8, 'null', 'null', 'null', 'null', 1, 3])

