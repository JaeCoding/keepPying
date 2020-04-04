# Implement atoi which converts a string to an integer. 
# 
#  The function first discards as many whitespace characters as necessary until 
# the first non-whitespace character is found. Then, starting from this character,
#  takes an optional initial plus or minus sign followed by as many numerical digi
# ts as possible, and interprets them as a numerical value. 
# 
#  The string can contain additional characters after those that form the integr
# al number, which are ignored and have no effect on the behavior of this function
# . 
# 
#  If the first sequence of non-whitespace characters in str is not a valid inte
# gral number, or if no such sequence exists because either str is empty or it con
# tains only whitespace characters, no conversion is performed. 
# 
#  If no valid conversion could be performed, a zero value is returned. 
# 
#  Note: 
# 
#  
#  Only the space character ' ' is considered as whitespace character. 
#  Assume we are dealing with an environment which could only store integers wit
# hin the 32-bit signed integer range: [−231, 231 − 1]. If the numerical value is 
# out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is
#  returned. 
#  
# 
#  Example 1: 
# 
#  
# Input: "42"
# Output: 42
#  
# 
#  Example 2: 
# 
#  
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sig
# n.
#              Then take as many numerical digits as possible, which gets 42.
#  
# 
#  Example 3: 
# 
#  
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a nume
# rical digit.
#  
# 
#  Example 4: 
# 
#  
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numeric
# al 
#              digit or a +/- sign. Therefore no valid conversion could be perfo
# rmed. 
# 
#  Example 5: 
# 
#  
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed 
# integer.
#              Thefore INT_MIN (−231) is returned. 
#  Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31


class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans




class myAutomaton:
    def __init__(self):
        self.status = 'start'
        # 四种状态，及 ' '， '+/-'， '数字'， '其他'。的转移状态
        self.table = {
            'start': ['start', 'signed', 'number', 'end'],
            'signed': ['end', 'end', 'number', 'end'],
            'number': ['end', 'end', 'number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }
        self.sign = 1
        self.number = 0

    def changeStatus(self, s):
        self.status = self.table[self.status][self.translate(s)]
        if self.status == 'start':
            return
        elif self.status == 'signed':
            self.sign = -1 if s == '-' else 1
        elif self.status == 'number':
            self.number = self.number * 10 + int(s)
            self.number = min(self.number, INT_MAX) if self.sign == 1 else min(self.number, -INT_MIN) # 注意这里是 -INT_MIN 也就是正了
        else:
            return

    def translate(self, s) -> int:
        if s == ' ':
            return 0
        elif s == '+' or s == '-':
            return 1
        elif s.isnumeric():
            return 2
        else:
            return 3


class Solution2:
    def myAtoi(self, str: str) -> int:
        an = myAutomaton()
        for s in str:
            an.changeStatus(s)
        return an.sign * an.number

a = Solution2().myAtoi("1adasd")
a = Solution2().myAtoi("1-1")
print(a)


# leetcode submit region end(Prohibit modification and deletion)
