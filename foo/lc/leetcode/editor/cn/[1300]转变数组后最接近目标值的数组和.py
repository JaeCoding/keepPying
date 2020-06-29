# Given an integer array arr and a target value target, return the integer value
#  such that when we change all the integers larger than value in the given array 
# to be equal to value, the sum of the array gets as close as possible (in absolut
# e difference) to target. 
# 
#  In case of a tie, return the minimum such integer. 
# 
#  Notice that the answer is not neccesarilly a number from arr. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [4,9,3], target = 10
# Output: 3
# Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's th
# e optimal answer.
#  
# 
#  Example 2: 
# 
#  
# Input: arr = [2,3,5], target = 10
# Output: 5
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [60864,25176,27249,21296,20204], target = 56803
# Output: 11361
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 10^4 
#  1 <= arr[i], target <= 10^5 
#  
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:

        # 目的： 找到一个数a，使得arr中大于a的数，都变成a，然后sum离target最近
        # 排序后 从小到大开始找这个数，并且使得下标 t - (0-i) 的平均值 离这个数 最近
        arr.sort()
        i_sum = 0  # 前i个数的汇总
        for i in range(len(arr)):
            cur_average = (target - i_sum) // (len(arr) - i)   # 减去前i部分和，并计算后部分我们期望的平均值，
            # 取整是因为要找一个恰好大于等于arr[i]的数
            if cur_average <= arr[i]:  # 说明 让i后面的所有数 变成 arr[i], 是可以使得离target最近的
                cur_average_double = (target - i_sum) / (len(arr) - i)  # 对比小数部分
                if cur_average_double - cur_average <= 0.5:
                    return cur_average
                else:
                    return cur_average + 1  # 进一位
            i_sum += arr[i]
        return arr[len(arr) - 1]  # 题目要求将数组中所有大于 value 的值变成 value 后，所以只能取最大数，让数组不减少

a = Solution().findBestValue([40091,2502,74024,53101,60555,33732,23467,40560,32693,13013], 78666)
print(a)

# leetcode submit region end(Prohibit modification and deletion)
