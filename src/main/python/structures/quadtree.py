import math
from enum import Enum
from main.python.structures.body import Body


class NodeStorage():

    def __init__(self):
        self.nodeList = []
        self.storageSize = 0

    def addNodeToStorage(self, nodeID, node):
        self.nodeList.append([nodeID, node])
        self.storageSize += 1

    def printNodeStorage(self):
        for i in range(self.storageSize):
            print(self.nodeList[i][0], self.nodeList[i][1].getInfo())

    def getSize(self):
        return self.storageSize

    def getNodeUsingID(self, nodeID):
        for i in range(self.storageSize):
            if (self.nodeList[i][0] == nodeID)
                return self.nodeList[i][1]


class NodeDirection(Enum):
    SW = 'SW'
    NW = 'NW'
    NE = 'NE'
    SE = 'SE'
    ROOT = 'ROOT'


class Node:

    def __init__(self, x0, xh, y0, yh, direction):
        self.x0 = x0
        self.x1 = xh
        self.y0 = y0
        self.y1 = yh
        self.direction = direction
        self.isEmpty = True
        self.hasChildren = False

    def isBodyInNode(self, body):
        if (body.getX() > self.x0) & (body.getX() < self.x1) & (body.getY() > self.y0) & (body.getY() < self.y1):
            return True
        else:
            return False

    # def addBodyToNode(self, body, nodeStorage):

    def divideNode(self, nodeStorage):
        SWNode = Node(self.x0, self.x1 / 2.0, self.y0, self.y1 / 2.0, NodeDirection.SW.name)
        NWNode = Node(self.x0, self.x1 / 2.0, self.y1 / 2.0, self.y1, NodeDirection.NW.name)
        NENode = Node(self.x1 / 2.0, self.x1, self.y1 / 2.0, self.y1, NodeDirection.NE.name)
        SENode = Node(self.x1 / 2.0, self.x1, self.y1, self.y1 / 2.0, NodeDirection.SE.name)
        nodeStorage.addNodeToStorage(SWNode.generateNodeID(0), SWNode)
        nodeStorage.addNodeToStorage(NWNode.generateNodeID(0), NWNode)
        nodeStorage.addNodeToStorage(NENode.generateNodeID(0), NENode)
        nodeStorage.addNodeToStorage(SENode.generateNodeID(0), SENode)

    def addBodyToQuadtree(self, body, nodeStorage):
        if self.isBodyInNode(body) == True:
            if self.isEmpty == True:
                if self.hasChildren == False:
                    self.divideNode(nodeStorage)
                    #self.addBodyToNode(body, nodeStorage)
                elif self.hasChildren == True:
                    self.divideNode(nodeStorage)
            # elif self.isEmpty == False:

    def generateNodeID(self, parentNodeID):
        if self.direction == 'ROOT':
            return parentNodeID
        elif self.direction == 'SW':
            return int(str(parentNodeID) + '1')
        elif self.direction == 'NW':
            return int(str(parentNodeID) + '2')
        elif self.direction == 'NE':
            return int(str(parentNodeID) + '3')
        elif self.direction == 'SE':
            return int(str(parentNodeID) + '4')

    def getInfo(self):
        return self.x0, self.x1, self.y0, self.y1

    def getLevel(self):
        return int(math.log(1 / (self.x1 - self.x0), 2))


nodeStorage = NodeStorage()
rootNode = Node(0.0, 1.0, 0.0, 1.0, 'ROOT')
testBody = Body(1, 1.2, 0.1, 0.1, 0.01, 0.01)
#rootNode.divideNode(nodeStorage)
#testBody2 = Body(1, 1.2, 0.15, 0.15, 0.01, 0.01)
#rootNode.divideNode(nodeStorage)
rootNode.addBodyToQuadtree(testBody, nodeStorage)
nodeStorage.printNodeStorage()

