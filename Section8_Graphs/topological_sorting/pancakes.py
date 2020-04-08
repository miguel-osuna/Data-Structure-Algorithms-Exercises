import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
from graph_adj_list import VertexDFS, GraphDFS


def build_pancake_graph():
    """ Builds a Graph for a Pancake recipe """
    pancake_graph = GraphDFS()
    ingredients = ["3/4 cup milk", "1 egg", "1 Tbl Oil", "1 cup mix"]
    instructions = [
        "heat syrup",
        "heat griddle",
        "pour 1/4 cup",
        "turn when bubbly",
        "eat",
    ]

    pancake_graph.add_edge(ingredients[0], ingredients[3])
    pancake_graph.add_edge(ingredients[1], ingredients[3])
    pancake_graph.add_edge(ingredients[2], ingredients[3])

    pancake_graph.add_edge(ingredients[3], instructions[0])
    pancake_graph.add_edge(ingredients[3], instructions[2])
    pancake_graph.add_edge(instructions[1], instructions[2])
    pancake_graph.add_edge(instructions[2], instructions[3])
    pancake_graph.add_edge(instructions[3], instructions[4])
    pancake_graph.add_edge(instructions[0], instructions[4])

    return pancake_graph


def topological_sorting(dfs_graph):
    """ Sorts the vertices in descending order by finish time """
    finish_times = [vertex.finish for vertex in dfs_graph]
    finish_times.sort()
    finish_times.reverse()

    sorted_vertices = []

    for finish_time in finish_times:
        for vertex in dfs_graph:
            if vertex.finish == finish_time:
                sorted_vertices.append(vertex)

    return sorted_vertices


def main():
    pancake_graph = build_pancake_graph()
    pancake_graph.dfs()

    for vertex in pancake_graph:
        print(vertex.id, vertex.discovery, vertex.finish)

    sorted_graph = topological_sorting(pancake_graph)

    for vertex in sorted_graph:
        print(vertex.id, vertex.finish)


if __name__ == "__main__":
    main()
