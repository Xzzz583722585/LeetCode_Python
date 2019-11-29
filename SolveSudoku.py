class Solution:
    def solveSudoku(self, board):
        row_uses = {}   # 每行0-9使用情况
        for i in range(9):
            row_uses[i] = [0] * 10

        col_uses = {}  # 每列0-9使用情况
        for j in range(9):
            col_uses[j] = [0] * 10

        grid_uses = {}   # 每个3×3小格子0-9使用情况
        for i in range(3):
            grid_uses[i] = {}
            for j in range(3):
                grid_uses[i][j] = [0] * 10

        # init
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    row_uses[i][num] = 1
                    col_uses[j][num] = 1
                    grid_uses[i // 3][j // 3][num] = 1

        self.solve(board, 0, 0, row_uses, col_uses, grid_uses)

    def solve(self, board, i, j, row_uses, col_uses, grid_uses):
        if board[i][j] == '.':
            for num in range(1, 10):
                if row_uses[i][num] == 0 and col_uses[j][num] == 0 and grid_uses[i // 3][j // 3][num] == 0:
                    row_uses[i][num] = 1
                    col_uses[j][num] = 1
                    grid_uses[i // 3][j // 3][num] = 1
                    board[i][j] = str(num)

                    if (i == 8 and j == 8) or self.solve(board, i + 1 if j == 8 else i, (j + 1) % 9, row_uses, col_uses, grid_uses):
                        return True

                    row_uses[i][num] = 0
                    col_uses[j][num] = 0
                    grid_uses[i // 3][j // 3][num] = 0
                    board[i][j] = '.'
        elif i == 8 and j == 8:
            return True
        else:
            return self.solve(board, i + 1 if j == 8 else i, (j + 1) % 9, row_uses, col_uses, grid_uses)


if __name__ == "__main__":
    board = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],

        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],

        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9'],
    ]
    Solution().solveSudoku(board)
    print(board)
