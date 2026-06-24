"""
给你一个字符串 s ，请找出满足每个字符最多出现两次的最长子字符串，并返回该
子字符串
的 最大 长度。



示例 1：

输入： s = "bcbbbcba"

输出： 4

解释：

以下子字符串长度为 4，并且每个字符最多出现两次："bcbbbcba"。

示例 2：

输入： s = "aaaa"

输出： 2

解释：

以下子字符串长度为 2，并且每个字符最多出现两次："aaaa"。
"""

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left, max_length = 0, 0
        # counter
        char_count = {}
        for right in range(len(s)):
            count_right = char_count.get(s[right], 0) + 1
            char_count[s[right]] = count_right
            while char_count[s[right]] > 2:
                count_left = char_count.get(s[left])
                char_count[s[left]] = count_left - 1
                left += 1
                if count_left == 0:
                    del char_count[s[left]]

            max_length = max(max_length, right - left + 1)

        return max_length

a = Solution().maximumLengthSubstring("bcbbbcba")
a = Solution().maximumLengthSubstring("aaaa")
print(a)




