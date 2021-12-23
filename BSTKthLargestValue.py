
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def findKthLargestValueInBst(tree, k):
    tree_vals = findKthLargestValueInBstHelper(tree, k)

    return tree_vals[len(tree_vals) - k]


def findKthLargestValueInBstHelper(tree, k, vals=[]):
    if tree is not None:
        findKthLargestValueInBstHelper(tree.left, k, vals)
        vals.append(tree.value)
    findKthLargestValueInBstHelper(tree.right, k, vals)
    return vals

def printTree(node, level=0):
    if node is not None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value)
        printTree(node.right, level + 1)
