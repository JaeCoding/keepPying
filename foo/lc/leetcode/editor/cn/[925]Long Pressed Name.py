# Your friend is typing his name into a keyboard. Sometimes, when typing a chara
# cter c, the key might get long pressed, and the character will be typed 1 or mor
# e times. 
# 
#  You examine the typed characters of the keyboard. Return True if it is possib
# le that it was your friends name, with some characters (possibly none) being lon
# g pressed. 
# 
#  
#  Example 1: 
# 
#  
# Input: name = "alex", typed = "aaleex"
# Output: true
# Explanation: 'a' and 'e' in 'alex' were long pressed.
#  
# 
#  Example 2: 
# 
#  
# Input: name = "saeed", typed = "ssaaedd"
# Output: false
# Explanation: 'e' must have been pressed twice, but it wasn't in the typed outp
# ut.
#  
# 
#  Example 3: 
# 
#  
# Input: name = "leelee", typed = "lleeelee"
# Output: true
#  
# 
#  Example 4: 
# 
#  
# Input: name = "laiden", typed = "laiden"
# Output: true
# Explanation: It's not necessary to long press any character.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= name.length <= 1000 
#  1 <= typed.length <= 1000 
#  The characters of name and typed are lowercase letters. 
#  
#  Related Topics 双指针 字符串 
#  👍 149 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        p1, p2 = 0, 0
        while p1 < len(name) and p2 < len(typed):
            # name = "saeed", typed = "ssaaedd"
            # name = "ssaeed", typed = "ssaaedd"
            if name[p1] == typed[p2]:
                if p1 + 1 < len(name) and p2 + 1 < len(typed) and name[p1 + 1] == typed[p2 + 1]:
                    p1 += 1
                    p2 += 1
                    continue
                    # next is differ, enter inner loop of reinput
                else:
                    while p2 + 1 < len(typed) and typed[p2] == typed[p2 + 1]:
                        p2 += 1
                p1 += 1
                p2 += 1
            else:
                return False
        if p1 == len(name) and p2 == len(typed):
            return True
        else:
            return False


# a = Solution().isLongPressedName("saeed", "ssaaedd")
# a = Solution().isLongPressedName("alex", "aaleex")
# a = Solution().isLongPressedName("leelee", "lleeelee")
a = Solution().isLongPressedName("laiden", "laiden")
a = Solution().isLongPressedName("laid", "laidennnn")
print(a)
# leetcode submit region end(Prohibit modification and deletion)
