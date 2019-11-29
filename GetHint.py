class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        length = len(secret)
        secret_nums = []
        guess_nums = []
        a = 0
        b = 0
        for i in range(length):
            if secret[i] == guess[i]:
                a += 1
            else:
                if secret[i] in guess_nums:
                    b += 1
                    guess_nums.remove(secret[i])
                else:
                    secret_nums.append(secret[i])

                if guess[i] in secret_nums:
                    b += 1
                    secret_nums.remove(guess[i])
                else:
                    guess_nums.append(guess[i])

        return "%dA%dB" % (a, b)

if __name__ == "__main__":
    print(Solution().getHint("1807", "7810"))
