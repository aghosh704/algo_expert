def minHeightBst(array):
    return minHeightBstHelper(array, 0, len(array) - 1)

def minHeightBstHelper(array, from_index, to_index, tree=None):
    if from_index > to_index:
        return tree
    mid = (to_index + from_index) // 2
    if tree is None:
        tree = BST(array[mid])
    else:
        tree.insert(array[mid])
    minHeightBstHelper(array, from_index, mid-1, tree)
    minHeightBstHelper(array, mid+1, to_index, tree)
    return tree

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

def printTree(node, level=0):
    if node is not None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value)
        printTree(node.right, level + 1)
