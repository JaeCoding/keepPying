# English description is not available for the problem. Please switch to Chinese
# .


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        def getBitSum(num: int):
            sum = 0
            while num > 0:
                sum += num % 10
                num = int(num / 10)
            return sum
        total = 0
        for i in range(m):
            for j in range(n):
                if getBitSum(i) + getBitSum(j) <= k:
                    print((i,j))
                    total += 1
        return total



a = Solution().movingCount(16,8,4)
print(a)
# leetcode submit region end(Prohibit modification and deletion)
