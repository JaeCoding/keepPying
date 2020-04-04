# Given n non-negative integers representing an elevation map where the width of
#  each bar is 1, compute how much water it is able to trap after raining. 
# 
#  
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In 
# this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos
#  for contributing this image! 
# 
#  Example: 
# 
#  
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6 
#  Related Topics 栈 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # 解法一：逐列找左右，看此列能存多少水.  复杂度 O(n^2) 超时
    def trap(self, height: List[int]) -> int:
        sum = 0
        for i in range(1, len(height) - 1):
            now_height = height[i]
            left_height = 0
            right_height = 0
            for l in range(i-1, -1, -1):
                left_height = max(left_height, height[l])
            for r in range(i+1, len(height)):
                right_height = max(right_height, height[r])
            sum += min(left_height, right_height) - now_height if now_height < min(left_height, right_height) else 0
        return sum

    #解法二：解法1的优化。用两个数组记录，左右最高高度。避免重复计算。  时间复杂度O(n) 空间复杂度O(n)
    def trap2(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        sum = 0
        for i in range(1,len(height)):
            left_max[i] = max(left_max[i-1], height[i-1])
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])
        for i in range(1, len(height) - 1):
            now_height = height[i]
            left_height = left_max[i]
            right_height = right_max[i]
            sum += min(left_height, right_height) - now_height if now_height < min(left_height, right_height) else 0
        return sum

    #解法3：对解法2的优化，因为两个数组中元素其实只使用了一次
    def trap3(self, height: List[int]) -> int:
        sum = 0
        left_max = 0
        right_max = 0
        now_left = 0
        now_right = len(height) - 1
        # 左右开弓，记录一个 当前左最高 与 当前右最高， 那边小就消耗哪边，因为增加量 只受两遍最小值影响
        while now_left <= now_right:
            # 消费左边
            if left_max < right_max:
                if height[now_left] < left_max:
                    sum += left_max - height[now_left]
                else:
                    left_max = height[now_left]
                now_left += 1
            # 消费右边
            else:
                if height[now_right] < right_max:
                    sum += right_max - height[now_right]
                else:
                    right_max = height[now_right]
                now_right -= 1
        return sum





a = Solution().trap3([1,0,3])
a = Solution().trap3([0,1,0,2,1,0,1,3,2,1,2,1])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
