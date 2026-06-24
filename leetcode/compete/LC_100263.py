class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        result = 0
        loop = x
        while loop > 0:
            num = loop % 10
            loop = loop // 10
            result += num
        if x % result == 0:
            return result
        else:
            return -1



print(Solution().sumOfTheDigitsOfHarshadNumber(18))