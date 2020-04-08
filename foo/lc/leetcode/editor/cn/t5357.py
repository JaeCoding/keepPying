from typing import List


class CustomStack:


    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.nowSize = 0
        self.List = []

    def push(self, x: int) -> None:
        if self.nowSize < self.maxSize:
            self.List.append(x)
            self.nowSize +=1

    def pop(self) -> int:
        if self.nowSize > 0:
            self.nowSize -= 1
            return self.List.pop()
        else:
            return -1


    def increment(self, k: int, val: int) -> None:
        end = min(k, self.nowSize)
        for i in range(0, end):
            self.List[i] = self.List[i] + val


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)):
            result.insert(index[i], nums[i])
        return result


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(1)
obj.push(2)
obj.pop()
obj.push(2)
obj.push(3)
obj.push(4)
obj.increment(5,100)