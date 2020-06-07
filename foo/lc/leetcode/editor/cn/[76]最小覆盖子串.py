# Given a string S and a string T, find the minimum window in S which will conta
# in all the characters in T in complexity O(n). 
# 
#  Example: 
# 
#  
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#  
# 
#  Note: 
# 
#  
#  If there is no such window in S that covers all characters in T, return the e
# mpty string "". 
#  If there is such window, you are guaranteed that there will always be only on
# e unique minimum window in S. 
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        visited = dict()
        min_len = 100000000
        l, r = 0, 0
        result_l, result_r = 0, 0
        change = False

        while r < len(s):
            # 发现是t元素
            item = s[r]
            if item in t:
                if len(visited) < len(t):  # 如果还没攒齐
                    visited[item] = visited[item] + 1 if item in visited else 1 # 计数
                    if len(visited) == 1: # 记录第一个l的位置
                        l = r

                else:  # 如果攒齐了，就 收缩左指针，到不能收缩为止，计算位置和长度
                    visited[item] = visited[item] + 1
                    while True:
                        l_item = s[l]
                        if l_item in t:
                            if visited[l_item] > 1:
                                visited[l_item] = visited[l_item] - 1
                            else:
                                break
                        l += 1

                if len(visited) == len(t) and r - l < min_len:
                    change = True
                    min_len = r - l
                    result_l, result_r = l, r
            r += 1
        return s[result_l:result_r + 1] if change else ""

from collections import Counter
from collections import defaultdict


class Solution2:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        ans = s + s  # 简单的取了两倍长度
        n = len(s)
        target = Counter(t)  # 总数map
        counter = defaultdict(lambda: 0)  # 计数map

        def contains(counter, target):
            """
            用于判断能否开始 左指针右移
            """
            if len(counter) < len(target):  # 简单判断 两者长度不等
                return False
            for k in counter:  # 仔细判断 长度等 但是内部元素数量还不够
                if k not in target or counter[k] < target[k]:
                    return False
            return True

        for r in range(n):
            if s[r] in target:
                counter[s[r]] += 1  # 计数+1
            while l < n and contains(counter, target):
                if r - l + 1 < len(ans):  # 更新结果
                    ans = s[l:r + 1]
                if s[l] in target:  # 右移后造成的 计数减少
                    counter[s[l]] -= 1
                l += 1
        return "" if ans == s + s else ans










# a = Solution().minWindow("ADOBECODEBANC", "ABC")
a = Solution().minWindow("AA", "AA")
print(a)





# leetcode submit region end(Prohibit modification and deletion)
