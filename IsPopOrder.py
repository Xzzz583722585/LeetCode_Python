# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV is None:
            return True

        stack = []
        length = len(pushV)
        i, j = 0, 0
        while i < length:
            stack.append(pushV[i])
            if pushV[i] == popV[j]:
                stack.pop()
                j += 1
            i += 1

        while stack and stack[-1] == popV[j] and j < length:
            stack.pop()
            j += 1

        return len(stack) == 0


if __name__ == "__main__":
    pushV = []
    popV = []

    print(Solution().IsPopOrder(None, None))
