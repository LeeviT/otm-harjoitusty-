import math
from enum import Enum
from main.python.structures.body import Body


class NodeStorage():

    def __init__(self):
        self.nodeList = []
        self.storageSize = 0
        self.bodyID = None

    def addNodeToStorage(self, nodeID, node, bodyID):
        if self.doContainID(nodeID) == False:
            self.nodeList.append([nodeID, node, bodyID])
            self.storageSize += 1

    def printNodeStorage(self):
        for i in range(self.storageSize):
            print(self.nodeList[i][0], self.nodeList[i][1].getInfo(), self.nodeList[i][2])

    def getSize(self):
        return self.storageSize

    def getNodeUsingID(self, nodeID):
        for i in range(self.storageSize):
            if (self.nodeList[i][0] == nodeID):
                return self.nodeList[i][1]

    def getStorageElementUsingID(self, nodeID):
        for i in range(self.storageSize):
            if (self.nodeList[i][0] == nodeID):
                return self.nodeList[i]

    def doContainID(self, nodeID):
        for i in range(self.storageSize):
            if (self.nodeList[i][0] == nodeID):
                return True
        return False

class NodeDirection(Enum):
    SW = 'SW'
    NW = 'NW'
    NE = 'NE'
    SE = 'SE'
    ROOT = 'ROOT'


class Node:

    id = 0

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

    def addBodyToNode(self, body, nodeStorage):
        self.isEmpty = False
        nodeStorage.getStorageElementUsingID(self.id)[2] = body.id

    def divideNode(self, nodeStorage):
        self.hasChildren = False
        SWNode = Node(self.x0, self.x1 / 2.0, self.y0, self.y1 / 2.0, NodeDirection.SW.name)
        NWNode = Node(self.x0, self.x1 / 2.0, self.y1 / 2.0, self.y1, NodeDirection.NW.name)
        NENode = Node(self.x1 / 2.0, self.x1, self.y1 / 2.0, self.y1, NodeDirection.NE.name)
        SENode = Node(self.x1 / 2.0, self.x1, self.y1, self.y1 / 2.0, NodeDirection.SE.name)
        SWID = SWNode.generateNodeID(self.id)
        NWID = NWNode.generateNodeID(self.id)
        NEID = NENode.generateNodeID(self.id)
        SEID = SENode.generateNodeID(self.id)
        SWNode.id = SWID
        NWNode.id = NWID
        NENode.id = NEID
        SENode.id = SEID
        commID = nodeStorage.getStorageElementUsingID(self.id)[2]
        commBody = bodyList[commID - 1]
        print(commBody.getVisualize())
        if SWNode.isBodyInNode(commBody) == True:
            SWNode.isEmpty = False
            nodeStorage.addNodeToStorage(SWID, SWNode, commBody.id)
        else:
            nodeStorage.addNodeToStorage(SWID, SWNode, None)
        if NWNode.isBodyInNode(commBody) == True:
            NWNode.isEmpty = False
            nodeStorage.addNodeToStorage(NWID, NWNode, commBody.id)
        else:
            nodeStorage.addNodeToStorage(NWID, NWNode, None)
        if NENode.isBodyInNode(commBody) == True:
            NENode.isEmpty = False
            nodeStorage.addNodeToStorage(NEID, NENode, commBody.id)
        else:
            nodeStorage.addNodeToStorage(NEID, NENode, None)
        if SENode.isBodyInNode(commBody) == True:
            SENode.isEmpty = False
            nodeStorage.addNodeToStorage(SEID, SENode, commBody.id)
        else:
            nodeStorage.addNodeToStorage(SEID, SENode, None)


    def addBodyToQuadtree(self, body, nodeStorage):
        if self.isBodyInNode(body) == True:
            if self.isEmpty == False:
                if self.hasChildren == False:
                    self.divideNode(nodeStorage)
                    for i in range(1, 5):
                        if self.id == 0:
                            tempNode = nodeStorage.getNodeUsingID(i)
                        else:
                            tempNode = nodeStorage.getNodeUsingID(int(str(self.id) + str(i)))
                        tempNode.addBodyToQuadtree(body, nodeStorage)
                elif self.hasChildren == True:
                    for i in range(1, 4):
                        if self.id == 0:
                            tempNode = nodeStorage.getNodeUsingID(i)
                        else:
                            tempNode = nodeStorage.getNodeUsingID(int(str(self.id) + str(i)))
                        tempNode.addBodyToQuadtree(body, nodeStorage)
            elif self.isEmpty == True:
                self.addBodyToNode(body, nodeStorage)

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
        return self.id, self.x0, self.x1, self.y0, self.y1

    def getLevel(self):
        return int(math.log(1 / (self.x1 - self.x0), 2))


global bodyList
bodyList = []
nodeStorage = NodeStorage()
rootNode = Node(0.0, 1.0, 0.0, 1.0, 'ROOT')
nodeStorage.addNodeToStorage(0, rootNode, None)
testBody = Body(1, 1.2, 0.6, 0.1, 0.01, 0.01)
testBody2 = Body(2, 1.2, 0.1, 0.1, 0.01, 0.01)
testBody3 = Body(3, 1.2, 0.1, 0.15, 0.01, 0.01)
bodyList.extend((testBody, testBody2, testBody3))
#rootNode.divideNode(nodeStorage)
rootNode.addBodyToQuadtree(testBody, nodeStorage)
rootNode.isEmpty = False
rootNode.addBodyToQuadtree(testBody2, nodeStorage)
rootNode.addBodyToQuadtree(testBody3, nodeStorage)

nodeStorage.printNodeStorage()
#print(nodeStorage.getNodeUsingID(3).getInfo())

