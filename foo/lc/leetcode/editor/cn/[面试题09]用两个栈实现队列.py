# English description is not available for the problem. Please switch to Chinese
# . Related Topics 栈 设计


# leetcode submit region begin(Prohibit modification and deletion)
class CQueue:

    def __init__(self):
        self.stack_in: list = list()
        self.stack_out: list = list()

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)


    def deleteHead(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        else:
            if not self.stack_in:
                return -1
            else:
                # put element from in_stack to out_stack
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())
                return self.stack_out.pop()

# Your CQueue object will be instantiated and called as such:
obj = CQueue()
obj.appendTail(1)
obj.appendTail(2)
obj.appendTail(3)
param_2 = obj.deleteHead()
print(param_2)
obj.appendTail(4)
obj.appendTail(5)
param_2 = obj.deleteHead()
print(param_2)
param_2 = obj.deleteHead()
print(param_2)
param_2 = obj.deleteHead()
print(param_2)
param_2 = obj.deleteHead()
print(param_2)
param_2 = obj.deleteHead()
print(param_2)
param_2 = obj.deleteHead()
print(param_2)
param_2 = obj.deleteHead()
print(param_2)
param_2 = obj.deleteHead()
print(param_2)
# leetcode submit region end(Prohibit modification and deletion)
