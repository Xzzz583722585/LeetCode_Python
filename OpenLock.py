class Solution:
    def openLock(self, deadends, target):
        queue = [[0, 0, 0, 0]]
        while queue:
            nums = queue.pop(0)

            if str(nums) == target:
                return True
            if str(nums) in deadends:
                continue

            for i in range(4):
                if nums[i] < int(target[i]):
                    tmp = nums[:]
                    tmp[i] += 1
                    queue.append(tmp)

        return -1


if __name__ == "__main__":
    print(Solution().openLock(["0201", "0101", "0102", "1212", "2002"], "0202"))
