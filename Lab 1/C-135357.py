# imports

from queue import PriorityQueue
import matplotlib.pyplot as plt
import networkx as nx


def ucs(graph, start, goal):
    # used the end='' to prevent skipping a line
    print("Uniform Cost Search:", end="")

    # a queue is used to store the nodes and a list to keep track of visited nodes
    q = PriorityQueue()
    # start node is marked as visited
    q.put((0, start))

    visited = []

    while True:
        if q.empty():
            print("Goal not attainable")
            return False

        w, current = q.get()
        # print(current)
        visited.append(current)

        if current == goal:
            print(visited)
            return

        for node in graph[current]:
            q.put((w + graph_costs(graph, current, node), node))


def graph_costs(graph, start, end):
    return graph[start][end]["weight"]


def ddfs(graph, start, goal, depth):
    # recursively calles the helper(DLS) until it reaches exhausts all nodes in the range
    print("Iterative Deepening DFS:" + start + "->", end="")
    # used the end='' to print on one line
    for i in range(depth):
        if ddfs_helper(graph, start, goal, i):
            return True
    return False


def ddfs_helper(graph, start, goal, depth):

    # checks if the start node is the goal node
    if start == goal:
        return True

    # checks if the range has been attained
    if depth <= 0:
        return False

    # recurse for all next nodes
    for i in graph[start]:
        # this is the list to be output
        if ddfs_helper(graph, i, goal, depth - 1):
            ddfs_list.append(i)
            return True

    return False


def draw(graph):
    # drawing the graph
    # randomizing node position on the graph
    pos = nx.spring_layout(graph, k=1)

    # creating edge list and weight list
    edges = [(u, v) for (u, v, d) in graph.edges(data=True)]
    edge_labels = nx.get_edge_attributes(graph, "weight")

    nx.draw_networkx_edges(graph, pos, edgelist=edges, width=1)
    nx.draw_networkx_nodes(graph, pos, node_size=200)
    nx.draw_networkx_labels(graph, pos, font_size=12, font_family="serif")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels)

    plt.show()


# graph dict creation

graph = {}

graph["A"] = {}
graph["A"]["D"] = 43
graph["A"]["O"] = 151

graph["B"] = {}
graph["B"]["G"] = 171

graph["C"] = {}
graph["C"]["B"] = 171
graph["C"]["D"] = 126

graph["D"] = {}
graph["D"]["F"] = 111
graph["D"]["M"] = 200
graph["D"]["O"] = 136

graph["E"] = {}
graph["E"]["A"] = 133
graph["E"]["L"] = 110

graph["F"] = {}
graph["F"]["H"] = 130
graph["F"]["G"] = 88

graph["G"] = {}
graph["G"]["C"] = 140
graph["G"]["D"] = 123
graph["G"]["H"] = 99

graph["H"] = {}
graph["H"]["N"] = 80

graph["I"] = {}
graph["I"]["C"] = 102
graph["I"]["A"] = 109

graph["J"] = {}
graph["J"]["E"] = 105
graph["J"]["I"] = 172
graph["J"]["K"] = 146

graph["K"] = {}
graph["K"]["E"] = 146
graph["K"]["L"] = 152

graph["L"] = {}
graph["L"]["O"] = 97

graph["M"] = {}
graph["M"]["N"] = 67

graph["N"] = {}

graph["O"] = {}
graph["O"]["M"] = 100


# creating a directed graph using the networks library
DG = nx.DiGraph()
# adding the adjacency list into the directional graph object created by netwokx

for x, y in graph.items():
    for a, b in y.items():
        # where x is the current node, a is the neighbour and b is the cost of the edge
        DG.add_edge(x, a, weight=b)

# Main Code
# list to store ddfs results
ddfs_list = []


# function used to visualize the graph uncomment to see the graph weights and links
draw(DG)

# # Iterative DDFS
# ddfs(DG, "A", "N", 10)
# # reversing the list using a negative step
# print(ddfs_list[::-1])

# ucs(DG, "A", "N")
