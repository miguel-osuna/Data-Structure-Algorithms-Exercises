# import os
# import sys

# base_dir = os.path.dirname(os.path.abspath(__file__))
# parent_dir = os.path.dirname(base_dir)
# sys.path.append(parent_dir)
# sys.path.insert(0, "Section4_Basic_Data_Structures/queue")
from queue1 import Queue1


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def __str__(self):
        return str(self.id) + " connected to: " + str([x.id for x in self.connectedTo])

    def add_neighbor(self, neighbor, weight=0):
        """ Adds a vertex neighbor to the current one """
        self.connectedTo[neighbor] = weight

    def get_connections(self):
        """ Returns all the neighbor vertices """
        return self.connectedTo.keys()

    def get_id(self):
        """ Returns the id of the current vertex """
        return self.id

    def get_weight(self, neighbor):
        """ Returns the weight between the neighbor and the current vertex """
        return self.connectedTo[neighbor]


class Graph:
    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def __str__(self):
        return "Vertices: " + str(self.get_vertices())

    def __len__(self):
        return self.get_num_vertices()

    def __contains__(self, vert_key):
        return vert_key in self.vert_list[vert_key]

    def __iter__(self):
        return iter(self.vert_list.values())

    def add_vertex(self, key):
        """ Adds a vertex to the graph """
        newVertex = Vertex(key)
        self.vert_list[key] = newVertex
        self.num_vertices += 1
        return newVertex

    def add_edge(self, from_vert, to_vert, weight=0):
        """ Adds a weighted edge to the first vertex """
        if from_vert not in self.vert_list:
            temp = self.add_vertex(from_vert)
        if to_vert not in self.vert_list:
            temp = self.add_vertex(to_vert)

        self.vert_list[from_vert].add_neighbor(self.vert_list[to_vert], weight)

    def get_vertex(self, vert_key):
        """ Returns the Vertex object from the vert_list """
        if vert_key in self.vert_list:
            return self.vert_list[vert_key]
        else:
            return None

    def get_vertices(self):
        """ Returns all vertices from the graph """
        return self.vert_list.keys()

    def get_num_vertices(self):
        """ Returns the number of vertices in the graph """
        return self.num_vertices

    def transpose(self):
        """ Creates the transpose of the graph """
        temp_vert_list = {}

        # Traverses the graph
        for vert in self:
            # Exchanges edges
            vert_key = vert.get_id()

            for nbr in vert.get_connections():
                nbr_key = nbr.get_id()

                # Adds vertices to the new temp_vert_list
                if nbr_key not in temp_vert_list:
                    nbr_vert = Vertex(nbr_key)
                    temp_vert_list[nbr_key] = nbr_vert

                if vert_key not in temp_vert_list:
                    new_vert = Vertex(vert_key)
                    temp_vert_list[vert_key] = new_vert

                # Gets weight from the previous edge
                weight = vert.get_weight(self.vert_list[nbr_key])

                # Sets new transpose edge
                temp_vert_list[nbr_key].add_neighbor(temp_vert_list[vert_key], weight)

        self.vert_list = temp_vert_list


class VertexBFS(Vertex):
    """ Vertex implementation for Breadth First Search Algorithm """

    def __init__(self, key):
        super().__init__(key)
        self.distance = 0
        self.predecessor = None
        self.color = "white"

    def get_distance(self):
        return self.distance

    def get_predecessor(self):
        return self.predecessor

    def get_color(self):
        return self.color

    def set_distance(self, d):
        self.distance = d

    def set_predecessor(self, p):
        self.predecessor = p

    def set_color(self, c):
        self.color = c


