class Solution:
    def minPathSum(self, grid):
        if not grid:
            return 0

        rows = [0, 1]
        cols = [1, 0]
        paths = {0: {0: 2}}  # {x: {y: 当下方和右方都被遍历过时就可以删除了}}
        visits = []
        for row in grid:
            visits.append([None] * len(row))
        visits[0][0] = grid[0][0]

        while visits[-1][-1] is None:
            min_paths = []

            for row in paths:
                for col in paths[row]:
                    for i in range(2):
                        next_row = row + rows[i]
                        next_col = col + cols[i]
                        if next_row < len(grid) and next_col < len(grid[0]) and visits[next_row][next_col] is None:
                            next_length = visits[row][col] + grid[next_row][next_col]
                            if not min_paths or next_length < min_paths[0][-1]:
                                min_paths = [(row, col, next_row, next_col, next_length)]
                            elif next_length == min_paths[0][-1]:
                                min_paths.append((row, col, next_row, next_col, next_length))

            for pre_row, pre_col, min_row, min_col, min_length in min_paths:
                paths[pre_row][pre_col] -= 1
                if paths[pre_row][pre_col] == 0:
                    del paths[pre_row][pre_col]

                if min_row not in paths:
                    paths[min_row] = {}
                if min_row == len(grid) - 1 or min_col == len(grid[0]) - 1:
                    paths[min_row][min_col] = 1
                else:
                    paths[min_row][min_col] = 2
                visits[min_row][min_col] = min_length

                if not paths[pre_row]:
                    del paths[pre_row]

        return visits[-1][-1]


if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(Solution().minPathSum(grid))
