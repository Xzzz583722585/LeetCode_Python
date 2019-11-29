class Solution:
    def intToRoman(self, num: int) -> str:
        num2Char = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        nums = [1000, 500, 100, 50, 10, 5, 1]
        syms = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

        s = ""
        while nums and num > 0:
            if num >= nums[0]:
                n = num // nums[0]
                c = num2Char[nums[0]]
                c_index = syms.index(c)
                num %= nums[0]

                if n == 4 and c_index > 1:
                    last_index = syms.index(s[-1]) if s else -1
                    if last_index == c_index - 1:
                        s = s[:-1] + c + syms[c_index - 2]
                    else:
                        s += (c + syms[c_index - 1])
                else:
                    s += (n * c)
            nums.pop(0)

        return s

if __name__ == "__main__":
    print(Solution().intToRoman(9090))
