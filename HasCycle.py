class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False

        low = head
        fast = head

        while low and fast:
            low = low.next

            fast = fast.next
            if fast is not None:
                fast = fast.next

            if low and fast and low == fast:
                return True

        return False


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)

    # n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n2

    print(Solution().hasCycle(n1))
