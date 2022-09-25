# DFS Traversal of an unweighted graph

# 136745 Ryan Ombatti
# 131860 Kuria Timothy
# 135803 Muthiore Maria
# 135357 Ian Koech
# 134703 Rita Maringa
# 134701 Sean Kinuthia


def dfs(graph, node):

    visited = []
    queue = []

    queue.append(node)
    visited.append(node)

    while queue:
        s = queue.pop()
        print(s)
        for x in graph[s][::-1]:
            if x not in visited:
                visited.append(x)
                queue.append(x)


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["E", "C"],
}

dfs(graph, "A")
