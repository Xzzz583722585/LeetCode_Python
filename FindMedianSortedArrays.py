class Heap:
    def __init__(self, mode):
        self.nums = []
        self.mode = mode    # 元素间的比较方法
        self.length = 0

    def add(self, num):
        self.length += 1
        self.nums.append(num)
        self.changeB2T(len(self.nums) - 1)

    def remove(self):
        self.length -= 1
        num = self.nums[0]
        self.nums[0] = self.nums[-1]
        self.nums.pop()
        self.changeT2B(0)
        return num

    def changeB2T(self, index):
        if index <= 0:
            return

        father_index = (index - 1) // 2
        if index & 1 == 1 and index + 1 < len(self.nums):
            bro_index = index + 1
        elif index & 1 == 0:
            bro_index = index - 1
        else:
            bro_index = None

        val = self.nums[index]
        father_val = self.nums[father_index]
        bro_val = self.nums[bro_index] if bro_index else None
        if bro_val is None or self.mode(val, bro_val):
            if not self.mode(father_val, val):
                self.nums[father_index], self.nums[index] = val, father_val
                self.changeB2T(father_index)
            else:
                return
        else:
            if not self.mode(father_val, bro_val):
                self.nums[father_index], self.nums[bro_index] = bro_val, father_val
                self.changeB2T(father_index)
            else:
                return

    def changeT2B(self, index):
        if index * 2 + 1 < len(self.nums):
            son_index1 = index * 2 + 1
            son_val1 = self.nums[son_index1]
        else:
            return

        if index * 2 + 2 < len(self.nums):
            son_index2 = index * 2 + 2
            son_val2 = self.nums[son_index2]
            m_index = son_index1 if self.mode(son_val1, son_val2) else son_index2
        else:
            m_index = son_index1

        val = self.nums[index]
        m_val = self.nums[m_index]
        if self.mode(val, m_val):
            return
        else:
            self.nums[index], self.nums[m_index] = m_val, val
            self.changeT2B(m_index)


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2:
            return

        min_heap = Heap(lambda x, y: x < y)
        max_heap = Heap(lambda x, y: x > y)

        for num in nums1 + nums2:
            min_heap.add(num)
            if min_heap.length - 1 > max_heap.length:
                max_heap.add(min_heap.remove())

        if min_heap.length == max_heap.length:
            return (min_heap.nums[0] + max_heap.nums[0]) / 2
        else:
            return min_heap.nums[0]


if __name__ == "__main__":
    nums1 = [1, 3, 5, 7]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
