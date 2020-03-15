from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        result: set = set()
        for i in range(0, row):
            row_max = min(matrix[i])
            max_index = matrix[i].index(row_max)
            flag = True
            for j in range(0, row):
                if matrix[j][max_index] > row_max:
                    flag = False
            if flag:
                result.add(row_max)
        return list(result)

a = Solution().luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]])

print(a)