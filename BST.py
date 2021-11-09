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


def pre_order_traverse(node, arr=[]):
    if node is not None:
        arr.append(node.value)
        pre_order_traverse(node.left, arr)
        pre_order_traverse(node.right, arr)
    return arr


def in_order_traverse(node, arr=[]):
    if node is not None:
        in_order_traverse(node.left, arr)
        arr.append(node.value)
        in_order_traverse(node.right, arr)
    return arr

def post_order_traverse(node, arr=[]):
    if node is not None:
        post_order_traverse(node.left, arr)
        post_order_traverse(node.right, arr)
        arr.append(node.value)
    return arr


def main1():
    arr = [10, 8, 9, 6, 7, 4, 5, 2, 3]
    pot_arr = [6, 3, 2, 4, 5, 8, 7, 9, 10]
    arr = sorted(arr)
    obj = minHeightBst(arr)
    printTree(obj)
    print(findKthLargestValueInBst(obj, 4))
    pre_order_traverse(obj)
def main2():
    arr = [2, 3, 4, 5, 6, 7, 8]
    tree = minHeightBst(arr)
    printTree(tree)
    pot = pre_order_traverse(tree)
    iot = in_order_traverse(tree)
    pst = post_order_traverse(tree)
    print(pot)
    print(iot)
    print(pst)


if __name__ == "__main__":
    main2()