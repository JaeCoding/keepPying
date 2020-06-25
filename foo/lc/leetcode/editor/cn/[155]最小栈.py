# Design a stack that supports push, pop, top, and retrieving the minimum elemen
# t in constant time. 
# 
#  
#  push(x) -- Push element x onto stack. 
#  pop() -- Removes the element on top of the stack. 
#  top() -- Get the top element. 
#  getMin() -- Retrieve the minimum element in the stack. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# 
# Output
# [null,null,null,null,-3,null,0,-2]
# 
# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
#  
# 
#  
#  Constraints: 
# 
#  
#  Methods pop, top and getMin operations will always be called on non-empty sta
# cks. 
#  
#  Related Topics 栈 设计


# leetcode submit region begin(Prohibit modification and deletion)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.base = []
        self.help = []


    def push(self, x: int) -> None:
        self.base.append(x)
        if not self.help or x <= self.help[-1]:
            self.help.append(x)
        else:
            self.help.append(self.help[-1])

    def pop(self) -> None:
        self.help.pop()
        return self.base.pop()

    def top(self) -> int:
        return self.base[-1]

    def getMin(self) -> int:
        return self.help[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# leetcode submit region end(Prohibit modification and deletion)
