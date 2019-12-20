class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set([])  # 已经计算过得数字
        while 1:
            num = sum([int(i) ** 2 for i in str(n)])

            if num == 1:
                return True
            elif n in nums:
                return False
            else:
                nums.add(n)
                n = num


if __name__ == "__main__":
    print(Solution().isHappy(19))