class GraphBFS(Graph):
    """ Graph Implementation for Breadth First Search Algorithm """

    def __init__(self):
        super().__init__()

    def add_vertex(self, key):
        """ Adds a vertex to the graph """
        newVertex = VertexBFS(key)
        self.vert_list[key] = newVertex
        self.num_vertices += 1
        return newVertex

    def add_edge(self, from_vert, to_vert, weight=0):
        """ Adds a weighted edge to the first vertex """
        if from_vert not in self.vert_list:
            temp = self.add_vertex(from_vert)
        if to_vert not in self.vert_list:
            temp = self.add_vertex(to_vert)

        self.vert_list[from_vert].add_neighbor(self.vert_list[to_vert], weight)

    def get_vertex(self, vert_key):
        return super().get_vertex(vert_key)

    def get_vertices(self):
        return super().get_vertices()

    def bfs(self, startKey):
        """ Breadth First Search Algorithm """
        start = self.get_vertex(startKey)
        start.set_predecessor(None)
        start.set_distance(0)
        vertQueue = Queue1()
        vertQueue.enqueue(start)

        # Traverse through graph until every Vertex is explored
        while vertQueue.size() > 0:
            # Grab current vertex from vertQueue
            current_vert = vertQueue.dequeue()

            # Look at current vertex edges
            for neighbor in current_vert.get_connections():
                # Neighbor has not been explored before
                if neighbor.get_color() == "white":
                    neighbor.set_color("gray")
                    neighbor.set_predecessor(current_vert)
                    neighbor.set_distance(current_vert.get_distance() + 1)
                    vertQueue.enqueue(neighbor)

            # Current vertex has now been explored completely
            current_vert.set_color("black")


class VertexDFS(VertexBFS):
    """ Vertex Implementation for the Depth First Search Algorithm """

    def __init__(self, key):
        super().__init__(key)
        self.discovery = 0
        self.finish = 0

    def set_discovery(self, dtime):
        self.discovery = dtime

    def set_finish(self, ftime):
        self.finish = ftime

    def get_discovery(self):
        return self.discovery

    def get_finish(self):
        return self.finish


class GraphDFS(GraphBFS):
    """ Graph Implementation for the Depth First Search Algorithm """

    def __init__(self):
        super().__init__()
        self.time = 0

    def add_vertex(self, key):
        """ Adds a vertex to the graph """
        newVertex = VertexDFS(key)
        self.vert_list[key] = newVertex
        self.num_vertices += 1
        return newVertex

    def add_edge(self, from_vert, to_vert, weight=0):
        """ Adds a weighted edge to the first vertex """
        if from_vert not in self.vert_list:
            temp = self.add_vertex(from_vert)
        if to_vert not in self.vert_list:
            temp = self.add_vertex(to_vert)

        self.vert_list[from_vert].add_neighbor(self.vert_list[to_vert], weight)

    def get_vertex(self, vert_key):
        return super().get_vertex(vert_key)

    def get_vertices(self):
        return super().get_vertices()

    def dfs(self):
        """ Depth Fist Search Algorithm """
        # Sets up every graph's vertex
        for vertex in self:
            vertex.set_color("white")
            vertex.set_predecessor(-1)

        # Iterates over all vertices of the graph
        for vertex in self:
            if vertex.get_color() == "white":
                self.dfs_visit(vertex)

    def dfs_visit(self, startVertex):
        startVertex.set_color("gray")
        self.time += 1
        startVertex.set_discovery(self.time)
        for nextVertex in startVertex.get_connections():
            if nextVertex.get_color() == "white":
                nextVertex.set_predecessor(startVertex)
                self.dfs_visit(nextVertex)
        startVertex.set_color("black")
        self.time += 1
        startVertex.set_finish(self.time)


def main():
    graph = Graph()

    for num in range(6):
        graph.add_vertex(num)

    # Vertex V0
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 5, 2)

    # Vertex V1
    graph.add_edge(1, 2, 4)

    # Vertex V2
    graph.add_edge(2, 3, 9)

    # Vertex V3
    graph.add_edge(3, 4, 7)
    graph.add_edge(3, 5, 3)

    # Vertex V4
    graph.add_edge(4, 0, 1)

    # Vertex V5
    graph.add_edge(5, 2, 1)
    graph.add_edge(5, 4, 8)

    for vertex in graph:
        print(vertex)

    graph.transpose()
    print("\nTranspose of Graph")
    for vertex in graph:
        print(vertex)


if __name__ == "__main__":
    main()
