# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.nums = []
        self.min_nums = []

    def push(self, node):
        if not self.min_nums or node < self.min_nums[-1]:
            self.min_nums.append(node)
        else:
            self.min_nums.append(self.min_nums[-1])

        self.nums.append(node)

    def pop(self):
        self.min_nums.pop()
        return self.nums.pop()

    def top(self):
        return self.nums[-1]

    def min(self):
        return self.min_nums[-1]


if __name__ == "__main__":
    stack = Solution()

    stack.push(2)
    stack.push(3)
    stack.push(1)
    stack.push(4)

    print(stack.top())
    print(stack.min())

    stack.pop()
    stack.pop()

    print(stack.top())
    print(stack.min())
