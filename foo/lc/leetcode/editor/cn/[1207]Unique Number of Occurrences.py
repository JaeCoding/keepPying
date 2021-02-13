# Given an array of integers arr, write a function that returns true if and only
#  if the number of occurrences of each value in the array is unique. 
# 
#  
#  Example 1: 
# 
#  
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values
#  have the same number of occurrences. 
# 
#  Example 2: 
# 
#  
# Input: arr = [1,2]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= arr.length <= 1000 
#  -1000 <= arr[i] <= 1000 
#  
#  Related Topics 哈希表 
#  👍 94 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = collections.defaultdict(int)
        for item in arr:
            dict[item] += 1
        visited = set()
        for (k, v) in dict.items():
            if v in visited:
                return False
            visited.add(v)
        return True
a = Solution().uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
a = Solution().uniqueOccurrences([1,2,2,1,1,3])
a = Solution().uniqueOccurrences([1,2])
print(a)

        
# leetcode submit region end(Prohibit modification and deletion)
