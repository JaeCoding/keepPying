# Given a string, find the length of the longest substring without repeating cha
# racters. 
# 
#  
#  Example 1: 
# 
#  
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
#  
# 
#  
#  Example 2: 
# 
#  
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#  
# 
#  
#  Example 3: 
# 
#  
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence
#  and not a substring.
#  
#  
#  
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    # 直接一轮扫过去 是错误的解法 比如dvdf，不考虑前面的情况，会算出来是df 而不是 vdf

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        has = dict()
        pos = 0
        longest = 0
        now_count = 0
        while pos < len(s):
            if s[pos] not in has:
                now_count += 1
                has[s[pos]] = pos  # 记录下已有元素的位置
            else:
                pos = has[s[pos]]  # 游标返回此元素
                now_count = 0  # 计数清零
                has.clear()  # 记录位置清0
            pos += 1
            longest = max(longest, now_count)
        return longest

a = Solution().lengthOfLongestSubstring("asdasd")
print(a)

# leetcode submit region end(Prohibit modification and deletion)
