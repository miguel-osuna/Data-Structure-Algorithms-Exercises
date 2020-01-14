import os
import sys
base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
sys.path.insert(0, "Section7_Trees/binary_heap")
from graph_adj_list import GraphBFS, VertexBFS


class PriorityQueue:
    def __init__(self):
        self.heapArray = [(0,0)]
        self.currentSize = 0

    def buildHeap(self,alist):
        self.currentSize = len(alist)
        self.heapArray = [(0,0)]
        for i in alist:
            self.heapArray.append(i)
        i = len(alist) // 2            
        while (i > 0):
            self.percDown(i)
            i = i - 1
                        
    def percDown(self,i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapArray[i][0] > self.heapArray[mc][0]:
                tmp = self.heapArray[i]
                self.heapArray[i] = self.heapArray[mc]
                self.heapArray[mc] = tmp
            i = mc
                
    def minChild(self,i):
        if i*2 > self.currentSize:
            return -1
        else:
            if i*2 + 1 > self.currentSize:
                return i*2
            else:
                if self.heapArray[i*2][0] < self.heapArray[i*2+1][0]:
                    return i*2
                else:
                    return i*2+1

    def percUp(self,i):
        while i // 2 > 0:
            if self.heapArray[i][0] < self.heapArray[i//2][0]:
               tmp = self.heapArray[i//2]
               self.heapArray[i//2] = self.heapArray[i]
               self.heapArray[i] = tmp
            i = i//2
 
    def add(self,k):
        self.heapArray.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def delMin(self):
        retval = self.heapArray[1][1]
        self.heapArray[1] = self.heapArray[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapArray.pop()
        self.percDown(1)
        return retval
        
    def isEmpty(self):
        if self.currentSize == 0:
            return True
        else:
            return False

    def decreaseKey(self,val,amt):
        ''' Updates the value of the vertices with a new distance '''
        done = False
        i = 1
        myKey = 0

        while not done and i <= self.currentSize:
            if self.heapArray[i][1] == val:
                done = True
                myKey = i
            else:
                i = i + 1

        if myKey > 0:
            self.heapArray[myKey] = (amt,self.heapArray[myKey][1])
            self.percUp(myKey)
            
    def __contains__(self,vertex):
        for pair in self.heapArray:
            if pair[1] == vertex:
                return True
        return False
        
def dijkstra(g, s):
    ''' Dijkstra's Shortest Path Algorithm '''

    # Initialize every vertex in the graph
    for vertex in g:
        vertex.setPredecessor(None)
        vertex.setDistance(sys.maxsize)

    # Get the starting vertex
    start = g.getVertex(s)
    start.setDistance(0)

    # Build the priority queue
    pq = PriorityQueue()
    pq.buildHeap([(v.getDistance(), v) for v in g])

    while not pq.isEmpty():
        currentVert = pq.delMin()

        # Traverse through all the neighbors 
        for nextVert in currentVert.getConnections():
            newDistance = currentVert.getDistance() + currentVert.getWeight(nextVert)
            
            if newDistance < nextVert.getDistance():
                nextVert.setDistance(newDistance)
                nextVert.setPredecessor(currentVert)
                pq.decreaseKey(nextVert, newDistance)

def getShortestPath(g, fromVert, toVert):
    ''' Prints path from one vertex to another '''
    currentVert = g.getVertex(toVert)

    while currentVert.getPredecessor() != None and currentVert.getId() != fromVert:
        print("from {} to {}, distance of {}".format(currentVert.getPredecessor().getId(), currentVert.getId(), currentVert.getDistance()))
        currentVert = currentVert.getPredecessor()

    return g.getVertex(toVert).getDistance()

def buildTestGraph():
    ''' Creates an example graph '''
    g = GraphBFS()
    
    # U neighbors
    g.addEdge("u", "v", 2)
    g.addEdge("u", "w", 5)
    g.addEdge("u", "x", 1)

    # V neighbors
    g.addEdge("v", "u", 2)
    g.addEdge("v", "x", 2)
    g.addEdge("v", "w", 3)

    # X neighbors
    g.addEdge("x", "u", 1)
    g.addEdge("x", "v", 2)
    g.addEdge("x", "w", 3)
    g.addEdge("x", "y", 1)

    # W neighbors
    g.addEdge("w", "v", 3)
    g.addEdge("w", "u", 5)
    g.addEdge("w", "x", 3)
    g.addEdge("w", "y", 1)
    g.addEdge("w", "z", 5)

    # Z neighbors
    g.addEdge("z", "w", 5)
    g.addEdge("z", "y", 1)

    # Y neighbors 
    g.addEdge("y", "x", 1)
    g.addEdge("y", "w", 1)
    g.addEdge("y", "z", 1)    
    
    return g


if __name__ == "__main__":
    g = buildTestGraph()

    dijkstra(g, "u")
    getShortestPath(g, "u", "y")
    print("\n")
    getShortestPath(g, "u", "z")



    


