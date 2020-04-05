import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
from graph_adj_list import GraphBFS, VertexBFS


def buildBoardGraph(bdSize):
    """ Builds Graph with bdSize vertices and bdSize - 1 edges """
    boardGraph = GraphBFS()
    for row in range(bdSize):
        for col in range(bdSize):
            vertId = posToVertexId(row, col, bdSize)
            legalPositions = generateLegalMoves(row, col, bdSize)

            for pos in legalPositions:
                nbrId = posToVertexId(pos[0], pos[1], bdSize)
                boardGraph.addEdge(vertId, nbrId)

    return boardGraph


def posToVertexId(row, col, bdSize):
    """ Coverts coordinates into square position number """
    return (row * bdSize) + col


def legalCoord(coord, bdSize):
    """ Checks if coordinate is withing the limits of the board """
    if coord >= 0 and coord < bdSize:
        return True
    else:
        return False


def generateLegalMoves(row, col, bdSize):
    """ Generates knight's legal moves in current position """
    legalMoves = []
    offsets = [(-1, -2), (1, -2), (2, -1), (-2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2)]

    for offset in offsets:
        x = row + offset[0]
        y = col + offset[1]

        if legalCoord(x, bdSize) and legalCoord(y, bdSize):
            legalMoves.append((x, y))

    return legalMoves


def knightTour(depthLevel, vertPath, currentVert, depthLimit):
    """ Knight's Tour Algorithm """
    # Vertex is now explored
    currentVert.setColor("gray")
    vertPath.append(currentVert)

    # Recursive can until every vertex is explored without repetition
    if depthLevel < depthLimit:
        nbrList = list(currentVert.getConnections())
        i = 0
        done = False

        # Traverse through the graph
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == "white":
                done = knightTour(depthLevel + 1, vertPath, nbrList[i], depthLimit)
            i += 1

        # Dead end found, prepare to backtrack the vertPath
        if not done:
            vertPath.pop()
            currentVert.setColor("white")

    # Full vertices path found
    else:
        done = True

    return done


if __name__ == "__main__":
    boardGraph = buildBoardGraph(8)
    for vertex in boardGraph:
        print(vertex)

    path = []
    print(knightTour(0, path, boardGraph.getVertex(0), 64))
    print("OK")
