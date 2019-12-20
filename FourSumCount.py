class Solution:
    def fourSumCount(self, A, B, C, D):
        n = len(A)
        s1 = {}
        s2 = {}

        for i in range(n):
            for j in range(n):
                anb = A[i] + B[j]
                if anb in s1:
                    s1[anb] += 1
                else:
                    s1[anb] = 1

                cnd = C[i] + D[j]
                if cnd in s2:
                    s2[cnd] += 1
                else:
                    s2[cnd] = 1

        res = 0
        for x in s1:
            if -x in s2:
                res += s1[x] * s2[-x]

        return res


if __name__ == "__main__":
    print(Solution().fourSumCount([-1, -1], [-1, 1], [-1, 1], [1, -1]))
