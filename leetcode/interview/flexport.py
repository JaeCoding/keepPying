# Hi welcome to Flexport!
#                   B     R
#                B  R  R  R
#       R     B  R  R  B  R  B
#       -  -  -  -  -  -  -  -  -
# ...  -3 -2 -1  0  1  2  3  4  5  ...
# Two players: R & B
# boolean put(string color, int pos)
# put("R", 3) -> false
# put("R", 3) -> false
# put("R", 3) -> true


class Solution:
    def __init__(self):
        self.map = {}

    def put(self, color, pos):
        if pos not in self.map:
            self.map[pos] = []

        # put the input
        self.map[pos].append(color)

        if len(self.map[pos]) >= 3 and self.map[pos][-1] == self.map[pos][-2] == self.map[pos][-3]:
            return True

        # check if has three same color
        count_left = 1
        i = pos - 1
        high = len(self.map[pos])
        while i in self.map and len(self.map[i]) >= high - 1 and self.map[i][high - 1] == color:
            count_left += 1
            if count_left == 3:
                return True
            i -= 1

        # check the right
        count_right = 1
        i = pos + 1
        while i in self.map and len(self.map[i]) >= high - 1 and self.map[i][high - 1] == color:
            count_right += 1
            if count_right == 3:
                return True
            i += 1
        if count_left + count_right - 1 >= 3:
            return True

        return False

r = Solution()
# print(r.put("R", 3))
# print(r.put("R", 3))
print(r.put("R", 3))
print(r.put("R", 5))
print(r.put("R", 4))






