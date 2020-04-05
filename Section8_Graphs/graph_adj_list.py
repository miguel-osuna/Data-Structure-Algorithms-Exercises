import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
sys.path.insert(0, "Section4_Basic_Data_Structures/queue")
from queue1 import Queue1


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def __str__(self):
        return str(self.id) + " connected to: " + str([x.id for x in self.connectedTo])

    def addNeighbor(self, neighbor, weight=0):
        """ Adds a vertex neighbor to the current one """
        self.connectedTo[neighbor] = weight

    def getConnections(self):
        """ Returns all the neighbor vertices """
        return self.connectedTo.keys()

    def getId(self):
        """ Returns the id of the current vertex """
        return self.id

    def getWeight(self, neighbor):
        """ Returns the weight between the neighbor and the current vertex """
        return self.connectedTo[neighbor]


class Graph:
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
        """ Adds a vertex to the graph """
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices += 1
        return newVertex

    def addEdge(self, fromVert, toVert, weight=0):
        """ Adds a weighted edge to the first vertex """
        if fromVert not in self.vertList:
            temp = self.addVertex(fromVert)
        if toVert not in self.vertList:
            temp = self.addVertex(toVert)

        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)

    def getVertex(self, vertKey):
        """ Returns the Vertex object from the vertList """
        if vertKey in self.vertList:
            return self.vertList[vertKey]
        else:
            return None

    def getVertices(self):
        """ Returns all vertices from the graph """
        return self.vertList.keys()

    def getNumVertices(self):
        """ Returns the number of vertices in the graph """
        return self.numVertices

    def transpose(self):
        """ Creates the transpose of the graph """
        tempVertList = {}

        # Traverses the graph
        for vert in self:
            # Exchanges edges
            vertKey = vert.getId()

            for nbr in vert.getConnections():
                nbrKey = nbr.getId()

                # Adds vertices to the new tempVertList
                if nbrKey not in tempVertList:
                    nbrVert = Vertex(nbrKey)
                    tempVertList[nbrKey] = nbrVert

                if vertKey not in tempVertList:
                    newVert = Vertex(vertKey)
                    tempVertList[vertKey] = newVert

                # Gets weight from the previous edge
                weight = vert.getWeight(self.vertList[nbrKey])

                # Sets new transpose edge
                tempVertList[nbrKey].addNeighbor(tempVertList[vertKey], weight)

        self.vertList = tempVertList


class VertexBFS(Vertex):
    """ Vertex implementation for Breadth First Search Algorithm """

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
    """ Graph Implementation for Breadth First Search Algorithm """

    def __init__(self):
        super().__init__()

    def addVertex(self, key):
        """ Adds a vertex to the graph """
        newVertex = VertexBFS(key)
        self.vertList[key] = newVertex
        self.numVertices += 1
        return newVertex

    def addEdge(self, fromVert, toVert, weight=0):
        """ Adds a weighted edge to the first vertex """
        if fromVert not in self.vertList:
            temp = self.addVertex(fromVert)
        if toVert not in self.vertList:
            temp = self.addVertex(toVert)

        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)

    def getVertex(self, vertKey):
        return super().getVertex(vertKey)

    def getVertices(self):
        return super().getVertices()

    def bfs(self, startKey):
        """ Breadth First Search Algorithm """
        start = self.getVertex(startKey)
        start.setPredecessor(None)
        start.setDistance(0)
        vertQueue = Queue1()
        vertQueue.enqueue(start)

        # Traverse through graph until every Vertex is explored
        while vertQueue.size() > 0:
            # Grab current vertex from vertQueue
            currentVert = vertQueue.dequeue()

            # Look at current vertex edges
            for neighbor in currentVert.getConnections():
                # Neighbor has not been explored before
                if neighbor.getColor() == "white":
                    neighbor.setColor("gray")
                    neighbor.setPredecessor(currentVert)
                    neighbor.setDistance(currentVert.getDistance() + 1)
                    vertQueue.enqueue(neighbor)

            # Current vertex has now been explored completely
            currentVert.setColor("black")


class VertexDFS(VertexBFS):
    """ Vertex Implementation for the Depth First Search Algorithm """

    def __init__(self, key):
        super().__init__(key)
        self.discovery = 0
        self.finish = 0

    def setDiscovery(self, dtime):
        self.discovery = dtime

    def setFinish(self, ftime):
        self.finish = ftime

    def getDiscovery(self):
        return self.discovery

    def getFinish(self):
        return self.finish


class GraphDFS(GraphBFS):
    """ Graph Implementation for the Depth First Search Algorithm """

    def __init__(self):
        super().__init__()
        self.time = 0

    def addVertex(self, key):
        """ Adds a vertex to the graph """
        newVertex = VertexDFS(key)
        self.vertList[key] = newVertex
        self.numVertices += 1
        return newVertex

    def addEdge(self, fromVert, toVert, weight=0):
        """ Adds a weighted edge to the first vertex """
        if fromVert not in self.vertList:
            temp = self.addVertex(fromVert)
        if toVert not in self.vertList:
            temp = self.addVertex(toVert)

        self.vertList[fromVert].addNeighbor(self.vertList[toVert], weight)

    def getVertex(self, vertKey):
        return super().getVertex(vertKey)

    def getVertices(self):
        return super().getVertices()

    def dfs(self):
        """ Depth Fist Search Algorithm """
        # Sets up every graph's vertex
        for vertex in self:
            vertex.setColor("white")
            vertex.setPredecessor(-1)

        # Iterates over all vertices of the graph
        for vertex in self:
            if vertex.getColor() == "white":
                self.dfsVisit(vertex)

    def dfsVisit(self, startVertex):
        startVertex.setColor("gray")
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == "white":
                nextVertex.setPredecessor(startVertex)
                self.dfsVisit(nextVertex)
        startVertex.setColor("black")
        self.time += 1
        startVertex.setFinish(self.time)


def main():
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

    graph.transpose()
    print("\nTranspose of Graph")
    for vertex in graph:
        print(vertex)


if __name__ == "__main__":
    main()
