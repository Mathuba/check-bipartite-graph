#Uses python3

import sys
from collections import deque


def add_edge(graph, vertex1, vertex2):
    """Build edges of graph by adding vertex2 to addjacent list of vertex1.
    
    Vertex1 is also added to vertex2 adjacent list. If vertex1 is not in
    the graph, vertex1 is added as new key.
    
    Parameters
    ----------
    graph: dictionary
        The graph being constructed as adjacency list.
    vertex1, vertex2:int
        vertex1 is the key and vertex2 is the neighbour to vertex 1
        all values greater than 0.
    """

    edges = (vertex1, vertex2)
    (v1, v2) = (edges)
    if v1 in graph:
        if v2 not in graph[v1]:
            graph[v1].append(v2)
            graph[v2].append(v1)
        else:
            graph[v1] = v2
    

def bipartite(adj):
    #write your code here
    return -1

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}
    for _ in range(m):
        vert1, vert2 = map(int, sys.stdin.readline().split())
        add_edge(graph, vert1, vert2)

    # print(bipartite(adj))
    print(graph)
