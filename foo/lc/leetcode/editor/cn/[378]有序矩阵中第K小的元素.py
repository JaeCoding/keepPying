# Given a n x n matrix where each of the rows and columns are sorted in ascendin
# g order, find the kth smallest element in the matrix. 
# 
#  
# Note that it is the kth smallest element in the sorted order, not the kth dist
# inct element.
#  
# 
#  Example:
#  
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
# 
# r7eturn 13.
#  
#  
# 
#  Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2. Related Topics 堆 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        reduce = 1
        left = True
        l = []
        while True:

            if k - reduce <= 0:
                # k will in the this diagonal
                if left:
                    for i in range(reduce):
                        l.append(matrix[i][reduce - 1 - i])
                else:
                    for i in range(reduce):
                        l.append(matrix[n - reduce + i][n - 1 - i])
                l.sort()
                return l[k - 1]

            k -= reduce
            if reduce < n:
                reduce += 1
            else:
                reduce -= 1
                left = False



a = Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)
a = Solution().kthSmallest([[1,3,5],[6,7,12],[11,14,14]],3)
print(a)
# leetcode submit region end(Prohibit modification and deletion)
