# The set [1,2,3,...,n] contains a total of n! unique permutations. 
# 
#  By listing and labeling all of the permutations in order, we get the followin
# g sequence for n = 3: 
# 
#  
#  "123" 
#  "132" 
#  "213" 
#  "231" 
#  "312" 
#  "321" 
#  
# 
#  Given n and k, return the kth permutation sequence. 
# 
#  Note: 
# 
#  
#  Given n will be between 1 and 9 inclusive. 
#  Given k will be between 1 and n! inclusive. 
#  
# 
#  Example 1: 
# 
#  
# Input: n = 3, k = 3
# Output: "213"
#  
# 
#  Example 2: 
# 
#  
# Input: n = 4, k = 9
# Output: "2314"
#  
#  Related Topics 数学 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def factorial(self, n: int) -> List[int]:
        result = [1]
        fac = 1
        for i in range(1, n+1):
            fac *= i
            result.append(fac)
        return result

    def getPermutation(self, n: int, k: int) -> str:

        fac: List[int] = self.factorial(n)
        contain = list(range(1, n+1))
        result: str = ""
        while len(contain) > 0:

            # 每组数量
            group_number = fac[n - 1]

            # 那一组的第几个，比如 5 % 2 = 1， 是第一个
            offset = k % group_number

            # 在第几组, 如果不是最后一个，需要进一组。 5 / 2 + 1 = 3, 是第三组
            carry = 1 if (offset > 0) else 0
            group_index = int(k / group_number + carry)

            # 找到是未访问的对应个数 [1,2,3,4,5,6,7] 里
            to_add = contain[group_index - 1]
            # 用完了删掉（Java用数组标记）
            del contain[group_index-1]
            result += str(to_add)

            n -= 1
            # 如果index为0 说明是最后一个
            k = group_number if(offset == 0) else offset

        return result









# leetcode submit region end(Prohibit modification and deletion)


a = Solution().getPermutation(3,5)

b = '33dd'
b += str(3)
print(b)