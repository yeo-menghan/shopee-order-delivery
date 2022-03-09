# library for int max
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

# A class to represent the adjacency list of the node

class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


# A graph is the list of the adjacency lists.
# Size of the array will be the no. of vertices "V"
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

    # Function to print the graph
    # Made it i+1 to start from 1 instead of 0. Thus eliminating need to subtract 1 from every value from the list of lists
    def print_graph(self):
        for i in range(self.V-1):
            print("Adjacency list of vertex {}\n head".format(i+1), end="")
            temp = self.graph[i+1]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


# generate graph - iterate through list of lists from 1 to NUM_ROADS and add edges
V = NUM_ROADS
graph = Graph(V)
# remember that its from 1 to before NUM_ROADS + 1
graph_data = list_of_lists[1:NUM_ROADS+1]
for pair in graph_data:
    graph.add_edge(pair[0], pair[1])
graph.print_graph()

# assign value to the warehouse nodes via a dictionary
# number of item X, delivery fee per km and location of warehouse
warehouse_data = list_of_lists[NUM_ROADS+1:NUM_ROADS+NUM_WAREHOUSES+1]
print(warehouse_data)

# assign value to the order nodes
num_of_orders = list_of_lists[NUM_ROADS+NUM_WAREHOUSES+1][0]

order_list = list_of_lists[NUM_ROADS+NUM_WAREHOUSES+2:NUM_ROADS+NUM_WAREHOUSES+2+num_of_orders]
print(order_list)

node_order_ls = []
node_order_amt_ls = []

for order in order_list:
    node_order_ls.append(order[1])
    node_order_amt_ls.append(order[0])

print(node_order_ls)
print(node_order_amt_ls)

order_dict = {}
for (node_order_ls, node_order_amt_ls) in zip(node_order_ls,node_order_amt_ls):
    if node_order_ls in order_dict.keys():
        #if the value is already in list, add current score to the sum
        order_dict[node_order_ls] += node_order_amt_ls
    else:
        #if the value is not yet in list, create an entry
        order_dict[node_order_ls] = node_order_amt_ls

print(order_dict)

### finished extracting values and assigning values to the nodes ###

# find shortest pathways from warehouse nodes to order nodes via Dijkstra's shortest path algo
# consider the cost efficiency by considering cost / km



# serve the node with the least number of connected nodes - compare the distance away from each warehouse


# consider inventory of each warehouse and rank the delivery route
