class Solution:
    def balancedStringSplit(self, s) -> int:
        l, r = 0, 0
        res = 0
        for c in s:
            if c == 'L':
                l += 1
            else:
                r += 1

            if l == r:
                res += 1

        return res


if __name__ == "__main__":
    print(Solution().balancedStringSplit("RLLLLRRRLR"))
