# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every
#  key of the original BST is changed to the original key plus sum of all keys gre
# ater than the original key in BST. 
# 
#  Example: 
# 
#  
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
# 
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13
#  
# 
#  Note: This question is the same as 1038: https://leetcode.com/problems/binary
# -search-tree-to-greater-sum-tree/ 
#  Related Topics 树 
#  👍 381 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from foo.lc.leetcode.editor.TreeNode import TreeNode
from foo.lc.leetcode.editor.TreeUtil import TreeUtil


class Solution:

    def convertBST(self, root: TreeNode) -> TreeNode:
        # 为每个节点维护一个大于其的数的和
        # maintain the sum of greater value for every node
        # maintain a sum of numbers greater than it for each node
        # sum are make up of two part : sum of father and sum of right son
        acc = [0]
        def mid_travel(node: TreeNode) -> int:
            if not node:
                return 0
            # calculate the
            mid_travel(node.right)
            node.val = str(int(node.val) + acc[0])
            acc[0] = int(node.val)
            print(node.val)
            mid_travel(node.left)

        def mid_travel(node: TreeNode) -> int:
            if not node:
                return 0
            mid_travel(node.right)
            node.val += acc[0]
            acc[0] = node.val
            mid_travel(node.left)


        mid_travel(root)
        return root




# root = TreeUtil.creat_tree(['4','2','6','1','3','5','7'])
# a = Solution().convertBST(root)

print(len("") == 0)
print(len("1") == 0)
print(len(None) == 0)


# leetcode submit region end(Prohibit modification and deletion)
