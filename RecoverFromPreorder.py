class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, s) -> TreeNode:
        if not s:
            return

        num = 0
        dep = 0
        pre = 0     # 0代表-,1代表数字
        nodes = []
        root = None
        for c in (s + '#'):
            if c == '-' or c == '#':
                if pre == 1:
                    childs = []
                    while nodes and dep < nodes[-1][0]:
                        childs.append(nodes.pop()[1])
                    for i in range(2):
                        if childs:
                            if i & 1 == 0:
                                nodes[-1][1].left = childs.pop()
                            else:
                                nodes[-1][1].right = childs.pop()

                    if not nodes or dep >= nodes[-1][0]:
                        node = TreeNode(num)
                        if root is None:
                            root = node
                        nodes.append((dep, node))
                    dep = 0

                num = 0
                dep += 1
                pre = 0
            else:
                num = num * 10 + int(c)
                pre = 1

        while nodes:
            childs = []
            child_num = 1
            if len(nodes) >= 2 and nodes[-1][0] == nodes[-2][0]:
                child_num = 2
            for i in range(child_num):
                childs.append(nodes.pop()[1])
            if nodes:
                for i in range(2):
                    if childs:
                        if i & 1 == 0:
                            nodes[-1][1].left = childs.pop()
                        else:
                            nodes[-1][1].right = childs.pop()

        return root


if __name__ == "__main__":
    root = Solution().recoverFromPreorder("")
    print()