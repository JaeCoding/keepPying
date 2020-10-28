# Given the array nums, for each nums[i] find out how many numbers in the array 
# are smaller than it. That is, for each nums[i] you have to count the number of v
# alid j's such that j != i and nums[j] < nums[i]. 
# 
#  Return the answer in an array. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= nums.length <= 500 
#  0 <= nums[i] <= 100 
#  
#  Related Topics 数组 哈希表 



# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        dict = collections.defaultdict(list)
        for i in range(len(nums)):
            dict[nums[i]].append(i)
        nums.sort()
        result = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i-1]:
                for j in dict[nums[i]]:
                    result[j] = i
        return result

a = Solution().smallerNumbersThanCurrent([8,1,2,2,3])
a = Solution().smallerNumbersThanCurrent([6,5,4,8])
a = Solution().smallerNumbersThanCurrent([7,7,7,7])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
