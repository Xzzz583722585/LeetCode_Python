class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.preOrder(root, 0)
        return root

    def preOrder(self, root, big_val):
        if not root:
            return 0

        root.val += big_val
        root.val += self.preOrder(root.right, big_val)
        self.preOrder(root.left, root.val + big_val)
        return root.val + big_val

        # now = root
        # stack = []
        # while now or stack:
        #     if now:
        #         stack.append(now)
        #         now = now.left
        #     else:
        #         father = stack.pop()
        #         if father:
        #             now = father.right


if __name__ == "__main__":
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n7 = TreeNode(7)
    n13 = TreeNode(13)

    n5.left = n2
    n5.right = n13

    n2.right = n3

    n13.left = n7

    root = Solution().convertBST(n5)
