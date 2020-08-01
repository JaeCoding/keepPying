# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。 
# 
#  注意: 
# 数组长度 n 满足以下条件: 
# 
#  
#  1 ≤ n ≤ 1000 
#  1 ≤ m ≤ min(50, n) 
#  
# 
#  示例: 
# 
#  
# 输入:
# nums = [7,2,5,10,8]
# m = 2
# 
# 输出:
# 18
# 
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
#  
#  Related Topics 二分查找 动态规划 
#  👍 278 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        def group(mid):
            """
            :param mid: 每组的和的最大值
            :return:
            """
            sums, cnt = 0, 1
            for i in nums:
                # 发现当前分组和超过mid
                if sums + i > mid:
                    # 重起一组，计数加一，重置当前和为当前数
                    cnt += 1
                    sums = i
                else:
                    sums += i
            return cnt

        # 二分，若分成len组，下界为 数组中的最大值；若分成1组，则上界为 全部和，记录其为期待值x
        left, right = max(nums), sum(nums)
        while left < right:
            # 让 x 为上下界中位数
            mid = (left + right) // 2
            sums, cnt = 0, 1
            # group(mid) 为 数组和最大值最小情况 对应的组数
            if group(mid) <= m:
                # 发现分出来的组 少了 说明x取大了，则要少取一点，让上界变为mid
                right = mid
            else:
                # 发现分出来的组 多了 说明x取小了，则要多取一点，让下界变为mid + 1
                left = mid + 1
        return left

# leetcode submit region end(Prohibit modification and deletion)
