# A string S of lowercase English letters is given. We want to partition this st
# ring into as many parts as possible so that each letter appears in at most one p
# art, and return a list of integers representing the size of these parts. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it split
# s S into less parts.
#  
# 
#  
# 
#  Note: 
# 
#  
#  S will have length in range [1, 500]. 
#  S will consist of lowercase English letters ('a' to 'z') only. 
#  
# 
#  
#  Related Topics 贪心算法 双指针 
#  👍 344 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        # ababcbacadefegdehijhklij
        # first char is a, so we want find the max_index_of a (8)
        # in the loop, we should check if there are further char tha max_index larger than before
        # if so, we update the end to bigger
        # if not, continue until reach the end, and cut the array, record the length
        max_pos = {}
        for i in range(len(S)):
            max_pos[S[i]] = i
        #
        result = []
        start, end = 0, 0
        for i in range(len(S)):
            last_visited_of_i = max_pos[S[i]]
            end = max(end, last_visited_of_i)
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result

a = Solution().partitionLabels("ababcbacadefegdehijhklij")
print(a)
# merge last_index to i


# leetcode submit region end(Prohibit modification and deletion)
