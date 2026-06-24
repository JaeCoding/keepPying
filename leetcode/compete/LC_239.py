from collections import deque

def maxSlidingWindow(nums, k):
    deq = deque()  # 存储索引
    res = []
    for i, n in enumerate(nums):
        # 移除窗口 左侧超出范围的索引
        while deq and deq[0] < i - k + 1:
            deq.popleft()
        # 移除队列中 所有小于当前元素的索引（因为不可能成为最大值）
        while deq and nums[deq[-1]] < n:
            deq.pop()
        deq.append(i)
        # 窗口形成后，添加当前最大值
        if i >= k - 1:
            res.append(nums[deq[0]])
    return res

# 示例
nums = [1,3,-1,-3,5,3,6,7]
k = 3
maxSlidingWindow(nums, k)
