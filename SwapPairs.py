class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if head is None:
            return

        pre = ListNode(0)
        tmp = pre
        pre.next = head
        now1 = head
        now2 = head.next

        while now1 and now2:
            pre.next = now2
            now1.next = now2.next
            now2.next = now1

            pre = now1
            now1 = pre.next
            now2 = now1.next if now1 else None

        return tmp.next

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    # n3.next = n4

    root = Solution().swapPairs(None)
    print()
