class Solution:
    def peakIndexInMountainArray(self, A):
        max_i, max_h = -1, None
        for i, h in enumerate(A):
            if max_h is None or h > max_h:
                max_h = h
                max_i = i

        return max_i



if __name__ == "__main__":
    nums = [0, 1, 2, 3]
    print(Solution().peakIndexInMountainArray(nums))
