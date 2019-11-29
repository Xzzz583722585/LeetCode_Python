class Solution:
    def getRow(self, row_index):
        if row_index == 0:
            return [1]

        pre = self.getRow(row_index - 1)
        now = [0] * (row_index + 1)
        for i in range(len(now)):
            x = pre[i - 1] if i > 0 else 0
            y = pre[i] if i < row_index else 0
            now[i] = x + y

        return now


if __name__ == "__main__":
    print(Solution().getRow(4))
