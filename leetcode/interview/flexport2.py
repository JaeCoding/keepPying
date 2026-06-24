class InfiniteBoard:
    def __init__(self):
        self.board = {}  # 用字典存储每个位置的棋子数量

    def put(self, color, index):
        if index not in self.board:
            self.board[index] = {'R': 0, 'B': 0}
        self.board[index][color] += 1  # 在指定位置增加一个棋子

        # 检查纵向是否有3个相同的棋子
        if self.board[index][color] >= 3:
            return True

        # 检查横向是否有3个相同的棋子
        count = 1  # 当前棋子本身算一个
        for direction in [-1, 1]:  # 检查左右两边
            i = 1
            while (index + i * direction) in self.board and self.board[index + i * direction][color] > 0:
                count += 1
                if count >= 3:
                    return True
                i += 1

        return False

# 使用提供的例子测试代码
board = InfiniteBoard()
print(board.put("R", 3))  # 输出应为False
print(board.put("R", 5))  # 输出应为True
print(board.put("R", 4))  # 输出应为False
