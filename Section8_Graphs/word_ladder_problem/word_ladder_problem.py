import os
import sys
base_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(base_dir)
sys.path.append(parent_dir)
sys.path.insert(0, "Section4_Basic_Data_Structures/queue")
from graph_adj_list import GraphBFS, VertexBFS
from queue1 import Queue1



def buildGraph(wordFile):
    ''' Builds a word ladder from a list of words and returns it as a GraphBFS '''
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
            bucket = word[:i] + "_" + word[i+1:]
            bucket = bucket.upper()

            # Append word to bucket list
            if bucket in wordDict:
                wordDict[bucket].append(word)
            # Create bucket list with word
            else:
                wordDict[bucket] = [word]

    # for key, value in wordDict.items():
    #     print("wordDict[{}] = {}".format(key, value))

    # Creates edges for words in the buckets
    for wordsFromBucket in wordDict.values():
        # Iterates through bucket's list of words
        for i in range(len(wordsFromBucket) - 1):
            # Adds edge to directed graph for each previous word
            wordGraph.addEdge(wordsFromBucket[i], wordsFromBucket[i + 1])

    return wordGraph


def bfs(graph, startKey):
    ''' Breadth First Search Algorithm '''
    start = graph.getVertex(startKey)
    start.setPredecessor(None)
    start.setDistance(0)
    vertQueue = Queue1()
    vertQueue.enqueue(start)

    # Traverse through graph until every Vertex is explored
    while vertQueue.size() > 0:
        # Grab current vertex from vertQueue
        currentVert = vertQueue.dequeue()

        # Look at current vertex edges
        for neighbor in currentVert.getConnections():
            # Neighbor has not been explored before
            if neighbor.getColor() == "white":
                neighbor.setColor("gray")
                neighbor.setPredecessor(currentVert)
                neighbor.setDistance(currentVert.getDistance() + 1)
                vertQueue.enqueue(neighbor)

        # Current vertex has now been explored completely
        currentVert.setColor("black")


def traverseGraph(vertex):
    ''' Traverse graph from end to beginning '''
    temp = vertex
    while (temp.getPredecessor()):
        print(temp.getId())
        temp = temp.getPredecessor()
    print(temp.getId())

    
if __name__ == "__main__":
    g = buildGraph("wordlist")
    bfs(g, "FOOL")
    traverseGraph(g.getVertex("SAGE"))
