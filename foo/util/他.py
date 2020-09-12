class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        count = 0
        result = ''
        for i in range(len(s) - 1, -1, -1):
            result = s[i] + result
            count += 1
            if count == 3 and i != 0:
                result = '.' + result
                count = 0
        return result


a = Solution().thousandSeparator(0)
print(a)