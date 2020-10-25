from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:

        result = 0

        def is_special(row, col):
            if mat[row][col] == 1:
                for i in range(len(mat)):
                    if i == row:
                        continue
                    if mat[i][col] == 1:
                        return False
                for j in range(len(mat[0])):
                    if j == col:
                        continue
                    if mat[row][j] == 1:
                        return False
                return True
            return False

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if is_special(i,j):
                    result += 1
        return result

a = Solution().numSpecial([[1,0,0],[0,0,1],[1,0,0]])
print(a)