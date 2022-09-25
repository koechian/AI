# imports

import matplotlib.pyplot as plt
import networkx as nx


def UCS(graph, start, goal):
    # opened, closed = [], []

    print("Uniform Cost Search:")
    # return path


def DDFS(range):
    print("Iterative Deepening DFS:")
    # return path
    pass


def draw(graph):
    # drawing the graph

    # randomizing node position on the graph
    pos = nx.spring_layout(graph, k=1)

    # creating edge list and weight list
    edges = [(u, v) for (u, v, d) in graph.edges(data=True)]
    edge_labels = nx.get_edge_attributes(graph, "weight")

    nx.draw_networkx_edges(graph, pos, edgelist=edges, width=2)
    nx.draw_networkx_nodes(graph, pos, node_size=200)
    nx.draw_networkx_labels(graph, pos, font_size=12, font_family="SF Pro Display")
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

draw(DG)
