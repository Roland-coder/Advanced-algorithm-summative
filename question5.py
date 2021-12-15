
import sys
import queue


# class the holds the structure of the vertex
class Vertex:
    #initializing the structure, which has an empty list of edges
    def __init__(self):
        self.edges = {}
    
    #function that gets edges stored in the class
    def get_edges(self):
        return self.edges
    
    # adding edges that are connected to our vertex, this includes the current vertex,the value of the next vertex an the distance between them
    def add_edge(self, val, dist):
        # check if the next vertex is not already in the current edges or the distance is less than the distance currently in that edge location 
        if val not in self.edges or dist < self.edges[val]:
            #adding the edge to our vertex
            self.edges[val] = dist


# Class that holds the structure of the graph 
class Graph:
    # initializing the graph by adding all initial number of vertices to the vertex structure initiated above
    def __init__(self, N):
        self.vertices = {}
        # This checks to ensure that all the number of nodes are added in as vertices, it runs untill number of nodes equals zero
        while N > 0:
            self.vertices[N] = Vertex()
            N -= 1

    # function to get vertices in our graph, it just returns the vertices initiated in the init function above
    def get_vertices(self):
        return self.vertices
        
    # function to get the vertex in our graph found in a particular index location

    def get_vertex(self, value):
        return self.vertices[value]

    # function to add new vertex in our graph at a particular index location

    def add_vertex(self, value, vertex):
        self.vertices[value] = vertex


# Dijkstra class to check and calculate the shortest distance between all vertices that have been solved
class Dijkstra:
    
    # initializing graph that would be used in functions
    def __init__(self, graph):
        self.graph = graph

    # function to calculate and update adjacent distances that are shortest from satrt vertex to a particular vertex
    def calculate(self, start):
        solved = {start : 0}
        adjacents = queue.PriorityQueue()
        self.update_adjacents(start, solved, adjacents)
        while not adjacents.empty():
            (distance, value) = adjacents.get()
            if value in solved:
                continue
            solved[value] = distance
            self.update_adjacents(value, solved, adjacents)
        return solved

    def update_adjacents(self, parent, solved, adjacents):
        edges = self.graph.get_vertex(parent).get_edges()
        for value, distance in edges.items():
            adjacents.put((solved[parent] + distance, value))

def shortestReach(n,edges,s):
    graph = Graph(n)
    
    for i in range(n):
        start,end,dist = edges[i][0], edges[i][1], edges[i][2]
        graph.get_vertex(start).add_edge(end, dist)
        graph.get_vertex(end).add_edge(start, dist)
    dijkstra = Dijkstra(graph)
    start = s
    distances = dijkstra.calculate(start)
    distance = list()
    for i in range(1, n + 1):
        if i == start:
            continue
        if i not in distances:
            distance.append(-1)
        else:
            distance.append(distances[i])
    return ' '.join(map(str, distance))


n = 5

edges = [[1,2,5],[2,3,6],[3,4,2],[1,3,15],[1,5,-1],[2,5,-1],[3,5,-1],[4,5,-1]]
s = 1

print(shortestReach(n,edges,s))

#1
#4 4
#1 2 24
#1 4 20
#1 3 3
#3 4 12
#1
