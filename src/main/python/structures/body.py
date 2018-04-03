class Body:

    def __init__(self, id, mass, xPosition, yPosition, xVelocity, yVelocity):
        self.id = id
        self.m = mass
        self.x = xPosition
        self.y = yPosition
        self.vx = xVelocity
        self.vy = yVelocity

    def getId(self):
        return self.id

    def getMass(self):
        return self.m

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getVX(self):
        return self.vx

    def getVY(self):
        return self.vy

    def getVisualize(self):
        return self.m, self.x, self.y