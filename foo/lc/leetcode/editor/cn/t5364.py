class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            result.insert(nums[i], index[i])
        return result