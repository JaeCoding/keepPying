# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the 
# coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its t
# op-right corner. 
# 
#  Two rectangles overlap if the area of their intersection is positive. To be c
# lear, two rectangles that only touch at the corner or edges do not overlap. 
# 
#  Given two (axis-aligned) rectangles, return whether they overlap. 
# 
#  Example 1: 
# 
#  
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
#  
# 
#  Example 2: 
# 
#  
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
#  
# 
#  Notes: 
# 
#  
#  Both rectangles rec1 and rec2 are lists of 4 integers. 
#  All coordinates in rectangles will be between -10^9 and 10^9. 
#  
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        # 对于二维判断 重叠的情况有 部分重叠*2 包含重叠*2 而不重叠只有 左右分离*2 显然不重叠更好书写
        x_match = not (rec1[0] >= rec2[2] or rec2[0] >= rec1[2])
        y_match = not (rec1[1] >= rec2[3] or rec2[1] >= rec1[3])
        return y_match and x_match


# a = Solution().isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3])
a = Solution().isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1])
# a = Solution().isRectangleOverlap([0, 0, 3, 3], [1, 1, 2, 2])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
