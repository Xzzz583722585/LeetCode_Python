class Solution:
    def __init__(self):
        self.cache = {0: 0, 1: 1}

    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1

        if n - 1 in self.cache:
            x = self.cache[n - 1]
        else:
            x = self.fib(n - 1)
            self.cache[n - 1] = x

        if n - 2 in self.cache:
            y = self.cache[n - 2]
        else:
            y = self.fib(n - 2)
            self.cache[n - 2] = y

        return x + y


if __name__ == "__main__":
    for i in range(10):
        print(Solution().fib(i))
