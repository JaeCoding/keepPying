# English description is not available for the problem. Please switch to Chinese
# . Related Topics 栈 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class MaxQueue:
    """2个数组"""
    def __init__(self):
        self.queue = []
        # 维护一个队列 保存最大值到最小值
        self.max_stack = []

    def max_value(self) -> int:
        # queue的最大值
        return self.max_stack[0] if self.max_stack else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        # 保存次大值， 比如queue 4203  deque为4 -> 42 -> 420 -> 43
        while self.max_stack and self.max_stack[-1] < value:
            self.max_stack.pop()
        self.max_stack.append(value)

    def pop_front(self) -> int:
        if not self.queue: return -1
        ans = self.queue.pop(0)
        # 当出队数等于最大值时，deque才出队伍
        if ans == self.max_stack[0]:
            self.max_stack.pop(0)
        return ans



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
# leetcode submit region end(Prohibit modification and deletion)
