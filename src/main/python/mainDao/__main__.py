from main.python.structures.body import Body
from main.python.structures.quadtree import Node, NodeStorage

def main():
    bodyList = []
    nodeStorage = NodeStorage()
    rootNode = Node(0.0, 1.0, 0.0, 1.0, 'ROOT')
    nodeStorage.addNodeToStorage(0, rootNode, None)
    testBody = Body(1, 1.2, 0.6, 0.1, 0.01, 0.01)
    testBody2 = Body(2, 1.2, 0.1, 0.1, 0.01, 0.01)
    testBody3 = Body(3, 1.2, 0.1, 0.15, 0.01, 0.01)
    bodyList.extend((testBody, testBody2, testBody3))
    rootNode.addBodyToQuadtree(testBody, nodeStorage, bodyList)
    rootNode.addBodyToQuadtree(testBody2, nodeStorage, bodyList)
    rootNode.addBodyToQuadtree(testBody3, nodeStorage, bodyList)
    nodeStorage.printNodeStorage()


if __name__ == "__main__":
    main()
