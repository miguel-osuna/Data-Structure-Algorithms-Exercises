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
        self.vertexList = {}
        self.numVertices = 0

    def __contains__(self, n):
        return n in self.vertexList[n]

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertextList[key] = newVertex
        self.numVertices += 1
        return newVertex

    def addEdge(self, fromVert, toVert):
        pass

    def addWeightedEdge(self, fromVert, toVert, weight):
        pass

    def getVertex(self, vertKey):
        pass

    def getVertices(self):
        pass

    def getNumVertices(self):
        return self.numVertices
