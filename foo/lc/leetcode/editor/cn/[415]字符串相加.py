# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。 
# 
#  
# 
#  提示： 
# 
#  
#  num1 和num2 的长度都小于 5100 
#  num1 和num2 都只包含数字 0-9 
#  num1 和num2 都不包含任何前导零 
#  你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式 
#  
#  Related Topics 字符串 
#  👍 244 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 让num1 始终为长者
        if len(num1) < len(num2):
            tmp = num1
            num1 = num2
            num2 = tmp

        # 填补空缺
        for i in range(len(num1) - len(num2)):
            num2 = '0' + num2

        remainder = 0
        carry = 0
        result = ''
        for i in range(len(num1) - 1, -1, -1):
            # 余数
            remainder = (carry + int(num1[i]) + int(num2[i])) % 10
            # 进位
            carry = (carry + int(num1[i]) + int(num2[i])) // 10
            result = str(remainder) + result
        return result if carry == 0 else str(carry) + result

a = Solution().addStrings("9", "0")
print(a)



# leetcode submit region end(Prohibit modification and deletion)
