class Solution:
    def numSquares(self, n: int) -> int:
        squs = []
        i = 1
        while i ** 2 <= n:
            if i ** 2 == n:
                return 1
            squs.insert(0, i ** 2)
            i += 1

        queue = [(n, 0)]
        while queue:
            s, length = queue.pop(0)
            for squ in squs:
                if s - squ == 0:
                    return length + 1
                elif s - squ > 0:
                    queue.append((s - squ, length + 1))


if __name__ == "__main__":
    print(Solution().numSquares(12))
