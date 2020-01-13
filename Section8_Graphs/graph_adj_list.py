class Vertex():
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def __str__(self):
        return str(self.id) + " connected to: " + str([x.id for x in self.connectedTo])

    def addNeighbor(self, neighbor, weight=0):
        ''' Adds a vertex neighbor to the current one '''
        self.connectedTo[neighbor] = weight

    def getConnections(self):
        ''' Returns all the neighbor vertices '''
        return self.connectedTo.keys()

    def getId(self):
        ''' Returns the id of the current vertex '''
        return self.id

    def getWeight(self, neighbor):
        ''' Returns the weight between the neighbor and the current vertex '''
        return self.connectedTo[neighbor]


class Graph():
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def __str__(self):
        return "Vertices: " + str(self.getVertices())

    def __len__(self):
        return self.getNumVertices()

    def __contains__(self, vertKey):
        return vertKey in self.vertList[vertKey]

    def __iter__(self):
        return iter(self.vertList.values())

    def addVertex(self, key):
        ''' Adds a vertex to the graph '''
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices += 1
        return newVertex

    def addEdge(self, fromVert, toVert, weight=0):
        ''' Adds a weighted edge to the first vertex '''
        if fromVert not in self.vertList:
            temp = self.addVertex(fromVert)
        if toVert not in self.vertList:
            temp = self.addVertex(toVert)

        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)

    def getVertex(self, vertKey):
        ''' Returns the Vertex object from the vertList '''
        if vertKey in self.vertList:
            return self.vertList[vertKey]
        else:
            return None

    def getVertices(self):
        ''' Returns all vertices from the graph '''
        return self.vertList.keys()

    def getNumVertices(self):
        ''' Returns the number of vertices in the graph '''
        return self.numVertices


class VertexBFS(Vertex):
    ''' Vertex implementation for Breadth First Search Algorithm '''

    def __init__(self, key):
        super().__init__(key)
        self.distance = 0
        self.predecessor = None
        self.color = "white"

    def getDistance(self):
        return self.distance

    def getPredecessor(self):
        return self.predecessor

    def getColor(self):
        return self.color

    def setDistance(self, d):
        self.distance = d

    def setPredecessor(self, p):
        self.predecessor = p

    def setColor(self, c):
        self.color = c


class GraphBFS(Graph):
    ''' Graph Implementation for Breadth First Search Algorithm '''

    def __init__(self):
        super().__init__()

    def addVertex(self, key):
        ''' Adds a vertex to the graph '''
        newVertex = VertexBFS(key)
        self.vertList[key] = newVertex
        self.numVertices += 1
        return newVertex

    def addEdge(self, fromVert, toVert, weight=0):
        ''' Adds a weighted edge to the first vertex '''
        if fromVert not in self.vertList:
            temp = self.addVertex(fromVert)
        if toVert not in self.vertList:
            temp = self.addVertex(toVert)

        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)

    def getVertex(self, vertKey):
        return super().getVertex(vertKey)

    def getVertices(self):
        return super().getVertices()


if __name__ == "__main__":
    graph = Graph()

    for num in range(6):
        graph.addVertex(num)

    # Vertex V0
    graph.addEdge(0, 1, 5)
    graph.addEdge(0, 5, 2)

    # Vertex V1
    graph.addEdge(1, 2, 4)

    # Vertex V2
    graph.addEdge(2, 3, 9)

    # Vertex V3
    graph.addEdge(3, 4, 7)
    graph.addEdge(3, 5, 3)

    # Vertex V4
    graph.addEdge(4, 0, 1)

    # Vertex V5
    graph.addEdge(5, 2, 1)
    graph.addEdge(5, 4, 8)

    for vertex in graph:
        print(vertex)
