# English description is not available for the problem. Please switch to Chinese
# . 
# 


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret = 0  # 所有数字异或的结果
        a = 0
        b = 0
        for n in nums:
            ret ^= n

        # 从低到高 找到第一位不是0的二进制位的对应位数
        h = 1
        while ret & h == 0:  # AND 两个操作数相应的比特位都是1时，结果才为1，否则为0。
            h <<= 1  # 左移，右边填充0
        # 最终h为类似 10000

        for n in nums:
            # 根据该位是否为0将其分为两组
            # 两个不同数一定会分到不同组，因为他们的第h位一定不一样
            # （因为h是ret的第一个1位，而第一个1位，是有a,b异或得来，只有此位不同的亦或才会得到1）
            if h & n == 0:  # 如果第h位 对应是 0 分到一组，并求亦或
                a ^= n
            else:
                b ^= n  # 如果第h位 对应是1 分到一组 并求亦或

        return [a, b]


# leetcode submit region end(Prohibit modification and deletion)
