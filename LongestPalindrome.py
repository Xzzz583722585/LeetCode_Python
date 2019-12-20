class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_nums = {}
        for c in s:
            if c in letter_nums:
                letter_nums[c] += 1
            else:
                letter_nums[c] = 1

        odd = 0
        length = 0
        for num in letter_nums.values():
            if num & 1:
                odd = 1
                length += (num - 1)
            else:
                length += num

        return length + odd


if __name__ == "__main__":
    print(Solution().longestPalindrome("abccccddAAA"))
