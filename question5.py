
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
class AllPaths:
    
    # initializing graph that would be used in functions
    def __init__(self, graph):
        self.graph = graph

    # function to calculate and update adjacent distances that are shortest from satrt vertex to a particular vertex
    def calculate_distance(self, start):
        # dictionary that holds nodes and their shortest distances from the first node that have been solved
        solved = {start : 0}
        # initailzing a dictionary that holds the adjacent nodes in the graph from the starting point, the variable holds a queue a priority queue data structure
        adjacents = queue.PriorityQueue()
        # updating all adjacent points around the starting node
        self.update_adjacents(start, solved, adjacents)
        # while loop that runs so long as the list of adjacents is not empty
        while not adjacents.empty():
            # get distance and value of the adjacent node
            (distance, value) = adjacents.get()
            # if the adjacent value already in solved then we continue
            if value in solved:
                continue
             # add node and distance to our dictionary of solved nodes
            solved[value] = distance
            # Update the adjacents nodes to the list of adjacents
            self.update_adjacents(value, solved, adjacents)
            # return dictionary containing solved 
        return solved

    # function that updatess adjacent nodes
    def update_adjacents(self, parent, solved, adjacents):
        # get all edges in the graph
        edges = self.graph.get_vertex(parent).get_edges()
        # add new node, distance, orevious slved distance of parent node plus the new distance 
        for value, distance in edges.items():
            adjacents.put((solved[parent] + distance, value))

# short reach function that actually does most of the required task by using the classes created above
def shortestReach(n,edges,s):
    # initialize graph by passing in the number of nodes
    graph = Graph(n)
    
    # loop through from 0 to he number of nodes
    for i in range(n):
        # get vertex from, vertex, and the distance between two of them frm=om the matrix of edges passed into the function
        start,end,dist = edges[i][0], edges[i][1], edges[i][2]
        # add vertex to the graph by specifying the end of that vertex and the distance
        graph.get_vertex(start).add_edge(end, dist)
        # on that same vertex, use the node to and add same edge now with the node from and the distance between them
        graph.get_vertex(end).add_edge(start, dist)
    # pass graph to our AllPaths class
    allpaths = AllPaths(graph)
    # stating the starting point on our graph
    start = s
    # use the disktra calculate distances function to get all distances from the start node to all other nodes on the graph
    distances = allpaths.calculate_distance(start)
     # since distances is a dictionary and the first key in that dictionary is the start index with value as zero, hence we delete it from the dictionary
    del distances[s]
    # sorting the dictionary by the keys
    distancess = sorted(distances)
    
    # initializing empty list that holds the distances for the final out put
    distance = []
    
    # loop through our sorted dictionary list
    for i in range(len(distancess)):
        # use value of sorted dictionary list as index in our distances dictionary to get value and store in empty list above
        distance.append(distances[distancess[i]])
    
    # display list as strings
    return ' '.join(map(str, distance))


n = 5

edges = [[1,2,5],[2,3,6],[3,4,2],[1,3,15],[1,5,-1],[2,5,-1],[3,5,-1],[4,5,-1]]
s = 1

print(shortestReach(n,edges,s))


