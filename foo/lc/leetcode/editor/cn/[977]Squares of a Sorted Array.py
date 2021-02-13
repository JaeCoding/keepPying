# Given an array of integers A sorted in non-decreasing order, return an array o
# f the squares of each number, also in sorted non-decreasing order. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= A.length <= 10000 
#  -10000 <= A[i] <= 10000 
#  A is sorted in non-decreasing order. 
#  
#  
#  Related Topics 数组 双指针 
#  👍 160 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        def get_closet_index_of_num(nums, target):
            left, right = 0, len(nums) - 1
            while left + 1 < right:
                mid = int((left + right) / 2)
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid
                else:
                    left = mid
            if abs(nums[left] - target) <= abs(nums[right] - target):
                return left
            else:
                return right

        point = get_closet_index_of_num(A, 0)
        out = []
        l1, r1 = point, point
        out.append(A[point] ** 2)
        while l1 - 1 >= 0 or r1 + 1 < len(A):
            # 基于下一个位置存在 而判断
            if l1 - 1 >= 0 and r1 + 1 < len(A):
                if A[l1-1] ** 2 <= A[r1+1] ** 2:
                    l1 -= 1
                    out.append(A[l1] ** 2)
                else:
                    r1 += 1
                    out.append(A[r1] ** 2)
            elif l1 - 1 >= 0:
                l1 -= 1
                out.append(A[l1] ** 2)
            elif r1 + 1 < len(A):
                r1 += 1
                out.append(A[r1] ** 2)
        return out


# a = Solution().sortedSquares([-7,-3,2,3,11])
# a = Solution().sortedSquares([-1,2,2])
# a = Solution().sortedSquares([-4,0,1,1])
# a = Solution().sortedSquares([-4, -1, 0, 3, 10])
print(a)
# leetcode submit region end(Prohibit modification and deletion)
