# Given a binary tree, we install cameras on the nodes of the tree. 
# 
#  Each camera at a node can monitor its parent, itself, and its immediate child
# ren. 
# 
#  Calculate the minimum number of cameras needed to monitor all nodes of the tr
# ee. 
# 
#  
# 
#  Example 1: 
# 
#  
#  
# Input: [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the tree.
#  The above image shows one of the valid configurations of camera placement.
#  
# 
#  
# Note: 
# 
#  
#  The number of nodes in the given tree will be in the range [1, 1000]. 
#  Every node has value 0. 
#  
#  
#  
#  Related Topics 树 深度优先搜索 动态规划 
#  👍 196 👎 0


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
    def minCameraCover(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1

        def dfs(node: TreeNode):
            if not node:
                return [0, 0]  # 表示选与没选的已用数量
            # left
            [left_use_count, left_not_count] = dfs(node.left)
            [right_use_count, right_not_count] = dfs(node.right)
            # 1 mean light this, then add left_not and right_not
            # 0 mean not light this node, should light left and right same times
            return [1 + left_not_count + right_not_count, 0 + left_use_count + right_use_count]

        b = dfs(root)
        return min(b)

    def minCameraCover(self, root: TreeNode) -> int:

        self.res = 0

        def lrd(node):
            if node is None:
                return 1  # 空节点不需要被人拍也不用拍别人，直接返回被拍了就好
            left = lrd(node.left)
            right = lrd(node.right)
            if left == 0 or right == 0:
                # 如果左儿子或者右儿子需要被拍，我就装个摄像机
                self.res += 1
                return 2
            if left == 2 or right == 2:
                # 如果左儿子或者右儿子装了摄像机，那我就被拍了
                return 1
            else:  # left == 1 and right == 1:
                # 如果左儿子和右儿子都是被拍的，都没有摄像机，那我就是需要被拍的状态
                return 0

        if lrd(root) == 0:
            ##看看根节点是不是需要被拍
            self.res += 1
        return self.res


# root = TreeUtil.creat_tree([1,2,'null',3,'null',4,'null','null',5])
# root = TreeUtil.creat_tree([0,0,'null',0,0])
# root = TreeUtil.creat_tree([0])
# root = TreeUtil.creat_tree([1,2,3,'null','null','null',4])
root = TreeUtil.creat_tree([1, 2, 3, 'null', 'null', 'null', 4])
a = Solution().minCameraCover(root)
print(a)

# leetcode submit region end(Prohibit modification and deletion)
