import sys

# 计算方程 y = ax^2 + x + b 与 x = C 、x = D 围成的面积
class Solution:
    def solve(self, A:int, B:int, C:int, D:int):
        # 方程的积分原函数
        def original(x):
            s = (A * (x ** 3)) / 3 + (x ** 2) / 2 + B * x
            return s

        # 分为三种情况，CD对于x轴
        if C <= 0 and D <= 0:
            return original(C) - original(D)
        elif C >= 0 and D >= 0:
            return original(D) - original(C)
        elif C < 0 and D > 0:
            return (original(C) - original(0)) + (original(D) - original(0))

    def calculate(self):
        count = input()
        for i in range(int(count)):
            sd = input()
            A, B, C, D = sd.split(' ')
            area = self.solve(int(A), int(B), int(C), int(D))
            print(area)

a = Solution().calculate()