

V = {"P1", "P2", "P3", "P4", "P5"}
E = [{"P1", "P2"}, {"P1", "P3"}, {"P2", "P3"}, {"P3", "P4"}, {"P4", "P5"}]

def build_adjacency_list(edges, directed=False):
    graph = {}

    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        graph[u].append(v)

        if not directed:
            graph[v].append(u)

    return graph



def degrees(graph):
    degree = {}
    for v, line in graph.items():
        degree[v] = len(line)

    return degree



def in_out_degree(graph):
    in_degree = {v: 0 for v in graph}
    out_degree = {v: len(neighbours) for v, neighbours in graph.items()}

    for neighbours in graph.values():
        for v in neighbours:
            in_degree[v] += 1

    return in_degree, out_degree


# TASK  3
def dfs(graph, start):
    visited = set()
    order = []

    def visit(v):
        visited.add(v)
        order.append(v)

        for neighbour in sorted(graph[v]):
            if neighbour not in visited:
                visit(neighbour)

    visit(start)
    return order

def connected_components(graph):



def is_weakly_connected(graph):

# TASK 4

