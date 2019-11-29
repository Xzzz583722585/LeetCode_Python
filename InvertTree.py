class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root):
        if root is None:
            return

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n7 = TreeNode(7)
    n9 = TreeNode(9)

    n4.left = n2
    n4.right = n7

    n2.left = n1
    n2.right = n3

    n7.right = n9

    root = Solution().invertTree(n4)
    print()
