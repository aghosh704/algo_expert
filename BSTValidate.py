# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validate_helper(bst, min_val, max_val):
    if bst is None:
        return True
    if (bst.value >= max_val) | (bst.value < min_val):
        return False
    return validate_helper(bst.left, min_val, bst.value) & (validate_helper(bst.right, bst.value, max_val))


def validateBst(tree):
    return validate_helper(tree, float('-inf'), float('inf'))

def printTree(node, level=0):
    if node is not None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value)
        printTree(node.right, level + 1)
