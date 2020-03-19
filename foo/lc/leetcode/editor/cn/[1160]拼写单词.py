# You are given an array of strings words and a string chars. 
# 
#  A string is good if it can be formed by characters from chars (each character
#  can only be used once). 
# 
#  Return the sum of lengths of all good strings in words. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: 
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: 
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 
# = 10.
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= words.length <= 1000 
#  1 <= words[i].length, chars.length <= 100 
#  All strings contain lowercase English letters only. 
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        c_map = dict()
        for c in chars:
            c_map[c] = c_map[c] + 1 if c in c_map else 1

        def contain(word: str) -> bool:
            w_map = dict()
            for w in word:
                w_map[w] = w_map[w] + 1 if w in w_map else 1
            for k, v in w_map.items():
                if k not in c_map or v > c_map[k]:
                    return False
            return True

        length = 0
        for ww in words:
            if contain(ww):
                length += len(ww)
        return length



# leetcode submit region end(Prohibit modification and deletion)


# a = Solution().countCharacters(["cat","bt","hat","tree"],"atach")
a = Solution().countCharacters(["hello","world","leetcode"], "welldonehoneyr")
print(a)