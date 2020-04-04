# Given an array of integers nums, sort the array in ascending order. 
# 
#  
#  Example 1: 
#  Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
#  Example 2: 
#  Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 50000 
#  -50000 <= nums[i] <= 50000 
#  
# 


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def sort(left:int , right:int):
            if left >= right:
                return
            mid = partition(left, right)
            sort(left, mid-1)
            sort(mid + 1, right)

        def partition(left: int, right:int) -> int:
            i,j = left+1, right
            p = nums[left]
            while True:
                while nums[i] < p:
                    i += 1
                    if i >= right:
                        break
                while nums[j] > p:
                    j -= 1
                    if j <= left:
                        break
                if i >= j:
                    break
                exch(i,j)
            exch(left, j)
            return j

        def exch(i: int, j:int):
            tem = nums[i]
            nums[i] = nums[j]
            nums[j] = tem
            # nums[i] = nums[i] ^ nums[j]
            # nums[j] = nums[j] ^ nums[i]
            # nums[i] = nums[i] ^ nums[j]

        sort(0, len(nums) - 1)
        return nums


a = Solution().sortArray([5,2,3,1])
print(a)
# leetcode submit region end(Prohibit modification and deletion)
