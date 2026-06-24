class Solution:
    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def maximumPrimeDifference(self, nums: List[int]) -> int:
        """ 返回数组中两个素数下标的最大距离 """
        prime_indices = [i for i, num in enumerate(nums) if self.is_prime(num)]
        if not prime_indices:
            return 0
        # 计算最大距离
        return prime_indices[-1] - prime_indices[0]
