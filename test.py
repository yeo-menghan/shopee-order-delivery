# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
 
# Library for INT_MAX
import sys
 
# read through the text file, convert it into a giant list of lists and make meaning out of it

a_file = open("text.txt", "r")

list_of_lists = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

a_file.close()

list_of_lists = [[int(int(j)) for j in i] for i in list_of_lists]

print(list_of_lists)

# making GLOBAL variables out of the list of lists
NUM_CITIES = list_of_lists[0][0]
NUM_WAREHOUSES = list_of_lists[0][1]
NUM_ROADS = list_of_lists[0][2]
print(NUM_CITIES)

class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.V-1):
            print("Adjacency list of vertex {}\n head".format(i+1), end="")
            temp = self.graph[i+1]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    # def __init__(self, vertices):
    #     self.V = vertices
    #     self.graph = [[0 for column in range(vertices)]
    #                 for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
 
        # Search nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[x] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                dist[y] > dist[x] + self.graph[x][y]:
                        dist[y] = dist[x] + self.graph[x][y]
 
        self.printSolution(dist)
 
# # Driver program
# g = Graph(9)
# g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#         [4, 0, 8, 0, 0, 0, 0, 11, 0],
#         [0, 8, 0, 7, 0, 4, 0, 0, 2],
#         [0, 0, 7, 0, 9, 14, 0, 0, 0],
#         [0, 0, 0, 9, 0, 10, 0, 0, 0],
#         [0, 0, 4, 14, 10, 0, 2, 0, 0],
#         [0, 0, 0, 0, 0, 2, 0, 1, 6],
#         [8, 11, 0, 0, 0, 0, 1, 0, 7],
#         [0, 0, 2, 0, 0, 0, 6, 7, 0]
#         ];

# generate graph - iterate through list of lists from 1 to NUM_ROADS and add edges
V = NUM_ROADS
graph = Graph(V)
# remember that its from 1 to before NUM_ROADS + 1
graph_data = list_of_lists[1:NUM_ROADS+1]
for pair in graph_data:
    graph.add_edge(pair[0], pair[1])
graph.print_graph()

graph.dijkstra(0);