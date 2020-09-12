from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = 0
        nums.sort()
        while nums[-1] != 0:
            nums.sort()
            for i in range(len(nums)):
                if nums[i] % 2 != 0 and nums[i] != 0:
                    nums[i] -= 1
                    count += 1
            if nums[-1] == 0:
                break
            for i in range(len(nums)):
                nums[i] /= 2
            count += 1

        return count

a = Solution().minOperations([2,4,8,16])
a = Solution().minOperations([3,2,2,4])
print(a)