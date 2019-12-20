class Solution:
    def pivotIndex(self, nums) -> int:
        if not nums:
            return -1

        i, j = -1, len(nums)
        s1, s2 = 0, 0  # 左右区间之和
        while j - i >= 2:
            if s1 == s2:
                if i + 2 == j:
                    return i + 1
                else:
                    if nums[i + 1] != 0 or nums[j - 1] == 0:
                        j -= 1
                        s2 += nums[j]
                    else:
                        i += 1
                        s1 += nums[i]
            else:
                if s1 < s2:
                    if nums[i + 1] > 0:
                        i += 1
                        s1 += nums[i]
                    else:
                        j -= 1
                        s2 += nums[j]
                else:
                    if nums[j - 1] > 0:
                        j -= 1
                        s2 += nums[j]
                    else:
                        i += 1
                        s1 += nums[i]

        return -1


if __name__ == "__main__":
    print(Solution().pivotIndex([-1,-1,0,1,0,-1]))
