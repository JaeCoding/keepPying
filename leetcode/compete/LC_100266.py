from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    dp[i][j] = 1
                elif i < j:
                    if nums[j] != nums[j-1]:
                        dp[i][j] = dp[i][j-1] + 1
                    else:
                        dp[i][j] = dp[i][j - 1]




        print(dp)
        print(dp[0][n-1])


Solution().countAlternatingSubarrays([1,0,1,0])