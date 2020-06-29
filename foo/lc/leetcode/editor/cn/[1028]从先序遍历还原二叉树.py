# We run a preorder depth first search on the root of a binary tree. 
# 
#  At each node in this traversal, we output D dashes (where D is the depth of t
# his node), then we output the value of this node. (If the depth of a node is D, 
# the depth of its immediate child is D+1. The depth of the root node is 0.) 
# 
#  If a node has only one child, that child is guaranteed to be the left child. 
# 
# 
#  Given the output S of this traversal, recover the tree and return its root. 
# 
#  
# 
#  Example 1: 
# 
#  
# 
#  
# Input: "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
#  
# 
#  
#  Example 2: 
# 
#  
# 
#  
# Input: "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7] 
#  
# 
#  
#  
# 
#  
#  Example 3: 
# 
#  
# 
#  
# Input: "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
#  
#  
# 
#  
# 
#  Note: 
# 
#  
#  The number of nodes in the original tree is between 1 and 1000. 
#  Each node will have a value between 1 and 10^9. 
#  
#  
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from foo.lc.TreeNode import TreeNode
from foo.lc.TreeUtil import TreeUtil


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:

        if not S:
            return None
        root = TreeNode(S[0])

        def my_split(line: str, reg: str):
            cut_point = []
            for i in range(1, len(line)):
                if line[i:i + len(reg)] == reg and line[i - 1].isnumeric() and line[i + len(reg)].isnumeric():
                    cut_point.append(i)
            if len(cut_point) == 1:
                return [line[0], line[cut_point[0] + len(reg):]]
            elif len(cut_point) == 2:
                return [line[0], line[cut_point[0] + len(reg):cut_point[1]], line[cut_point[1] + len(reg):]]

        def recur(father: TreeNode, sp: str, inner_str: str):
            if "-" not in inner_str:
                return
            str_list = my_split(inner_str, sp)
            left_str = str_list[1] if len(str_list) > 1 else None
            right_str = str_list[2] if len(str_list) > 2 else None
            if left_str:

                left_node = TreeNode(left_str[0])
                father.left = left_node
                recur(left_node, sp + "-", left_str)
            if right_str:
                right_node = TreeNode(right_str[0])
                father.right = right_node
                recur(right_node, sp + "-", right_str)

        recur(root, "-", S)
        return root


# a = Solution().recoverFromPreorder("1-2--3--4-5--6--7")
# a = Solution().recoverFromPreorder("1-2--3---4-5--6---7")
a = Solution().recoverFromPreorder("1-401--349---90--88")


# leetcode submit region end(Prohibit modification and deletion)
