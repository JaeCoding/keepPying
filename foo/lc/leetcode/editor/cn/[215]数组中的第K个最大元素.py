# Find the kth largest element in an unsorted array. Note that it is the kth lar
# gest element in the sorted order, not the kth distinct element. 
# 
#  Example 1: 
# 
#  
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#  
# 
#  Example 2: 
# 
#  
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4 
# 
#  Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length. 
#  Related Topics 堆 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # to find kth largest equals to 
        

        # partition
        def partition(left, right):
            i, j = left + 1, right
            v = nums[left]
            while True:
                while nums[i] <= v:
                    i += 1
                    if i >= right: 
                        break
                while nums[j] >= v:
                    j -= 1
                    if j <= left:
                        break
                if i >= j:
                    break
                # swap i j
                nums[i], nums[j] = nums[j], nums[i]
            # swap first and j    
            nums[left], nums[j] = nums[j], nums[left]
            return j   
        
        l, r = 0, len(nums) - 1
        while True:
            if l == r:
                return nums[l]
            mid = partition(l, r)
            if r - mid + 1 > k:
                l, r = mid + 1, r
            elif r - mid + 1 < k:
                k -= r - mid + 1
                l, r = l, mid - 1
            else:
                return nums[mid]
                
            
# a = Solution().findKthLargest([3,2,1,5,6,4], 2)
# a = Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4)
# a = Solution().findKthLargest([7,6,5,4,3,2,1],2)
a = Solution().findKthLargest([3,3,3,3,3,3,3,3,3],1)
# a = Solution().findKthLargest([-1,-1], 2)
# a = Solution().findKthLargest([1], 1)
print(a)

# leetcode submit region end(Prohibit modification and deletion)
