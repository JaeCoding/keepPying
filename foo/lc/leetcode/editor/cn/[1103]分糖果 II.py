# We distribute some number of candies, to a row of n = num_people people in the
#  following way: 
# 
#  We then give 1 candy to the first person, 2 candies to the second person, and
#  so on until we give n candies to the last person. 
# 
#  Then, we go back to the start of the row, giving n + 1 candies to the first p
# erson, n + 2 candies to the second person, and so on until we give 2 * n candies
#  to the last person. 
# 
#  This process repeats (with us giving one more candy each time, and moving to 
# the start of the row after we reach the end) until we run out of candies. The la
# st person will receive all of our remaining candies (not necessarily one more th
# an the previous gift). 
# 
#  Return an array (of length num_people and sum candies) that represents the fi
# nal distribution of candies. 
# 
#  
#  Example 1: 
# 
#  
# Input: candies = 7, num_people = 4
# Output: [1,2,3,1]
# Explanation:
# On the first turn, ans[0] += 1, and the array is [1,0,0,0].
# On the second turn, ans[1] += 2, and the array is [1,2,0,0].
# On the third turn, ans[2] += 3, and the array is [1,2,3,0].
# On the fourth turn, ans[3] += 1 (because there is only one candy left), and th
# e final array is [1,2,3,1].
#  
# 
#  Example 2: 
# 
#  
# Input: candies = 10, num_people = 3
# Output: [5,2,3]
# Explanation: 
# On the first turn, ans[0] += 1, and the array is [1,0,0].
# On the second turn, ans[1] += 2, and the array is [1,2,0].
# On the third turn, ans[2] += 3, and the array is [1,2,3].
# On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candies <= 10^9 
#  1 <= num_people <= 1000 
#  
#  Related Topics 数学


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:

        one_round_max = (1 + num_people) * num_people / 2
        round: int = int(candies / one_round_max) + 1
        remain: int = int(candies % one_round_max)

        result = []
        for i in range(1, num_people + 1):
            if(i <= remain):
                result.append((round - 1) * num_people + i)
            elif i == remain + 1:
                result.append((round - 1) * num_people + remain)
            else:
                result.append((round - 2) * num_people + i)
        return result





# leetcode submit region end(Prohibit modification and deletion)

a = Solution().distributeCandies(7,4)
print(a)