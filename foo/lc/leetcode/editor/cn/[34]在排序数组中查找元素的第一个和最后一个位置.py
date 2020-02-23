# Given an array of integers nums sorted in ascending order, find the starting a
# nd ending position of a given target value. 
# 
#  Your algorithm's runtime complexity must be in the order of O(log n). 
# 
#  If the target is not found in the array, return [-1, -1]. 
# 
#  Example 1: 
# 
#  
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4] 
# 
#  Example 2: 
# 
#  
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1] 
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binary_search(left, right) -> int:
            if left > right:
                return -1
            mid: int = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return binary_search(mid + 1, right)

        index = binary_search(0, len(nums)-1)
        start, end = index, index
        if index == -1:
            return [index, index]

        lr = index - 1
        # if the previous is equal target and in boundary (>=0)
        while lr >= 0 and nums[lr] == target:
            next_index = binary_search(0, lr)
            if next_index > -1:
                start = next_index
                lr = next_index - 1

        rl = index + 1
        # if the next is equal target and in boundary (<len)
        while rl < len(nums) and nums[rl] == target:
            next_index = binary_search(rl, len(nums) - 1)
            if next_index > 0:
                end = next_index
                rl = next_index + 1

        return [start, end]

        
# leetcode submit region end(Prohibit modification and deletion)


a = Solution().searchRange([1,1,2], 1)


print(a)