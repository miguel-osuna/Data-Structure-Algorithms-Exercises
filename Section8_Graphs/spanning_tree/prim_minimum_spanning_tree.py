# Standard library imports
import os
import sys

# Local application imports
base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
sys.path.insert(0, "Section7_Trees/binary_heap")
from shortest_path_algorithm.dijkstras_algorithm import PriorityQueue
from graph_adj_list import GraphBFS, VertexBFS


def prim(g, start):
    """ Prim's Algorithm to find the Minimum Spanning Tree of a Graph class"""

    # Initialize every vertex in the graph
    for vertex in g:
        vertex.set_predecessor(None)
        vertex.set_distance(sys.maxsize)

    # Get the starting vertex
    start = g.get_vertex(start)
    start.set_distance(0)

    # Build the priority queue with the vertices distances
    pq = PriorityQueue()
    pq.build_heap([(vert.get_distance(), vert) for vert in g])

    while not pq.is_empty():
        current_vert = pq.del_min()

        # Traverse through all the neighbors
        for next_vert in current_vert.get_connections():
            new_cost = current_vert.get_distance() + current_vert.get_weight(next_vert)

            # Compare distance
            if next_vert in pq and new_cost < next_vert.get_distance():
                next_vert.set_predecessor(current_vert)
                next_vert.set_distance(new_cost)
                pq.decrease_key(next_vert, new_cost)


def print_path(g, end):
    path = []
    current_vert = g.get_vertex("G")
    while current_vert != None:
        path.insert(0, current_vert)
        current_vert = current_vert.get_predecessor()

    for vert in path:
        print("{} distance = {}".format(vert.get_id(), vert.get_distance()))


def generate_internet_radio_graph():
    g = GraphBFS()

    # Vertex A Edges
    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 3)

    # Vertex B Edges
    g.add_edge("B", "A", 2)
    g.add_edge("B", "C", 1)
    g.add_edge("B", "D", 1)
    g.add_edge("B", "E", 4)

    # Vertex C Edges
    g.add_edge("C", "A", 3)
    g.add_edge("C", "B", 1)
    g.add_edge("C", "F", 5)

    # Vertex D Edges
    g.add_edge("D", "B", 1)
    g.add_edge("D", "E", 1)

    # Vertex E Edges
    g.add_edge("E", "B", 4)
    g.add_edge("E", "D", 1)
    g.add_edge("E", "F", 1)

    # Vertex F Edges
    g.add_edge("F", "E", 1)
    g.add_edge("F", "C", 5)
    g.add_edge("F", "G", 1)

    # Vertex G Edges
    g.add_edge("G", "F", 1)

    return g


def main():
    g = generate_internet_radio_graph()
    prim(g, "A")
    print_path(g, "G")


if __name__ == "__main__":
    main()
