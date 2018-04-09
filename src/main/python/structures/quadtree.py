import math
from enum import Enum
from main.python.structures.body import Body

class NodeStorage:

class NodeDirection(Enum):
    SW = 'SW'
    NW = 'NW'
    NE = 'NE'
    SE = 'SE'

class Node:

    def __init__(self, x0, xh, y0, yh, direction):
        self.id = nodeId
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

    def addBodyToNode(self, body):
        

    def divideNode(self):
        SWNode = Node(self.x0, self.x1/2.0, self.y0, self.y1/2.0, NodeDirection.SW)
        NWNode = Node(self.x0, self.x1/2.0, self.y1/2.0, self.y1, NodeDirection.NW)
        NENode = Node(self.x1/2.0, self.x1, self.y1/2.0, self.y1, NodeDirection.NE)
        SENode = Node(self.x1/2.0, self.x1, self.y1, self.y1/2.0, NodeDirection.SE)



    def addBodyToQuadtree(self, body):
        for i in range(len(nodes)):
            if self.isBodyInNode(body) == True:
                if self.isEmpty == True:
                    if self.hasChildren == False:
                        self.addBodyToNode(body)
                    elif self.hasChildren == True:
                        self.divideNode()
                elif self.isEmpty == False:


    def generateNodeID(self, parentNodeID):
        if self.direction == 'Sw':
            return parentNodeID + '1'
        elif self.direction == 'NW':
            return parentNodeID + '2'
        elif self.direction == 'NE':
            return parentNodeID + '3'
        elif self.direction == 'SE':
            return parentNodeID + '4'


    def getInfo(self):
        return self.id, self.x0, self.x1, self.y0, self.y1

    def getLevel(self):
        return int(math.log(1/(self.x1 - self.x0), 2))

global nodeId
global nodes
nodeId = 1
nodes = []
nodes.append(Node(0.0, 0.5, 0.0, 0.5))
nodeId += 1
nodes.append(Node(0.0, 0.5, 0.5, 0.5))
nodeId += 1
nodes.append(Node(0.5, 0.5, 0.5, 0.5))
nodeId += 1
nodes.append(Node(0.5, 0.5, 0.0, 0.5))
testBody = Body(1, 1.2, 0.51, 0.51, 0.1, 0.1)
addBodyToQuadtree(testBody)
for i in range(len(nodes)):
    print(nodes[i].isEmpty)