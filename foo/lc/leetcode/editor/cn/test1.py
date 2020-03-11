class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        cur = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        memo, res = {(0, 0, 0, 0, 0): 0}, 0
        for l, i in enumerate(s):
            # 如果是元音字母
            if i in cur:
                # 按位异或运算符：当两对应的二进位相异时，结果为1
                cur[i] ^= 1
            # 取cur
            key = tuple(v for k, v in cur.items())
            if key in memo:
                res = max(res, l - memo[key] + 1)
            else:
                memo[key] = l + 1
        return res


a = Solution().findTheLongestSubstring("eleetminicoworoep")
