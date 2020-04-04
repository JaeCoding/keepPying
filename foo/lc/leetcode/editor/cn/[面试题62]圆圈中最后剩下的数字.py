# English description is not available for the problem. Please switch to Chinese
# . 
# 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # 最后幸存者的位置
        index = 0
        # 推算 每次补充 m人，并取余，就是上一轮幸存者的位置
        for i in range(2, n+1):
            index = (index + m) % i
        return index




# leetcode submit region end(Prohibit modification and deletion)
