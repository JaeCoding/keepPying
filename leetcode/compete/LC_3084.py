"""
给你一个字符串 s 和一个字符 c 。返回在字符串 s 中并且以 c 字符开头和结尾的
非空子字符串
的总数。

示例 1：
输入：s = "abada", c = "a"
输出：6
解释：以 "a" 开头和结尾的子字符串有： "abada"、"abada"、"abada"、"abada"、"abada"、"abada"。

示例 2：
输入：s = "zzz", c = "z"
输出：6
解释：字符串 s 中总共有 6 个子字符串，并且它们都以 "z" 开头和结尾。

"""


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = 0
        for i in range(0, len(s)):
            if s[i] == c:
                for j in range(i, len(s)):
                    if s[j] == c:
                        count += 1
        return count


print(Solution().countSubstrings("abada", 'a'))
print(Solution().countSubstrings("zzz", 'z'))