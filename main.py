from networkx import DiGraph
import random

from networkx.classes import graph


def generate_graph(nodes=5, edges=6) -> DiGraph:

    if edges < nodes:
        return Exception("Graph is not connected")
    else:
        _nodes = list(range(0, nodes))

        graph = DiGraph()
        graph.add_nodes_from(_nodes)

        i = 0

        while i < edges:
            start = random.choice(_nodes)
            end = random.choice(_nodes)
            if ((start, end) not in graph) and (start != end):
                graph.add_edge(start, end)
                graph.add_edge(end, start)
                i = i + 1

    return graph


graph = generate_graph(6, 7)
edges = graph.edges(0)

print(edges)


def find_articular_points(graph: DiGraph):

    result = []
    visited = [False for _ in graph]
    time_in = [0 for _ in graph]
    time_up = [0 for _ in graph]
    timer = 0

    def dfs(vertex: int, parent: int = -1):
        nonlocal timer
        nonlocal time_in
        nonlocal time_up
        nonlocal visited
        nonlocal result

        print(visited)

        visited[vertex] = True
        timer += 1
        time_in[vertex] = time_up[vertex] = timer
        children = 0

        for edge in graph.edges(vertex):
            to = edge[1]
            if (to is parent):
                continue
            if (visited[to]):
                time_up[vertex] = time_up[vertex] if time_up[vertex] < time_in[to] else time_in[to]
            else:
                dfs(vertex=to, parent=vertex)
                time_up[vertex] = time_up[vertex] if time_up[vertex] < time_in[to] else time_in[to]
                if time_up[to] >= time_in[vertex] and parent is not -1:
                    if vertex not in result:
                        result.append(vertex)
                children += 1

        if parent is -1 and children > 1:
            if vertex not in result:
                result.append(vertex)

    dfs(0)

    return result
