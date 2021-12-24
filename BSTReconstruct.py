class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):

    if len(preOrderTraversalValues) == 0:
        return None

    root_idx = 0
    right_idx = len(preOrderTraversalValues)
    for idx, val in enumerate(preOrderTraversalValues):
        if val > preOrderTraversalValues[root_idx]:
            right_idx = idx
            break

    return BST(preOrderTraversalValues[root_idx],
               reconstructBst(preOrderTraversalValues[1:right_idx]),
               reconstructBst(preOrderTraversalValues[right_idx:])
               )

def printTree(node, level=0):
    if node is not None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value)
        printTree(node.right, level + 1)


if __name__ == "__main__":
    arr = [10, 4, 2, 1, 5, 17, 19, 18]
    tree = reconstructBst(arr)
    printTree(tree)