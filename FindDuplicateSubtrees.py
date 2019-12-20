class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = {}

    def findDuplicateSubtrees(self, root):
        self.preOrder(root)
        return [v[0] for k, v in self.res.items() if len(v) > 1]

    def preOrder(self, root):
        if root is None:
            return '#'

        left_order = self.preOrder(root.left)
        right_order = self.preOrder(root.right)

        order = str(root.val) + left_order + right_order
        if order in self.res:
            self.res[order].append(root)
        else:
            self.res[order] = [root]

        return order


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2_1 = TreeNode(2)
    n3 = TreeNode(3)
    n4_1 = TreeNode(4)
    n2_2 = TreeNode(2)
    n4_2 = TreeNode(4)
    n4_3 = TreeNode(4)

    n1.left = n2_1
    n1.right = n3

    n2_1.left = n4_1

    n3.left = n2_2
    n3.right = n4_2

    n2_2.left = n4_3

    res = Solution().findDuplicateSubtrees(n1)
    print()
