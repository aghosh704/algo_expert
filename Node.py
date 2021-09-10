class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearchHelper(self, array, node=None):
        if not node:
            array.append(self.name)
            node = self
        for tmp in node.children:
            array.append(tmp.name)
            self.depthFirstSearchHelper(array, tmp)

    def depthFirstSearch(self, array):
        self.depthFirstSearchHelper(array)
graph = Node("A")

graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")

result = []
print(graph)
#graph.depthFirstSearchHelper(graph, result)
graph.depthFirstSearch(result)
print(result)
