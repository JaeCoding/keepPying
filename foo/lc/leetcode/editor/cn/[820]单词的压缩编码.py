# Given a list of words, we may encode it by writing a reference string S and a 
# list of indexes A. 
# 
#  For example, if the list of words is ["time", "me", "bell"], we can write it 
# as S = "time#bell#" and indexes = [0, 2, 5]. 
# 
#  Then for each index, we will recover the word by reading from the reference s
# tring from that index until we reach a "#" character. 
# 
#  What is the length of the shortest reference string S possible that encodes t
# he given words? 
# 
#  Example: 
# 
#  
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: S = "time#bell#" and indexes = [0, 2, 5].
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= words.length <= 2000. 
#  1 <= words[i].length <= 7. 
#  Each word has only lowercase letters. 
#  
# 


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        N = len(words)
        # 逆序字典序排序
        words.sort(key=lambda word: word[::-1])

        res = 0
        for i in range(N):
            if i + 1 < N and words[i + 1].endswith(words[i]):
                # 当前单词是下一个单词的后缀，丢弃
                pass
            else:
                res += len(words[i]) + 1  # 单词加上一个 '#' 的长度

        return res


a = Solution().minimumLengthEncoding(["me", "time", "ti", "bel"])
print(a)

# leetcode submit region end(Prohibit modification and deletion)
