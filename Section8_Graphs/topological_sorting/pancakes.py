import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
from graph_adj_list import VertexDFS, GraphDFS


def buildPancakeGraph():
    """ Builds a Graph for a Pancake recipe """
    pancakeGraph = GraphDFS()
    ingredients = ["3/4 cup milk", "1 egg", "1 Tbl Oil", "1 cup mix"]
    instructions = [
        "heat syrup",
        "heat griddle",
        "pour 1/4 cup",
        "turn when bubbly",
        "eat",
    ]

    pancakeGraph.addEdge(ingredients[0], ingredients[3])
    pancakeGraph.addEdge(ingredients[1], ingredients[3])
    pancakeGraph.addEdge(ingredients[2], ingredients[3])

    pancakeGraph.addEdge(ingredients[3], instructions[0])
    pancakeGraph.addEdge(ingredients[3], instructions[2])
    pancakeGraph.addEdge(instructions[1], instructions[2])
    pancakeGraph.addEdge(instructions[2], instructions[3])
    pancakeGraph.addEdge(instructions[3], instructions[4])
    pancakeGraph.addEdge(instructions[0], instructions[4])

    return pancakeGraph


def topologicalSorting(dfsGraph):
    """ Sorts the vertices in descending order by finish time """
    finishTimes = [vertex.finish for vertex in dfsGraph]
    finishTimes.sort()
    finishTimes.reverse()

    sortedVertices = []

    for finishtime in finishTimes:
        for vertex in dfsGraph:
            if vertex.finish == finishtime:
                sortedVertices.append(vertex)

    return sortedVertices


if __name__ == "__main__":
    pancakeGraph = buildPancakeGraph()
    pancakeGraph.dfs()

    for vertex in pancakeGraph:
        print(vertex.id, vertex.discovery, vertex.finish)

    sortedGraph = topologicalSorting(pancakeGraph)

    for vertex in sortedGraph:
        print(vertex.id, vertex.finish)
