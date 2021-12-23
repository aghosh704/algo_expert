class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def minimum_value(self):
        curr_node = self
        val = None
        while curr_node is not None:
            val = curr_node.value
            curr_node = curr_node.left
        return val

    def insert(self, value):
        curr_node = self
        while True:
            if value < curr_node.value:
                if curr_node.left is None:
                    curr_node.left = BST(value)
                    break
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = BST(value)
                    break
                else:
                    curr_node = curr_node.right
        return self

    def contains(self, value):
        if self.value == value:
            return True
        else:
            if (self.left is not None) & (self.value > value):
                return self.left.contains(value)
            elif self.right is not None:
                return self.right.contains(value)
            else:
                return False

    def remove(self, value, prev_node=None):
        curr_node = self
        while curr_node is not None:
            if value < curr_node.value:
                prev_node = curr_node
                curr_node = curr_node.left
            elif value > curr_node.value:
                prev_node = curr_node
                curr_node = curr_node.right
            else:
                if (curr_node.left is not None) & (curr_node.right is not None):
                    curr_node.value = curr_node.right.minimum_value()
                    curr_node.right.remove(curr_node.value, curr_node)
                elif prev_node is None:
                    if curr_node.left is not None:
                        curr_node.value = curr_node.left.value
                        curr_node.right = curr_node.left.right
                        curr_node.left = curr_node.left.left
                    elif curr_node.right is not None:
                        curr_node.value = curr_node.right.value
                        curr_node.right = curr_node.right.right
                        curr_node.left = curr_node.right.left
                elif prev_node.left == curr_node:
                    prev_node.left = curr_node.left if curr_node.left is not None else curr_node.right
                elif prev_node.right == curr_node:
                    prev_node.right = curr_node.right if curr_node.right is not None else curr_node.left

                break

        return self


def printTree(node, level=0):
    if node is not None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.value)
        printTree(node.right, level + 1)



