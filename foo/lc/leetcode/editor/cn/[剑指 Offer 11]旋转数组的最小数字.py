# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2
# ] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。 
# 
#  示例 1： 
# 
#  输入：[3,4,5,1,2]
# 输出：1
#  
# 
#  示例 2： 
# 
#  输入：[2,2,2,0,1]
# 输出：0
#  
# 
#  注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sor
# ted-array-ii/ 
#  Related Topics 二分查找 
#  👍 117 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:

        left, right = 0, len(numbers) - 1

        while left < right:

            mid = (left + right) // 2
            # 如果中间 大于左边，则取右半部分
            if numbers[mid] > numbers[right]:
                left = mid + 1
            # 如果中间 小于坐标 则取左半部分
            elif numbers[mid] < numbers[right]:
                right = mid
            # 如果相同，无法判断 最小在左右哪边，只能一位一位缩减。比如[10,1,10,10,10]情况，
            else:
                # 两种情况都行，只能缩减一步
                # left += 1
                right -= 1
        return numbers[left]


# a = Solution().minArray([3,4,5,1,2])
a = Solution().minArray([2,2,2,0,1])
# a = Solution().minArray([2,2,2,0,1])
# a = Solution().minArray([1,2,3,5])
# a = Solution().minArray([3,1,3])
# a = Solution().minArray([10,1,10,10,10])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
