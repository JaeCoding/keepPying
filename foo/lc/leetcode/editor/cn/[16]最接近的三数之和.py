# Given an array nums of n integers and an integer target, find three integers i
# n nums such that the sum is closest to target. Return the sum of the three integ
# ers. You may assume that each input would have exactly one solution. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= nums.length <= 10^3 
#  -10^3 <= nums[i] <= 10^3 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_gap = 10000000000
        result = nums[0] + nums[1] + nums[2]
        for i in range(0, len(nums) - 2):
            a = nums[i]
            t = target - a
            l_point, r_point = i + 1, len(nums) - 1
            while l_point < r_point:
                # update the min gap
                now = a + nums[l_point] + nums[r_point]
                if abs(target - now) < min_gap:
                    result = now
                    min_gap = abs(target - now)
                if nums[l_point] + nums[r_point] < t:
                    l_point += 1
                elif nums[l_point] + nums[r_point] > t:
                    r_point -= 1
                else:
                    return target
        return result

# a = Solution().threeSumClosest([-1,2123123,1,-4], 1)
a = Solution().threeSumClosest([1,1,1,1], 0)
# a = Solution().threeSumClosest([-100,-98,-2,-1], -101)
print(a)



# leetcode submit region end(Prohibit modification and deletion)
