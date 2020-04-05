import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
sys.path.insert(0, "Section7_Trees/binary_heap")
from shortest_path_algorithm.dijkstras_algorithm import PriorityQueue
from graph_adj_list import GraphBFS, VertexBFS


def prim(g, start):
    """ Prim's Algorithm to find the Minimum Spanning Tree of a Graph """

    # Initialize every vertex in the graph
    for vertex in g:
        vertex.setPredecessor(None)
        vertex.setDistance(sys.maxsize)

    # Get the starting vertex
    start = g.getVertex(start)
    start.setDistance(0)

    # Build the priority queue with the vertices distances
    pq = PriorityQueue()
    pq.buildHeap([(vert.getDistance(), vert) for vert in g])

    while not pq.isEmpty():
        currentVert = pq.delMin()

        # Traverse through all the neighbors
        for nextVert in currentVert.getConnections():
            newCost = currentVert.getDistance() + currentVert.getWeight(nextVert)

            # Compare distance
            if nextVert in pq and newCost < nextVert.getDistance():
                nextVert.setPredecessor(currentVert)
                nextVert.setDistance(newCost)
                pq.decreaseKey(nextVert, newCost)


def printPath(g, end):
    path = []
    currentVert = g.getVertex("G")
    while currentVert != None:
        path.insert(0, currentVert)
        currentVert = currentVert.getPredecessor()

    for vert in path:
        print("{} distance = {}".format(vert.getId(), vert.getDistance()))


def generateInternetRadioGraph():
    g = GraphBFS()

    # Vertex A Edges
    g.addEdge("A", "B", 2)
    g.addEdge("A", "C", 3)

    # Vertex B Edges
    g.addEdge("B", "A", 2)
    g.addEdge("B", "C", 1)
    g.addEdge("B", "D", 1)
    g.addEdge("B", "E", 4)

    # Vertex C Edges
    g.addEdge("C", "A", 3)
    g.addEdge("C", "B", 1)
    g.addEdge("C", "F", 5)

    # Vertex D Edges
    g.addEdge("D", "B", 1)
    g.addEdge("D", "E", 1)

    # Vertex E Edges
    g.addEdge("E", "B", 4)
    g.addEdge("E", "D", 1)
    g.addEdge("E", "F", 1)

    # Vertex F Edges
    g.addEdge("F", "E", 1)
    g.addEdge("F", "C", 5)
    g.addEdge("F", "G", 1)

    # Vertex G Edges
    g.addEdge("G", "F", 1)

    return g


def main():
    g = generateInternetRadioGraph()
    prim(g, "A")
    printPath(g, "G")


if __name__ == "__main__":
    main()
