import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
sys.path.insert(0, "Section8_Graphs/")
from graph_adj_list import GraphBFS, VertexBFS


def build_graph(wordFile):
    """ Builds a word ladder from a list of words and returns it as a GraphBFS """
    file_name = os.path.join(base_dir, wordFile)

    if ".txt" not in file_name:
        file_name += ".txt"

    word_dict = {}
    word_graph = GraphBFS()
    words = open(file_name, "r")

    # Creates buckets of words in text file
    for line in words:
        word = line[:-1]
        for i in range(len(word)):
            # Generates len(word) number of buckets
            bucket = word[:i] + "_" + word[i + 1 :]
            bucket = bucket.upper()

            # Append word to bucket list
            if bucket in word_dict:
                word_dict[bucket].append(word)
            # Create bucket list with word
            else:
                word_dict[bucket] = [word]

    # Creates edges for words in the buckets
    for word_from_bucket in word_dict.values():
        # Iterates through bucket's list of words
        for i in range(len(word_from_bucket) - 1):
            # Adds edge to directed graph for each previous word
            word_graph.add_edge(word_from_bucket[i], word_from_bucket[i + 1])

    return word_graph


def traverse_graph(g, startKey, endKey):
    """ Traverse graph from end to beginning """
    temp = g.get_vertex(endKey)
    path = []
    path.insert(0, temp.get_id())

    while temp.get_predecessor() != None and temp.get_id() != startKey:
        temp = temp.get_predecessor()
        path.insert(0, temp.get_id())

    for node in path:
        print(node)


def main():
    g = build_graph("wordlist")
    g.bfs("FOOL")
    traverse_graph(g, "FOOL", "SAGE")


if __name__ == "__main__":
    main()
