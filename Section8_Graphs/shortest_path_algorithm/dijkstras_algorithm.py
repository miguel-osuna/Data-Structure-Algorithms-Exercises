import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
sys.path.insert(0, "Section7_Trees/binary_heap")
from graph_adj_list import GraphBFS, VertexBFS


class PriorityQueue:
    def __init__(self):
        self.heap_array = [(0, 0)]
        self.current_size = 0

    def build_heap(self, a_list):
        self.current_size = len(a_list)
        self.heap_array = [(0, 0)]
        for i in a_list:
            self.heap_array.append(i)
        i = len(a_list) // 2
        while i > 0:
            self.perc_down(i)
            i = i - 1

    def perc_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_array[i][0] > self.heap_array[mc][0]:
                tmp = self.heap_array[i]
                self.heap_array[i] = self.heap_array[mc]
                self.heap_array[mc] = tmp
            i = mc

    def min_child(self, i):
        if i * 2 > self.current_size:
            return -1
        else:
            if i * 2 + 1 > self.current_size:
                return i * 2
            else:
                if self.heap_array[i * 2][0] < self.heap_array[i * 2 + 1][0]:
                    return i * 2
                else:
                    return i * 2 + 1

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_array[i][0] < self.heap_array[i // 2][0]:
                tmp = self.heap_array[i // 2]
                self.heap_array[i // 2] = self.heap_array[i]
                self.heap_array[i] = tmp
            i = i // 2

    def add(self, k):
        self.heap_array.append(k)
        self.current_size = self.current_size + 1
        self.perc_up(self.current_size)

    def del_min(self):
        retval = self.heap_array[1][1]
        self.heap_array[1] = self.heap_array[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_array.pop()
        self.perc_down(1)
        return retval

    def is_empty(self):
        if self.current_size == 0:
            return True
        else:
            return False

    def decrease_key(self, val, amt):
        """ Updates the value of the vertices with a new distance """
        done = False
        i = 1
        my_key = 0

        while not done and i <= self.current_size:
            if self.heap_array[i][1] == val:
                done = True
                my_key = i
            else:
                i = i + 1

        if my_key > 0:
            self.heap_array[my_key] = (amt, self.heap_array[my_key][1])
            self.perc_up(my_key)

    def __contains__(self, vertex):
        for pair in self.heap_array:
            if pair[1] == vertex:
                return True
        return False


def dijkstra(g, s):
    """ Dijkstra's Shortest Path Algorithm """

    # Initialize every vertex in the graph
    for vertex in g:
        vertex.set_predecessor(None)
        vertex.set_distance(sys.maxsize)

    # Get the starting vertex
    start = g.get_vertex(s)
    start.set_distance(0)

    # Build the priority queue
    pq = PriorityQueue()
    pq.build_heap([(v.get_distance(), v) for v in g])

    while not pq.is_empty():
        current_vert = pq.del_min()

        # Traverse through all the neighbors
        for next_vert in current_vert.get_connections():
            new_distance = current_vert.get_distance() + current_vert.get_weight(
                next_vert
            )

            if new_distance < next_vert.get_distance():
                next_vert.set_distance(new_distance)
                next_vert.set_predecessor(current_vert)
                pq.decrease_key(next_vert, new_distance)


def get_shortest_path(g, from_vert, to_vert):
    """ Prints path from one vertex to another """
    current_vert = g.get_vertex(to_vert)

    while current_vert.get_predecessor() != None and current_vert.get_id() != from_vert:
        print(
            "from {} to {}, distance of {}".format(
                current_vert.get_predecessor().get_id(),
                current_vert.get_id(),
                current_vert.get_distance(),
            )
        )
        current_vert = current_vert.get_predecessor()

    return g.get_vertex(to_vert).get_distance()


def build_test_graph():
    """ Creates an example graph """
    g = GraphBFS()

    # U neighbors
    g.add_edge("u", "v", 2)
    g.add_edge("u", "w", 5)
    g.add_edge("u", "x", 1)

    # V neighbors
    g.add_edge("v", "u", 2)
    g.add_edge("v", "x", 2)
    g.add_edge("v", "w", 3)

    # X neighbors
    g.add_edge("x", "u", 1)
    g.add_edge("x", "v", 2)
    g.add_edge("x", "w", 3)
    g.add_edge("x", "y", 1)

    # W neighbors
    g.add_edge("w", "v", 3)
    g.add_edge("w", "u", 5)
    g.add_edge("w", "x", 3)
    g.add_edge("w", "y", 1)
    g.add_edge("w", "z", 5)

    # Z neighbors
    g.add_edge("z", "w", 5)
    g.add_edge("z", "y", 1)

    # Y neighbors
    g.add_edge("y", "x", 1)
    g.add_edge("y", "w", 1)
    g.add_edge("y", "z", 1)

    return g


def main():
    g = build_test_graph()

    dijkstra(g, "u")
    get_shortest_path(g, "u", "y")
    print("\n")
    get_shortest_path(g, "u", "z")


if __name__ == "__main__":
    main()
