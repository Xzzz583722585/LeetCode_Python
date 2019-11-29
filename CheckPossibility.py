class Solution:
    def checkPossibility(self, nums) -> bool:
        reverse = 0
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                if i + 1 == j and nums[i] == nums[j]:
                    break
                elif nums[i] > nums[j]:
                    reverse += 1
                    break

        return reverse <= 1


if __name__ == "__main__":
    print(Solution().checkPossibility([3,3,2,2]))
