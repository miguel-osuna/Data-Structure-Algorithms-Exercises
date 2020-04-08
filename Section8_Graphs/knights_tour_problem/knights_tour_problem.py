import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
from graph_adj_list import GraphBFS, VertexBFS


def build_board_graph(board_size):
    """ Builds Graph with board_size vertices and board_size - 1 edges """
    board_graph = GraphBFS()
    for row in range(board_size):
        for col in range(board_size):
            vertId = post_to_vertex_id(row, col, board_size)
            legal_positions = generate_legal_moves(row, col, board_size)

            for pos in legal_positions:
                nbrId = post_to_vertex_id(pos[0], pos[1], board_size)
                board_graph.add_edge(vertId, nbrId)

    return board_graph


def post_to_vertex_id(row, col, board_size):
    """ Coverts coordinates into square position number """
    return (row * board_size) + col


def legal_coord(coord, board_size):
    """ Checks if coordinate is withing the limits of the board """
    if coord >= 0 and coord < board_size:
        return True
    else:
        return False


def generate_legal_moves(row, col, board_size):
    """ Generates knight's legal moves in current position """
    legal_moves = []
    offsets = [(-1, -2), (1, -2), (2, -1), (-2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2)]

    for offset in offsets:
        x = row + offset[0]
        y = col + offset[1]

        if legal_coord(x, board_size) and legal_coord(y, board_size):
            legal_moves.append((x, y))

    return legal_moves


def knight_tour(depth_level, vert_path, current_vert, depth_limit):
    """ Knight's Tour Algorithm """
    # Vertex is now explored
    current_vert.set_color("gray")
    vert_path.append(current_vert)

    # Recursive can until every vertex is explored without repetition
    if depth_level < depth_limit:
        nbr_list = list(current_vert.get_connections())
        i = 0
        done = False

        # Traverse through the graph
        while i < len(nbr_list) and not done:
            if nbr_list[i].get_color() == "white":
                done = knight_tour(depth_level + 1, vert_path, nbr_list[i], depth_limit)
            i += 1

        # Dead end found, prepare to backtrack the vert_path
        if not done:
            vert_path.pop()
            current_vert.set_color("white")

    # Full vertices path found
    else:
        done = True

    return done


def main():
    board_graph = build_board_graph(8)
    for vertex in board_graph:
        print(vertex)

    path = []
    print(knight_tour(0, path, board_graph.get_vertex(0), 64))
    print("OK")


if __name__ == "__main__":
    main()
