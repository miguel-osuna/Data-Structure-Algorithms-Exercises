import os
import sys

base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
sys.path.insert(0, "Section8_Graphs/")
from graph_adj_list import GraphBFS, VertexBFS


def buildGraph(wordFile):
    """ Builds a word ladder from a list of words and returns it as a GraphBFS """
    fileName = os.path.join(base_dir, wordFile)

    if ".txt" not in fileName:
        fileName += ".txt"

    wordDict = {}
    wordGraph = GraphBFS()
    words = open(fileName, "r")

    # Creates buckets of words in text file
    for line in words:
        word = line[:-1]
        for i in range(len(word)):
            # Generates len(word) number of buckets
            bucket = word[:i] + "_" + word[i + 1 :]
            bucket = bucket.upper()

            # Append word to bucket list
            if bucket in wordDict:
                wordDict[bucket].append(word)
            # Create bucket list with word
            else:
                wordDict[bucket] = [word]

    # Creates edges for words in the buckets
    for wordsFromBucket in wordDict.values():
        # Iterates through bucket's list of words
        for i in range(len(wordsFromBucket) - 1):
            # Adds edge to directed graph for each previous word
            wordGraph.addEdge(wordsFromBucket[i], wordsFromBucket[i + 1])

    return wordGraph


def traverseGraph(g, startKey, endKey):
    """ Traverse graph from end to beginning """
    temp = g.getVertex(endKey)
    path = []
    path.insert(0, temp.getId())

    while temp.getPredecessor() != None and temp.getId() != startKey:
        temp = temp.getPredecessor()
        path.insert(0, temp.getId())

    for node in path:
        print(node)


def main():
    g = buildGraph("wordlist")
    g.bfs("FOOL")
    traverseGraph(g, "FOOL", "SAGE")


if __name__ == "__main__":
    main()
