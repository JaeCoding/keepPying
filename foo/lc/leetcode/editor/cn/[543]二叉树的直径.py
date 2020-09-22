# 
# Given a binary tree, you need to compute the length of the diameter of the tre
# e. The diameter of a binary tree is the length of the longest path between any t
# wo nodes in a tree. This path may or may not pass through the root.
#  
# 
#  
# Example: 
# Given a binary tree 
#  
#           1
#          / \
#         2   3
#        / \     
#       4   5    
#  
#  
#  
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#  
# 
#  Note:
# The length of path between two nodes is represented by the number of edges bet
# ween them.
#  Related Topics 树


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from foo import TreeNode
from foo import TreeUtil


class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.m = 1
        # m=1通过记录节点数，m=0记录连接数, 节点数 - 1 = 连接数
        # 因为节点数最少是1， 连接数最少是0，

        def deep(node: TreeNode) -> int:
            if not node:
                return 0
            else:
                l = deep(node.left)
                r = deep(node.right)
                self.m = max(self.m, l + r + 1)
                return max(l, r) + 1

        deep(root)
        return self.m

    def diameterOfBinaryTree2(self, root):

        self.ans = 1

        def depth(node):
            # 访问到空节点了，返回0
            if not node: return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            # 用了一个变量 保存最大半径，这样只需要遍历考虑深度即可
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1


root = TreeUtil.creat_tree([])
a = Solution().diameterOfBinaryTree2(root)
print(a)

# leetcode submit region end(Prohibit modification and deletion)
