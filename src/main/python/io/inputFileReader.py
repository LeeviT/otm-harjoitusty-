from src.main.python.structures.body import Body

class InputFileReader:

    def readNumberOfBodies(fileName):
        global nob
        file = open(fileName, "r")
        firstLine = file.readline()
        nob = int(firstLine[4:100])
        return nob

    def readDataToBodyList(fileName):
        inputData = [None]*nob
        bodyList = [None]*nob
        i = 0
        with open(fileName, "r") as file:
            lines = file.readlines()[1:]
            for line in lines:
                inputData[i] = list(map(float, line.split()))
                id, mass, x = i, inputData[i][0], inputData[i][1]
                y, vx, vy = inputData[i][2], inputData[i][3], inputData[i][4]
                bodyList[i] = Body(id, mass, x, y, vx, vy)
                testBody = Body(id, mass, x, y, vx, vy)
                print(testBody.getVisualize())
                i += 1
        return bodyList

    readNumberOfBodies("testi.dat")
    readDataToBodyList("testi.dat")
