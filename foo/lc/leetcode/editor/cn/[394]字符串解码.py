# Given an encoded string, return its decoded string. 
# 
#  The encoding rule is: k[encoded_string], where the encoded_string inside the 
# square brackets is being repeated exactly k times. Note that k is guaranteed to 
# be a positive integer. 
# 
#  You may assume that the input string is always valid; No extra white spaces, 
# square brackets are well-formed, etc. 
# 
#  Furthermore, you may assume that the original data does not contain any digit
# s and that digits are only for those repeat numbers, k. For example, there won't
#  be input like 3a or 2[4]. 
# 
#  Examples: 
# 
#  
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
#  
# 
#  
#  Related Topics 栈 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def decodeString(self, s: str) -> str:
        final_res = ''
        res = ''
        multi = 0
        stack = []
        for c in s:
            if "0" <= c <= '9':
                multi = multi * 10 + int(c)
            elif c.isalpha():
                res += c
            elif c == '[':
                stack.append((multi, res))
                res = ''
                multi = 0
            elif c == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + res * cur_multi
        return res


a = Solution().decodeString("2[abc]3[cd]ef")
print(a)
# leetcode submit region end(Prohibit modification and deletion)
