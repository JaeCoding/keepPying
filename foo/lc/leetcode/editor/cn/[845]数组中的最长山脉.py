# 我们把数组 A 中符合下列属性的任意连续子数组 B 称为 “山脉”： 
# 
#  
#  B.length >= 3 
#  存在 0 < i < B.length - 1 使得 B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B
# [B.length - 1] 
#  
# 
#  （注意：B 可以是 A 的任意子数组，包括整个数组 A。） 
# 
#  给出一个整数数组 A，返回最长 “山脉” 的长度。 
# 
#  如果不含有 “山脉” 则返回 0。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[2,1,4,7,3,2,5]
# 输出：5
# 解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
#  
# 
#  示例 2： 
# 
#  输入：[2,2,2]
# 输出：0
# 解释：不含 “山脉”。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= A.length <= 10000 
#  0 <= A[i] <= 10000 
#  
#  Related Topics 双指针 
#  👍 138 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        longest = 0
        # 关键 从1开始 与上一个做比较
        i = 1
        while i < len(A):
            # 将计数清零
            increasing, decreasing = 0, 0
            # 找到上升阶段最长
            while i < len(A) and A[i - 1] < A[i]:
                i += 1
                increasing += 1
            # 找到下降阶段最长
            while i < len(A) and A[i - 1] > A[i]:
                i += 1
                decreasing += 1
            # 计算长度
            if increasing > 0 and decreasing > 0:
                longest = max(longest, increasing + decreasing + 1)
            # 如果i与上个位置相同
            while i < len(A) and A[i - 1] == A[i]:
                i += 1
            # 其他情况则表示清零 循环
        return longest

# a = Solution().longestMountain([2,1,4,7,3,2,5])
# a = Solution().longestMountain([2,2,2])
# a = Solution().longestMountain([875,884,239,731,723,685])
# a = Solution().longestMountain([0,0,1,0,0,1,1,1,1,1])
# a = Solution().longestMountain([0,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1])
a = Solution().longestMountain([3,2])
print(a)


# leetcode submit region end(Prohibit modification and deletion)
