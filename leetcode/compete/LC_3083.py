class Solution:
    def checkIfExistSubstring(self, s: str) -> bool:
        # Edge case: 字符串长度小于2，直接返回False
        if len(s) < 2:
            return False
        # 遍历字符串，直到倒数第二个字符
        for i in range(len(s) - 1):
            # 提取当前字符和下一个字符组成的子字符串
            sub_string = s[i:i + 2]
            # 检查子字符串的反转是否在原字符串中
            if sub_string[::-1] in s:
                return True
        # 如果没有找到符合条件的子字符串，返回False
        return False

    def test_cases(self):
        # 测试用例1
        assert self.checkIfExistSubstring("leetcode") == True
        # 测试用例2
        assert self.checkIfExistSubstring("abcba") == True
        # 测试用例3
        assert self.checkIfExistSubstring("abcd") == False

# 实例化Solution类
solution = Solution()
# 调用测试用例方法
solution.test_cases()
