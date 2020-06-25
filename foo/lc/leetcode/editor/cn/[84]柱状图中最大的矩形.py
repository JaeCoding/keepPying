# Given n non-negative integers representing the histogram's bar height where th
# e width of each bar is 1, find the area of largest rectangle in the histogram. 
# 
#  
# 
#  
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3
# ]. 
# 
#  
# 
#  
# The largest rectangle is shown in the shaded area, which has area = 10 unit. 
# 
#  
# 
#  Example: 
# 
#  
# Input: [2,1,5,6,2,3]
# Output: 10
#  
#  Related Topics 栈 数组


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #  the max area of rectangle[i] is height * (i - j) (i represent the index of first lower one in left, and j to right)
        #  use monotonic(单调的) stack to store the left lower one, and when counter right higher, append it, otherwise calculate the area
        stack = [(0, -1)]  # for the dummy. height,index
        max_area = 0
        for i in range(len(heights) + 1):
            height = heights[i] if i < len(heights) else 0
            if height >= stack[len(stack) - 1][0]:
                stack.append((height, i))
            else:
                while stack[len(stack) - 1][0] > height:
                    last_height = stack.pop()[0]
                    last_index = stack[len(stack) - 1][1]  # the lower one index is top of stack
                    max_area = max(max_area, last_height * (i - last_index - 1))
                stack.append((height, i))
        return max_area



b = Solution().largestRectangleArea([2, 1, 4, 5, 6, 4, 3])
print(b)

# leetcode submit region end(Prohibit modification and deletion)
