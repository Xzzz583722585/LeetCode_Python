class Solution:
    def kthGrammar(self, n, k):
        if n < 1:
            return ""

        now = "0"
        next = ""
        for i in range(n - 1):
            for c in now:
                if c == '0':
                    next += "01"
                elif c == '1':
                    next += "10"

            now = next
            next = ""

        return now[k - 1]

if __name__ == "__main__":
    for i in range(5):
        print(Solution().kthGrammar(i, 2))
