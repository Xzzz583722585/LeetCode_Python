class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper = 0
        lower = 0
        for c in word:
            o = ord(c)
            if 65 <= o <= 90:
                upper += 1
                if lower > 0:
                    return False
            else:
                lower += 1
                if upper > 1:
                    return False

        return True


if __name__ == "__main__":
    print(Solution().detectCapitalUse("FFFFFFFFFFFFFFFFFFFFf"))
