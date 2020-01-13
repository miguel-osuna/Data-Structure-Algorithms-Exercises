import os
import sys
base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
from graph_adj_list import VertexBFS, GraphBFS


class VertexDFS(VertexBFS):
    ''' Vertex Implementation for the Depth First Search Algorithm '''
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
    ''' Graph Implementation for the Depth First Search Algorithm '''
    def __init__(self):
        super().__init__()
        self.time = 0

    def addVertex(self, key):
        ''' Adds a vertex to the graph '''
        newVertex = VertexDFS(key)
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


    def dfs(self):
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


if __name__ == "__main__":
    g = GraphDFS()
    print(g)