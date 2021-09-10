class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList: LinkedList):
    # Write your code here.
    node = linkedList
    prev_node = None

    while True:
        if node is None:
            break
        if prev_node is not None:
            if node.value == prev_node.value:
                prev_node.next = node.next
                node = node.next
            else:
                prev_node = node
                node = node.next
        else:
            prev_node = node
            node = node.next

    return linkedList
