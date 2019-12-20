class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars = list(t)
        chars_exited = {}
        for i, c in enumerate(s):
            if c in chars or c in chars_exited:
                if c in chars_exited:
                    chars_exited[c].append(i)
                else:
                    chars.remove(c)
                    chars_exited[c] = [i]

        return


if __name__ == "__main__":
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
