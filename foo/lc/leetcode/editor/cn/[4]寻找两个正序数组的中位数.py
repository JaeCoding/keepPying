# There are two sorted arrays nums1 and nums2 of size m and n respectively. 
# 
#  Find the median of the two sorted arrays. The overall run time complexity sho
# uld be O(log (m+n)). 
# 
#  You may assume nums1 and nums2 cannot be both empty. 
# 
#  Example 1: 
# 
#  
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
#  
# 
#  Example 2: 
# 
#  
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
#  
#  Related Topics 数组 二分查找 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 使得长的List， 始终处在在num2位置上
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        infinty = 2**40
        m, n = len(nums1), len(nums2)
        left, right, ansi = 0, m, -1
        # median1：前一部分的最大值
        # median2：后一部分的最小值
        median1, median2 = 0, 0

        while left <= right:
            # 前一部分包含 nums1[0 .. i-1] 和 nums2[0 .. j-1]
            # // 后一部分包含 nums1[i .. m-1] 和 nums2[j .. n-1]
            i = (left + right) // 2  # // 就是正常的取余，不用int搞
            j = (m + n + 1) // 2 - i  # 用减法计算，而不是len2给除出来

            # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            nums_im1 = (-infinty if i == 0 else nums1[i - 1])
            nums_i = (infinty if i == m else nums1[i])
            nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
            nums_j = (infinty if j == n else nums2[j])

            if nums_im1 <= nums_j:
                ansi = i
                median1, median2 = max(nums_im1, nums_jm1), min(nums_i, nums_j)
                left = i + 1
            else:
                right = i - 1

        return (median1 + median2) / 2 if (m + n) % 2 == 0 else median1


a = Solution().findMedianSortedArrays([1,2,3,4], [5,6,7])


# leetcode submit region end(Prohibit modification and deletion)
