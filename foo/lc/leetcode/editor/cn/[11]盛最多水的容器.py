# Given n non-negative integers a1, a2, ..., an , where each represents a point 
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
#  line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis for
# ms a container, such that the container contains the most water. 
# 
#  Note: You may not slant the container and n is at least 2. 
# 
#  
# 
#  
# 
#  The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In thi
# s case, the max area of water (blue section) the container can contain is 49. 
# 
#  
# 
#  Example: 
# 
#  
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49 Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # 取原有 和 移动后的最大值
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            # 如果左边小 左指针右移
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area


a = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(a)




# leetcode submit region end(Prohibit modification and deletion)
