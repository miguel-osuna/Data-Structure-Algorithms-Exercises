class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def __str__(self):
        return str(self.id) + " connected to: " + str([x.id for x in self.connectedTo])

    def addNeighbor(self, neighbor, weight=0):
        self.connectedTo[neighbor] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neighbor):
        return self.connectedTo[neighbor]


class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def __contains__(self, vertKey):
        return vertKey in self.vertList[vertKey]

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertextList[key] = newVertex
        self.numVertices += 1
        return newVertex

    def addEdge(self, fromVert, toVert, weight=0):
        if fromVert not in self.vertList:
            temp = self.addVertex(fromVert)
        if toVert not in self.vertList:
            temp = self.addVertex(toVert)

        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)

    def getVertex(self, vertKey):
        if vertKey in self.vertList:
            return self.vertextList[vertKey]
        else:
            return None

    def getVertices(self):
        return self.vertList.keys()

    def getNumVertices(self):
        return self.numVertices
