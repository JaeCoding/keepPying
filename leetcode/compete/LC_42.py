from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [height[0]] * n
        right = [height[n - 1]] * n
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        for i in range(n-2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        ans = 0
        for i in range(n):
            ans += min(left[i], right[i]) - height[i]
        return ans

a = Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(a)