class Solution:
    def findComplement(self, num: int) -> int:
        return int(bin(num)[2:].replace('1', '2').replace('0', '1').replace('2', '0'), 2)


if __name__ == "__main__":
    print(Solution().findComplement(1))
