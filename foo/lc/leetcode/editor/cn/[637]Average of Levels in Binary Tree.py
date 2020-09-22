# Given a non-empty binary tree, return the average value of the nodes on each l
# evel in the form of an array.
# 
#  Example 1: 
#  
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 
# 2 is 11. Hence return [3, 14.5, 11].
#  
#  
# 
#  Note: 
#  
#  The range of node's value is in the range of 32-bit signed integer. 
#  
#  Related Topics 树 
#  👍 176 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
from typing import List

from foo import TreeNode
from foo import TreeUtil


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        result = []
        q = queue.Queue()
        next_q = queue.Queue()
        sum = 0
        count = 0
        q.put(root)
        while not q.empty():
            node: TreeNode = q.get()
            sum += node.val
            count += 1
            if not node.left:
                next_q.put(node.left)
            if not node.right:
                next_q.put(node.right)

            if q.empty():
                result.append(sum/count)
                sum = 0
                count = 0
                q = next_q
                next_q = queue.Queue()
        return result

root = TreeUtil.creat_tree([3,9,20,15,7])
a = Solution().averageOfLevels(root)
print(a)


        
# leetcode submit region end(Prohibit modification and deletion)
