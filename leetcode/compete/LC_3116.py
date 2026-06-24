from typing import List


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        combine = []
        for coin in coins:
            for i in range(1, k + 1):
                kth = i * coin
                if kth not in combine:
                    combine.append(kth)
        combine.sort()
        return combine[k-1]


a = Solution().findKthSmallest([3,6,9], 3)
print(a)
