class Solution:
    def gameOfLife(self, board):
        xs = [-1, 0, 1, 1, 1, 0, -1, -1]
        ys = [-1, -1, -1, 0, 1, 1, 1, 0]

        factors = []    # 记录每个细胞周围的活细胞/死细胞数
        for i in range(len(board)):
            factors.append([0] * len(board[i]))
            for j in range(len(board[i])):
                life_factor = 0
                for index in range(8):
                    x, y = j + xs[index], i + ys[index]
                    if 1 <= x < len(factors[i]) and 0 <= y < len(factors):
                        if board[y][x]:
                            life_factor += 1
                factors[i][j] = life_factor

        for i in range(len(board)):
            for j in range(len(board[i])):
                life_factor = factors[i][j]
                if board[i][j] == 1 and life_factor < 2 or life_factor > 3:
                    board[i][j] = 0
                    self.changeFactors(factors, i, j, -1)
                elif board[i][j] == 0 and life_factor == 3:
                    board[i][j] = 1
                    self.changeFactors(factors, i, j, 1)

    def changeFactors(self, factors, i, j, target):
        xs = [-1, 0, 1, 1, 1, 0, -1, -1]
        ys = [-1, -1, -1, 0, 1, 1, 1, 0]
        for index in range(8):
            x, y = j + xs[index], i + ys[index]
            if 1 <= x < len(factors[i]) and 0 <= y < len(factors):
                factors[y][x] += target


if __name__ == "__main__":
    board = [[0, 1, 0],
             [0, 0, 1],
             [1, 1, 1],
             [0, 0, 0]]
    print(Solution().gameOfLife(board))
